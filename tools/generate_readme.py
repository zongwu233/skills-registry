#!/usr/bin/env python3
"""
Skills Registry README Generator

Generate a human-readable README.md from skills-registry.json
"""

import sys
import io
import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict

# Fix Windows console encoding
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')


def load_registry(registry_path: str) -> dict:
    """Load the skills registry"""
    with open(registry_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def generate_readme(data: dict) -> str:
    """Generate README content from registry data"""

    lines = []

    # Header
    lines.append("# Claude Skills Registry")
    lines.append("")
    lines.append("A centralized registry of Claude Skills available for installation via Skills Store.")
    lines.append("")

    # About section
    lines.append("## About")
    lines.append("")
    lines.append("This registry contains a curated list of Claude Skills that can be discovered and installed")
    lines.append("using [Skills Store](https://github.com/your-username/skills-store). Each skill entry includes")
    lines.append("metadata, source information, and installation details.")
    lines.append("")

    # Statistics
    stats = data.get('stats', {})
    lines.append("## Statistics")
    lines.append("")
    lines.append(f"- **Total Skills**: {stats.get('total_skills', 0)}")
    lines.append(f"- **Total Sources**: {stats.get('total_sources', 0)}")
    lines.append(f"- **Last Updated**: {data.get('last_updated', 'Unknown')}")
    lines.append("")

    # Quick links
    lines.append("## Quick Links")
    lines.append("")
    categories = data.get('categories', {})
    if categories:
        for cat_id, cat_info in sorted(categories.items()):
            name = cat_info.get('name', cat_id)
            count = cat_info.get('count', 0)
            lines.append(f"- [{name}](#{cat_id.replace('_', '-')}) ({count} skills)")
    lines.append("")

    # Skills by category
    lines.append("## Skills by Category")
    lines.append("")

    # Group skills by category
    skills_by_category = defaultdict(list)
    for skill_name, skill in data.get('skills', {}).items():
        category = skill.get('metadata', {}).get('category', 'other')
        skills_by_category[category].append((skill_name, skill))

    # Sort categories
    sorted_categories = sorted(skills_by_category.items())

    for category, skills in sorted_categories:
        # Get category info
        cat_info = categories.get(category, {})
        cat_name = cat_info.get('name', category.title())
        cat_desc = cat_info.get('description', '')

        # Category header
        lines.append(f"### {cat_name}")
        lines.append("")

        if cat_desc:
            lines.append(f"{cat_desc}")
            lines.append("")

        # Sort skills by name
        skills.sort(key=lambda x: x[0])

        # List skills
        for skill_name, skill in skills:
            lines.append(f"#### {skill_name}")
            lines.append("")

            description = skill.get('description', 'No description')
            lines.append(f"**Description**: {description}")
            lines.append("")

            # Source info
            source = skill.get('source', {})
            source_type = source.get('type', 'unknown')

            if source_type == 'github':
                repo = source.get('repo', 'unknown')
                url = source.get('url', '')
                lines.append(f"**Source**: [GitHub]({url})")
                lines.append("")
            elif source_type == 'local':
                path = source.get('path', 'unknown')
                lines.append(f"**Source**: Local (`{path}`)")
                lines.append("")

            # Metadata
            metadata = skill.get('metadata', {})

            # Author
            if metadata.get('author'):
                lines.append(f"**Author**: {metadata['author']}")

            # License
            if metadata.get('license'):
                lines.append(f"**License**: {metadata['license']}")

            # Tags
            tags = metadata.get('tags', [])
            if tags:
                tags_str = ', '.join(tags)
                lines.append(f"**Tags**: `{tags_str}`")

            lines.append("")

            # Installation hint
            lines.append("**Installation**:")
            lines.append("")
            lines.append("```bash")
            lines.append(f"python scripts/install_skill.py {skill_name}")
            lines.append("```")
            lines.append("")

    # Usage section
    lines.append("## Usage")
    lines.append("")
    lines.append("### Prerequisites")
    lines.append("")
    lines.append("1. Install [Skills Store](https://github.com/your-username/skills-store)")
    lines.append("2. Ensure you have Python 3.7+ and required dependencies")
    lines.append("")

    lines.append("### Installing a Skill")
    lines.append("")
    lines.append("```bash")
    lines.append("# Search for skills")
    lines.append("python scripts/search_skills.py \"keyword\"")
    lines.append("")
    lines.append("# Install a specific skill")
    lines.append("python scripts/install_skill.py <skill-name>")
    lines.append("```")
    lines.append("")

    # Contributing section
    lines.append("## Contributing")
    lines.append("")
    lines.append("To add a new skill to the registry:")
    lines.append("")
    lines.append("1. Fork this repository")
    lines.append("2. Edit `skills/skills-registry.json`")
    lines.append("3. Add your skill following the [schema](docs/SCHEMA.md)")
    lines.append("4. Run validation: `python tools/validate_registry.py`")
    lines.append("5. Regenerate this README: `python tools/generate_readme.py`")
    lines.append("6. Submit a pull request")
    lines.append("")

    # Schema reference
    lines.append("## Schema Reference")
    lines.append("")
    lines.append("For detailed information about the registry schema, see [SCHEMA.md](docs/SCHEMA.md).")
    lines.append("")

    # Footer
    lines.append("---")
    lines.append("")
    lines.append("**Maintained by**: The Claude Skills Community")
    lines.append("")
    lines.append("*This README is automatically generated from skills-registry.json*")
    lines.append("")
    lines.append(f"*Generated: {datetime.now().isoformat()}*")

    return '\n'.join(lines)


def main():
    """Main entry point"""
    # Default path
    registry_path = "skills/skills-registry.json"
    readme_path = "README.md"

    # Allow override via command line
    if len(sys.argv) > 1:
        registry_path = sys.argv[1]

    if len(sys.argv) > 2:
        readme_path = sys.argv[2]

    print(f"Loading registry from: {registry_path}")

    try:
        data = load_registry(registry_path)
    except Exception as e:
        print(f"❌ Error loading registry: {e}")
        return 1

    print(f"Generating README...")

    try:
        readme_content = generate_readme(data)

        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(readme_content)

        print(f"✅ README generated: {readme_path}")
        print("")
        print(f"  {len(data.get('skills', {}))} skills")
        print(f"  {len(data.get('categories', {}))} categories")

        return 0

    except Exception as e:
        print(f"❌ Error generating README: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
