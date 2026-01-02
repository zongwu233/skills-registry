#!/usr/bin/env python3
"""
Skills Registry Validator

Validate the skills-registry.json file for correctness and completeness.
"""

import sys
import io
import json
from pathlib import Path
from datetime import datetime

# Fix Windows console encoding
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')


def validate_registry(registry_path: str) -> tuple[bool, list[str]]:
    """
    Validate the skills registry JSON file

    Args:
        registry_path: Path to skills-registry.json

    Returns:
        Tuple of (is_valid, list_of_errors)
    """
    errors = []
    warnings = []

    # Check if file exists
    path = Path(registry_path)
    if not path.exists():
        return False, [f"Registry file not found: {registry_path}"]

    # Load JSON
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        return False, [f"Invalid JSON: {e}"]
    except Exception as e:
        return False, [f"Error reading file: {e}"]

    # Validate root structure
    required_root_fields = ['version', 'last_updated', 'skills']
    for field in required_root_fields:
        if field not in data:
            errors.append(f"Missing required root field: {field}")

    # Validate version
    if 'version' in data:
        version = data['version']
        if not isinstance(version, str):
            errors.append("Version must be a string")
        else:
            # Check semantic versioning format
            parts = version.split('.')
            if len(parts) != 3:
                errors.append("Version should follow semantic versioning (MAJOR.MINOR.PATCH)")

    # Validate last_updated timestamp
    if 'last_updated' in data:
        try:
            datetime.fromisoformat(data['last_updated'].replace('Z', '+00:00'))
        except ValueError:
            errors.append("last_updated should be ISO 8601 format (e.g., 2026-01-02T15:30:00Z)")

    # Validate skills object
    if 'skills' in data:
        if not isinstance(data['skills'], dict):
            errors.append("skills must be an object/dictionary")
        else:
            # Validate each skill
            for skill_name, skill in data['skills'].items():
                skill_errors = validate_skill(skill_name, skill)
                errors.extend(skill_errors)

    # Validate categories if present
    if 'categories' in data:
        if not isinstance(data['categories'], dict):
            errors.append("categories must be an object/dictionary")
        else:
            for cat_name, category in data['categories'].items():
                cat_errors = validate_category(cat_name, category)
                errors.extend(cat_errors)

    # Validate stats if present
    if 'stats' in data:
        stats_errors = validate_stats(data['stats'])
        errors.extend(stats_errors)

    # Check for warnings
    if 'skills' in data and 'stats' in data:
        total_skills = data['stats'].get('total_skills', 0)
        actual_count = len(data['skills'])
        if total_skills != actual_count:
            warnings.append(f"stats.total_skills ({total_skills}) doesn't match actual skill count ({actual_count})")

    return len(errors) == 0, errors + warnings


def validate_skill(name: str, skill: dict) -> list[str]:
    """Validate a single skill entry"""
    errors = []

    # Check required fields
    required_fields = ['name', 'description', 'source']
    for field in required_fields:
        if field not in skill:
            errors.append(f"Skill '{name}': Missing required field '{field}'")

    # Validate name matches key
    if 'name' in skill and skill['name'] != name:
        errors.append(f"Skill '{name}': name field ('{skill['name']}') doesn't match key ('{name}')")

    # Validate name format
    if not name.replace('-', '').replace('_', '').isalnum():
        errors.append(f"Skill '{name}': Name should contain only alphanumeric characters, hyphens, and underscores")

    # Validate source
    if 'source' in skill:
        source = skill['source']
        if not isinstance(source, dict):
            errors.append(f"Skill '{name}': source must be an object")
        else:
            if 'type' not in source:
                errors.append(f"Skill '{name}': source missing 'type' field")
            else:
                source_type = source['type']
                if source_type not in ['github', 'local']:
                    errors.append(f"Skill '{name}': source.type must be 'github' or 'local'")

                # Validate GitHub source
                if source_type == 'github':
                    required_github_fields = ['repo', 'path']
                    for field in required_github_fields:
                        if field not in source:
                            errors.append(f"Skill '{name}': source missing required field '{field}' for github type")

                    # Validate repo format
                    if 'repo' in source:
                        repo = source['repo']
                        if '/' not in repo:
                            errors.append(f"Skill '{name}': repo should be in 'owner/repo' format")

                # Validate local source
                if source_type == 'local':
                    if 'path' not in source:
                        errors.append(f"Skill '{name}': source missing 'path' field for local type")

    # Validate metadata if present
    if 'metadata' in skill:
        metadata = skill['metadata']
        if not isinstance(metadata, dict):
            errors.append(f"Skill '{name}': metadata must be an object")
        else:
            # Validate tags if present
            if 'tags' in metadata:
                tags = metadata['tags']
                if not isinstance(tags, list):
                    errors.append(f"Skill '{name}': metadata.tags must be an array")
                else:
                    for i, tag in enumerate(tags):
                        if not isinstance(tag, str):
                            errors.append(f"Skill '{name}': metadata.tags[{i}] must be a string")

            # Validate category if present
            if 'category' in metadata:
                if not isinstance(metadata['category'], str):
                    errors.append(f"Skill '{name}': metadata.category must be a string")

    return errors


def validate_category(name: str, category: dict) -> list[str]:
    """Validate a single category entry"""
    errors = []

    required_fields = ['name', 'description', 'count']
    for field in required_fields:
        if field not in category:
            errors.append(f"Category '{name}': Missing required field '{field}'")

    # Validate count is a number
    if 'count' in category:
        if not isinstance(category['count'], int):
            errors.append(f"Category '{name}': count must be an integer")

    return errors


def validate_stats(stats: dict) -> list[str]:
    """Validate the stats object"""
    errors = []

    required_fields = ['total_skills', 'total_sources', 'last_sync']
    for field in required_fields:
        if field not in stats:
            errors.append(f"stats: Missing required field '{field}'")

    # Validate types
    if 'total_skills' in stats and not isinstance(stats['total_skills'], int):
        errors.append("stats.total_skills must be an integer")

    if 'total_sources' in stats and not isinstance(stats['total_sources'], int):
        errors.append("stats.total_sources must be an integer")

    # Validate last_sync timestamp
    if 'last_sync' in stats:
        try:
            datetime.fromisoformat(stats['last_sync'].replace('Z', '+00:00'))
        except ValueError:
            errors.append("stats.last_sync should be ISO 8601 format")

    return errors


def main():
    """Main entry point"""
    # Default path
    registry_path = "skills/skills-registry.json"

    # Allow override via command line
    if len(sys.argv) > 1:
        registry_path = sys.argv[1]

    print(f"Validating: {registry_path}")
    print("")

    is_valid, errors = validate_registry(registry_path)

    if is_valid:
        print("✅ Registry is VALID!")
        print("")

        # Check if there are warnings
        warnings = [e for e in errors if 'Warning:' in e]
        if warnings:
            print("⚠️  Warnings:")
            for warning in warnings:
                print(f"   {warning}")
            print("")

        print("📊 Registry Statistics:")
        # Load and display stats
        with open(registry_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        print(f"   Version: {data.get('version', 'Unknown')}")
        print(f"   Total Skills: {data.get('stats', {}).get('total_skills', 'Unknown')}")
        print(f"   Total Sources: {data.get('stats', {}).get('total_sources', 'Unknown')}")
        print(f"   Last Updated: {data.get('last_updated', 'Unknown')}")
        print("")

        return 0
    else:
        print("❌ Registry is INVALID!")
        print("")

        errors_only = [e for e in errors if 'Warning:' not in e]
        if errors_only:
            print("🚫 Errors:")
            for error in errors_only:
                print(f"   {error}")
            print("")

        warnings = [e for e in errors if 'Warning:' in e]
        if warnings:
            print("⚠️  Warnings:")
            for warning in warnings:
                print(f"   {warning}")
            print("")

        return 1


if __name__ == "__main__":
    sys.exit(main())
