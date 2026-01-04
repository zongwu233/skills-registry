#!/usr/bin/env python3
"""
Add Skill to Registry

Interactive script to add a new skill to the registry.
"""

import sys
import json
from pathlib import Path
from datetime import datetime

def get_input(prompt, default=None, required=True):
    """Get user input with optional default"""
    if default:
        full_prompt = f"{prompt} [{default}]: "
    else:
        full_prompt = f"{prompt}: "

    value = input(full_prompt).strip()

    if not value and default:
        return default
    if not value and required:
        print(f"❌ This field is required!")
        sys.exit(1)

    return value

def main():
    """Main entry point"""
    print("🎯 Add New Skill to Registry")
    print("=" * 50)
    print()

    # Get skill information
    name = get_input("Skill name (lowercase, hyphens)", required=True)
    description = get_input("Description", required=True)

    print("\n📍 Source Information")
    repo = get_input("GitHub repo (owner/repo)", required=True)
    branch = get_input("Branch", default="main")
    path = get_input("Path to skill in repo", default="skills/" + name)

    print("\n📝 Metadata")
    author = get_input("Author", required=True)
    license_type = get_input("License", default="MIT")
    category = get_input(
        "Category",
        default="development",
        required=False
    )

    tags_input = get_input("Tags (comma-separated)", required=False)
    tags = [t.strip() for t in tags_input.split(",")] if tags_input else []

    # Build skill entry
    skill_entry = {
        "name": name,
        "description": description,
        "source": {
            "type": "github",
            "repo": repo,
            "url": f"https://github.com/{repo}",
            "branch": branch,
            "path": path
        },
        "metadata": {
            "author": author,
            "license": license_type,
            "tags": tags,
            "category": category
        }
    }

    # Load registry
    registry_path = Path(__file__).parent.parent / "skills" / "skills-registry.json"

    print(f"\n📂 Loading registry from {registry_path}")

    try:
        with open(registry_path, 'r', encoding='utf-8') as f:
            registry = json.load(f)
    except FileNotFoundError:
        print("❌ Registry file not found!")
        sys.exit(1)

    # Check if skill already exists
    if name in registry['skills']:
        response = input(f"\n⚠️  Skill '{name}' already exists. Overwrite? (y/N): ")
        if response.lower() != 'y':
            print("❌ Aborted.")
            sys.exit(0)

    # Add skill
    registry['skills'][name] = skill_entry

    # Update stats
    registry['last_updated'] = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    registry['stats']['total_skills'] = len(registry['skills'])

    # Save registry
    print(f"\n💾 Saving registry...")

    with open(registry_path, 'w', encoding='utf-8') as f:
        json.dump(registry, f, indent=2, ensure_ascii=False)

    print("✅ Skill added successfully!")
    print()
    print("📋 Summary:")
    print(f"  Name: {name}")
    print(f"  Description: {description}")
    print(f"  Source: {repo}")
    print(f"  Path: {path}")
    print()
    print("👉 Next steps:")
    print(f"  1. Run: python tools/validate_registry.py")
    print(f"  2. Run: python tools/generate_readme.py")
    print(f"  3. Run: git add . && git commit -m 'Add: {name} - {description}'")
    print(f"  4. Run: git push")

if __name__ == "__main__":
    main()
