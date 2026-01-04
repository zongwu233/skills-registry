#!/usr/bin/env python3
"""
Batch Skills Manager

A user-friendly tool for managing multiple skill repositories.
"""

import sys
import json
import requests
import io
from pathlib import Path
from datetime import datetime
from typing import List, Dict

# Fix Windows console encoding
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

class Colors:
    """Terminal colors for better output"""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'

def print_header(text: str):
    """Print formatted header"""
    print(f"\n{Colors.HEADER}{Colors.BOLD}{'=' * 60}{Colors.END}")
    print(f"{Colors.HEADER}{Colors.BOLD}{text.center(60)}{Colors.END}")
    print(f"{Colors.HEADER}{Colors.BOLD}{'=' * 60}{Colors.END}\n")

def print_success(text: str):
    """Print success message"""
    print(f"{Colors.GREEN}✅ {text}{Colors.END}")

def print_error(text: str):
    """Print error message"""
    print(f"{Colors.RED}❌ {text}{Colors.END}")

def print_warning(text: str):
    """Print warning message"""
    print(f"{Colors.YELLOW}⚠️  {text}{Colors.END}")

def print_info(text: str):
    """Print info message"""
    print(f"{Colors.CYAN}ℹ️  {text}{Colors.END}")

def fetch_github_contents(repo: str, path: str = "", branch: str = "main") -> dict:
    """Fetch repository contents from GitHub API"""
    url = f"https://api.github.com/repos/{repo}/contents/{path}?ref={branch}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return None
        else:
            print_error(f"GitHub API error: {response.status_code}")
            return None
    except Exception as e:
        print_error(f"Request failed: {e}")
        return None

def find_skills_in_repo(repo: str, branch: str = "main") -> List[Dict]:
    """Find all skills in a repository"""
    print_info(f"Scanning {Colors.BOLD}{repo}{Colors.END}...")

    skills_found = []
    search_paths = ["skills", ""]

    for search_path in search_paths:
        contents = fetch_github_contents(repo, search_path, branch)
        if not contents or isinstance(contents, dict):
            continue

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

def load_registry(registry_path: Path) -> dict:
    """Load the skills registry"""
    try:
        with open(registry_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print_error("Registry file not found!")
        sys.exit(1)

def save_registry(registry_path: Path, registry: dict):
    """Save the skills registry"""
    with open(registry_path, 'w', encoding='utf-8') as f:
        json.dump(registry, f, indent=2, ensure_ascii=False)

def create_skill_entry(skill: Dict, branch: str = "main") -> Dict:
    """Create a skill entry for the registry"""
    return {
        "name": skill['name'],
        "description": f"Skill from {skill['repo']}",
        "source": {
            "type": "github",
            "repo": skill['repo'],
            "url": f"https://github.com/{skill['repo']}",
            "branch": branch,
            "path": skill['path']
        },
        "metadata": {
            "author": skill['repo'].split('/')[0],
            "license": "Unknown",
            "tags": [],
            "category": "general"
        }
    }

def batch_add_repositories(repos: List[str], branch: str = "main"):
    """Batch add skills from multiple repositories"""
    print_header("🚀 Batch Skills Manager")

    registry_path = Path(__file__).parent.parent / "skills" / "skills-registry.json"
    registry = load_registry(registry_path)

    all_skills = []
    repo_stats = {}

    # Step 1: Scan all repositories
    print_info(f"Scanning {len(repos)} repositories...\n")

    for i, repo in enumerate(repos, 1):
        print(f"[{i}/{len(repos)}] {Colors.BOLD}{repo}{Colors.END}")
        skills = find_skills_in_repo(repo, branch)

        if skills:
            print_success(f"Found {len(skills)} skill(s)")
            all_skills.extend(skills)
            repo_stats[repo] = {'found': len(skills), 'status': 'success'}
        else:
            print_warning("No skills found")
            repo_stats[repo] = {'found': 0, 'status': 'empty'}
        print()

    if not all_skills:
        print_error("No skills found in any repository!")
        return

    # Step 2: Show summary
    print_header("📊 Scan Summary")

    total_found = len(all_skills)
    print(f"Repositories scanned: {len(repos)}")
    print(f"Total skills found: {Colors.GREEN}{Colors.BOLD}{total_found}{Colors.END}")
    print()

    for repo, stats in repo_stats.items():
        if stats['status'] == 'success':
            print(f"  {Colors.GREEN}✅{Colors.END} {repo}: {stats['found']} skills")
        else:
            print(f"  {Colors.YELLOW}⚠️{Colors.END} {repo}: 0 skills")

    # Step 3: Filter existing skills
    print()
    print_header("🔍 Checking for Duplicates")

    new_skills = []
    existing_skills = []

    for skill in all_skills:
        if skill['name'] in registry['skills']:
            existing_skills.append(skill)
        else:
            new_skills.append(skill)

    print(f"New skills: {Colors.GREEN}{len(new_skills)}{Colors.END}")
    print(f"Existing skills: {Colors.YELLOW}{len(existing_skills)}{Colors.END}")

    if existing_skills:
        print()
        print_warning("These skills already exist and will be skipped:")
        for skill in existing_skills[:10]:  # Show first 10
            print(f"  - {skill['name']}")
        if len(existing_skills) > 10:
            print(f"  ... and {len(existing_skills) - 10} more")

    # Step 4: Interactive selection
    if new_skills:
        print()
        print_header(f"📋 New Skills to Add ({len(new_skills)})")

        # Display skills in a nice format
        for i, skill in enumerate(new_skills, 1):
            status = "NEW"
            print(f"{Colors.CYAN}{i:3d}.{Colors.END} {Colors.BOLD}{skill['name']}{Colors.END}")
            print(f"     {Colors.BLUE}Repo:{Colors.END} {skill['repo']}")
            print(f"     {Colors.BLUE}Path:{Colors.END} {skill['path']}")
            print()

        # Ask for confirmation
        print(f"{Colors.YELLOW}Choose an option:{Colors.END}")
        print(f"  {Colors.GREEN}1{Colors.END}. Add all new skills ({len(new_skills)})")
        print(f"  {Colors.GREEN}2{Colors.END}. Select specific skills to add")
        print(f"  {Colors.GREEN}3{Colors.END}. Cancel")

        choice = input(f"\n{Colors.BOLD}Enter choice [1-3]:{Colors.END} ").strip()

        if choice == '1':
            # Add all
            selected = new_skills
        elif choice == '2':
            # Select specific
            print()
            print(f"Enter skill numbers to add (comma-separated, e.g., 1,3,5):")
            print(f"Or enter 'all' to add all, '0' to cancel")

            selection = input(f"{Colors.BOLD}Selection:{Colors.END} ").strip()

            if selection.lower() == 'all':
                selected = new_skills
            elif selection == '0':
                print_info("Cancelled")
                return
            else:
                try:
                    indices = [int(x.strip()) - 1 for x in selection.split(',')]
                    selected = [new_skills[i] for i in indices if 0 <= i < len(new_skills)]
                except:
                    print_error("Invalid selection")
                    return
        else:
            print_info("Cancelled")
            return

        if not selected:
            print_warning("No skills selected")
            return

        # Step 5: Add skills to registry
        print()
        print_header("💾 Adding Skills to Registry")

        added_count = 0
        for skill in selected:
            skill_entry = create_skill_entry(skill, branch)
            registry['skills'][skill['name']] = skill_entry
            added_count += 1
            print_success(f"Added {skill['name']}")

        # Update stats
        registry['last_updated'] = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
        registry['stats']['total_skills'] = len(registry['skills'])

        # Save registry
        save_registry(registry_path, registry)

        print()
        print_success(f"Successfully added {added_count} skill(s)!")
        print()
        print(f"{Colors.BOLD}Next steps:{Colors.END}")
        print(f"  1. {Colors.CYAN}python tools/validate_registry.py{Colors.END}")
        print(f"  2. {Colors.CYAN}python tools/generate_readme.py{Colors.END}")
        print(f"  3. {Colors.CYAN}git add . && git commit -m 'Batch add {added_count} skills'{Colors.END}")
        print(f"  4. {Colors.CYAN}git push{Colors.END}")

def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        # Interactive mode
        print_header("🎯 Batch Skills Manager")
        print(f"{Colors.BOLD}Add multiple skill repositories at once{Colors.END}\n")

        print(f"{Colors.YELLOW}Options:{Colors.END}")
        print(f"  1. Enter repository URLs interactively")
        print(f"  2. Load from file")
        print(f"  3. Use popular repositories")

        choice = input(f"\n{Colors.BOLD}Choose option [1-3]:{Colors.END} ").strip()

        repos = []

        if choice == '1':
            print()
            print_info("Enter repository URLs (one per line, empty line to finish):")
            print_info("Format: owner/repo (e.g., anthropics/skills)")

            while True:
                repo = input(f"{Colors.BOLD}Repo:{Colors.END} ").strip()
                if not repo:
                    break
                repos.append(repo)

        elif choice == '2':
            filename = input(f"\n{Colors.BOLD}Enter filename:{Colors.END} ").strip()
            try:
                with open(filename, 'r') as f:
                    repos = [line.strip() for line in f if line.strip()]
                print_success(f"Loaded {len(repos)} repositories from {filename}")
            except FileNotFoundError:
                print_error(f"File not found: {filename}")
                return

        elif choice == '3':
            repos = [
                "anthropics/skills",
                "obra/superpowers",
                "alirezarezvani/claude-skills",
                "K-Dense-AI/claude-scientific-skills",
                "mrgoonie/claudekit-skills",
                "czlonkowski/n8n-skills",
                "huggingface/skills",
                "bear2u/my-skills",
                "yusufkaraaslan/Skill_Seekers"
            ]
            print_success(f"Selected {len(repos)} popular repositories")

        else:
            print_error("Invalid choice")
            return

        if not repos:
            print_error("No repositories specified")
            return

        batch_add_repositories(repos)

    else:
        # Command line mode
        repos = sys.argv[1:]
        batch_add_repositories(repos)

if __name__ == "__main__":
    main()
