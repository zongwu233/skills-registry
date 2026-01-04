#!/usr/bin/env python3
"""
Repository Manager

Advanced tool for managing skill repositories with config file support.
"""

import sys
import json
import requests
import io
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional

# Fix Windows console encoding
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

class Colors:
    """Terminal colors"""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'

def print_header(text: str):
    print(f"\n{Colors.HEADER}{Colors.BOLD}{'=' * 70}{Colors.END}")
    print(f"{Colors.HEADER}{Colors.BOLD}{text.center(70)}{Colors.END}")
    print(f"{Colors.HEADER}{Colors.BOLD}{'=' * 70}{Colors.END}\n")

def print_success(text: str):
    print(f"{Colors.GREEN}✅ {text}{Colors.END}")

def print_error(text: str):
    print(f"{Colors.RED}❌ {text}{Colors.END}")

def print_warning(text: str):
    print(f"{Colors.YELLOW}⚠️  {text}{Colors.END}")

def print_info(text: str):
    print(f"{Colors.CYAN}ℹ️  {text}{Colors.END}")

def load_config(config_path: Path) -> dict:
    """Load repository configuration"""
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print_error(f"Config file not found: {config_path}")
        sys.exit(1)

def save_config(config_path: Path, config: dict):
    """Save repository configuration"""
    with open(config_path, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2, ensure_ascii=False)

def fetch_github_contents(repo: str, path: str = "", branch: str = "main") -> Optional[dict]:
    """Fetch repository contents from GitHub API"""
    url = f"https://api.github.com/repos/{repo}/contents/{path}?ref={branch}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()
        return None
    except Exception as e:
        print_error(f"Request failed: {e}")
        return None

def find_skills_in_repo(repo: str, branch: str = "main") -> List[Dict]:
    """Find all skills in a repository"""
    skills_found = []
    search_paths = ["skills", ""]

    for search_path in search_paths:
        contents = fetch_github_contents(repo, search_path, branch)
        if contents and isinstance(contents, list):
            for item in contents:
                if item['type'] == 'dir':
                    dir_contents = fetch_github_contents(repo, item['path'], branch)
                    if dir_contents and isinstance(dir_contents, list):
                        has_skill_md = any(
                            f['name'].lower() == 'skill.md'
                            for f in dir_contents
                        )

                        if has_skill_md:
                            skills_found.append({
                                'name': item['name'],
                                'path': item['path'],
                                'repo': repo
                            })

    return skills_found

def categorize_skill(skill_name: str, description: str, categories: dict) -> str:
    """Auto-categorize a skill based on keywords"""
    skill_lower = skill_name.lower()
    desc_lower = description.lower()

    for category, config in categories.items():
        keywords = config.get('keywords', [])
        for keyword in keywords:
            if keyword.lower() in skill_lower or keyword.lower() in desc_lower:
                return category

    return "general"

def list_repositories(config: dict):
    """List all repositories in configuration"""
    print_header("📚 Configured Repositories")

    repos = config.get('repositories', [])
    if not repos:
        print_warning("No repositories configured")
        return

    print(f"{f"№":<3} {f"Enabled":<7} {f"Priority":<8} {f"Repository":<40} {f"Description"}")
    print("-" * 100)

    for i, repo_config in enumerate(repos, 1):
        enabled = "✅" if repo_config.get('enabled', True) else "❌"
        priority = repo_config.get('priority', 999)
        repo = repo_config['repo']
        desc = repo_config.get('description', '')

        print(f"{i:<3} {enabled:<7} {priority:<8} {repo:<40} {desc}")

    print(f"\n{Colors.GREEN}Total:{Colors.END} {len(repos)} repositories")

def add_repository(config: dict, config_path: Path):
    """Add a new repository to configuration"""
    print_header("➕ Add New Repository")

    repo = input(f"{Colors.BOLD}Repository (owner/repo):{Colors.END} ").strip()
    if not repo:
        print_error("Repository is required")
        return

    branch = input(f"{Colors.BOLD}Branch [main]:{Colors.END} ").strip() or "main"
    name = input(f"{Colors.BOLD}Name:{Colors.END} ").strip() or repo
    description = input(f"{Colors.BOLD}Description:{Colors.END} ").strip()
    priority = input(f"{Colors.BOLD}Priority [99]:{Colors.END} ").strip()
    priority = int(priority) if priority else 99

    new_repo = {
        "name": name,
        "repo": repo,
        "branch": branch,
        "enabled": True,
        "priority": priority,
        "description": description
    }

    config['repositories'].append(new_repo)
    config['repositories'].sort(key=lambda x: x.get('priority', 999))
    config['last_updated'] = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    save_config(config_path, config)
    print_success(f"Added {repo} to configuration")

def scan_repositories(config: dict, config_path: Path):
    """Scan enabled repositories and add skills"""
    print_header("🔍 Scan Repositories")

    registry_path = Path(__file__).parent.parent / "skills" / "skills-registry.json"

    try:
        with open(registry_path, 'r', encoding='utf-8') as f:
            registry = json.load(f)
    except FileNotFoundError:
        print_error("Registry file not found!")
        return

    # Get enabled repositories
    repos = [r for r in config.get('repositories', []) if r.get('enabled', True)]

    if not repos:
        print_warning("No enabled repositories found")
        print_info("Use 'repo_manager.py enable' to enable repositories")
        return

    print_info(f"Scanning {len(repos)} enabled repository(ies)...\n")

    all_skills = []
    repo_summary = {}

    for repo_config in repos:
        repo = repo_config['repo']
        branch = repo_config.get('branch', 'main')

        print(f"{Colors.BOLD}[{repo}]{Colors.END}")
        skills = find_skills_in_repo(repo, branch)

        if skills:
            print_success(f"Found {len(skills)} skill(s)")
            all_skills.extend(skills)
            repo_summary[repo] = {'found': len(skills), 'status': 'success'}
        else:
            print_warning("No skills found")
            repo_summary[repo] = {'found': 0, 'status': 'empty'}
        print()

    if not all_skills:
        print_error("No skills found!")
        return

    # Show summary
    print_header("📊 Scan Summary")
    print(f"Total skills found: {Colors.GREEN}{len(all_skills)}{Colors.END}\n")

    # Filter existing skills
    categories = config.get('categories', {})
    new_skills = []

    for skill in all_skills:
        if skill['name'] not in registry['skills']:
            # Auto-categorize
            category = categorize_skill(skill['name'], f"Skill from {skill['repo']}", categories)

            skill['category'] = category
            new_skills.append(skill)

    print(f"New skills: {Colors.GREEN}{len(new_skills)}{Colors.END}")
    print(f"Existing skills: {Colors.YELLOW}{len(all_skills) - len(new_skills)}{Colors.END}\n")

    if not new_skills:
        print_info("All skills already exist in registry")
        return

    # Ask for confirmation
    print(f"{Colors.YELLOW}Add {len(new_skills)} new skill(s)?{Colors.END}")
    choice = input(f"{Colors.BOLD}[y/N]:{Colors.END} ").strip().lower()

    if choice != 'y':
        print_info("Cancelled")
        return

    # Add skills to registry
    print_header("💾 Adding Skills")

    for skill in new_skills:
        skill_entry = {
            "name": skill['name'],
            "description": f"Skill from {skill['repo']}",
            "source": {
                "type": "github",
                "repo": skill['repo'],
                "url": f"https://github.com/{skill['repo']}",
                "branch": "main",
                "path": skill['path']
            },
            "metadata": {
                "author": skill['repo'].split('/')[0],
                "license": "Unknown",
                "tags": [],
                "category": skill.get('category', 'general')
            }
        }

        registry['skills'][skill['name']] = skill_entry
        print_success(f"Added {skill['name']}")

    # Update stats
    registry['last_updated'] = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    registry['stats']['total_skills'] = len(registry['skills'])

    with open(registry_path, 'w', encoding='utf-8') as f:
        json.dump(registry, f, indent=2, ensure_ascii=False)

    print()
    print_success(f"Added {len(new_skills)} skill(s) to registry!")
    print()
    print(f"{Colors.BOLD}Next steps:{Colors.END}")
    print(f"  1. {Colors.CYAN}python tools/validate_registry.py{Colors.END}")
    print(f"  2. {Colors.CYAN}python tools/generate_readme.py{Colors.END}")
    print(f"  3. {Colors.CYAN}git add . && git commit -m 'Add {len(new_skills)} skills from scan'{Colors.END}")
    print(f"  4. {Colors.CYAN}git push{Colors.END}")

def toggle_repository(config: dict, config_path: Path):
    """Toggle repository enabled status"""
    print_header("🔄 Toggle Repository")

    repos = config.get('repositories', [])

    print(f"{Colors.BOLD}Select repository to toggle:{Colors.END}\n")

    for i, repo_config in enumerate(repos, 1):
        enabled = "✅ Enabled" if repo_config.get('enabled', True) else "❌ Disabled"
        print(f"  {i}. {repo_config['repo']} - {enabled}")

    try:
        choice = int(input(f"\n{Colors.BOLD}Enter number:{Colors.END} ")) - 1
        if 0 <= choice < len(repos):
            repos[choice]['enabled'] = not repos[choice].get('enabled', True)
            status = "enabled" if repos[choice]['enabled'] else "disabled"
            save_config(config_path, config)
            print_success(f"{repos[choice]['repo']} {status}")
        else:
            print_error("Invalid selection")
    except ValueError:
        print_error("Invalid input")

def main():
    """Main entry point"""
    config_path = Path(__file__).parent.parent / "repositories.json"

    if not config_path.exists():
        print_error("repositories.json not found!")
        print_info("Create it first using the template")
        sys.exit(1)

    config = load_config(config_path)

    if len(sys.argv) < 2:
        # Interactive mode
        print_header("🎯 Repository Manager")

        print(f"{Colors.BOLD}Available actions:{Colors.END}")
        print(f"  {Colors.GREEN}1{Colors.END}. List repositories")
        print(f"  {Colors.GREEN}2{Colors.END}. Add repository")
        print(f"  {Colors.GREEN}3{Colors.END}. Scan and import skills")
        print(f"  {Colors.GREEN}4{Colors.END}. Toggle repository")
        print(f"  {Colors.GREEN}5{Colors.END}. Exit")

        choice = input(f"\n{Colors.BOLD}Choose action [1-5]:{Colors.END} ").strip()

        actions = {
            '1': list_repositories,
            '2': add_repository,
            '3': scan_repositories,
            '4': toggle_repository
        }

        if choice in actions:
            actions[choice](config, config_path)
        elif choice == '5':
            print_info("Goodbye!")
        else:
            print_error("Invalid choice")

    else:
        # Command line mode
        command = sys.argv[1].lower()

        commands = {
            'list': list_repositories,
            'add': add_repository,
            'scan': scan_repositories,
            'toggle': toggle_repository
        }

        if command in commands:
            commands[command](config, config_path)
        else:
            print_error(f"Unknown command: {command}")
            print_info(f"Available: {', '.join(commands.keys())}")

if __name__ == "__main__":
    main()
