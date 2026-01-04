#!/usr/bin/env python3
"""
Import Skills from GitHub Repository

Scan a GitHub repository and discover all skills automatically.
"""

import sys
import json
import requests
from pathlib import Path
from datetime import datetime

def fetch_github_contents(repo, path="", branch="main"):
    """Fetch repository contents from GitHub API"""
    url = f"https://api.github.com/repos/{repo}/contents/{path}?ref={branch}"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"❌ Failed to fetch {url}")
        print(f"   Status: {response.status_code}")
        return None

    return response.json()

def find_skills_in_repo(repo, branch="main", search_paths=["skills", ""]):
    """Find all skills in a repository"""
    print(f"🔍 Scanning {repo}...")
    skills_found = []

    for search_path in search_paths:
        print(f"   Searching in: {search_path or 'root'}")

        contents = fetch_github_contents(repo, search_path, branch)
        if not contents:
            continue

        for item in contents:
            if item['type'] == 'dir':
                # Check if this directory contains a SKILL.md
                dir_contents = fetch_github_contents(repo, item['path'], branch)
                if dir_contents:
                    has_skill_md = any(
                        f['name'].lower() == 'skill.md'
                        for f in dir_contents
                    )

                    if has_skill_md:
                        skill_name = item['name']
                        print(f"   ✅ Found: {skill_name}")

                        skills_found.append({
                            'name': skill_name,
                            'path': item['path']
                        })

    return skills_found

def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("Usage: python import_from_repo.py <owner/repo> [branch]")
        print()
        print("Example:")
        print("  python import_from_repo.py anthropic/skills")
        print("  python import_from_repo.py anthropic/skills main")
        sys.exit(1)

    repo = sys.argv[1]
    branch = sys.argv[2] if len(sys.argv) > 2 else "main"

    print(f"🎯 Import Skills from GitHub Repository")
    print("=" * 50)
    print(f"Repository: {repo}")
    print(f"Branch: {branch}")
    print()

    # Find skills
    skills = find_skills_in_repo(repo, branch)

    if not skills:
        print("❌ No skills found!")
        sys.exit(0)

    print(f"\n✅ Found {len(skills)} skill(s)")
    print()

    # Load registry
    registry_path = Path(__file__).parent.parent / "skills" / "skills-registry.json"

    try:
        with open(registry_path, 'r', encoding='utf-8') as f:
            registry = json.load(f)
    except FileNotFoundError:
        print("❌ Registry file not found!")
        sys.exit(1)

    # Ask for confirmation
    print("📋 Skills to add:")
    for i, skill in enumerate(skills, 1):
        exists = skill['name'] in registry['skills']
        status = "⚠️  EXISTS" if exists else "✅ NEW"
        print(f"  {i}. {status} - {skill['name']}")
        print(f"     Path: {skill['path']}")

    print()
    response = input("Continue? (y/N): ")

    if response.lower() != 'y':
        print("❌ Aborted.")
        sys.exit(0)

    # Add skills to registry
    added_count = 0
    skipped_count = 0

    for skill in skills:
        skill_name = skill['name']

        if skill_name in registry['skills']:
            print(f"⏭️  Skipped: {skill_name} (already exists)")
            skipped_count += 1
            continue

        # Create skill entry
        skill_entry = {
            "name": skill_name,
            "description": f"Skill from {repo}",
            "source": {
                "type": "github",
                "repo": repo,
                "url": f"https://github.com/{repo}",
                "branch": branch,
                "path": skill['path']
            },
            "metadata": {
                "author": repo.split('/')[0],
                "license": "Unknown",
                "tags": [],
                "category": "general"
            }
        }

        registry['skills'][skill_name] = skill_entry
        added_count += 1
        print(f"✅ Added: {skill_name}")

    # Update stats
    registry['last_updated'] = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    registry['stats']['total_skills'] = len(registry['skills'])

    # Save registry
    print()
    print(f"💾 Saving registry...")

    with open(registry_path, 'w', encoding='utf-8') as f:
        json.dump(registry, f, indent=2, ensure_ascii=False)

    print()
    print("✅ Import complete!")
    print(f"   Added: {added_count}")
    print(f"   Skipped: {skipped_count}")
    print()
    print("👉 Next steps:")
    print(f"  1. Edit skills/skills-registry.json to add descriptions and metadata")
    print(f"  2. Run: python tools/validate_registry.py")
    print(f"  3. Run: python tools/generate_readme.py")
    print(f"  4. Run: git add . && git commit -m 'Import skills from {repo}'")
    print(f"  5. Run: git push")

if __name__ == "__main__":
    main()
