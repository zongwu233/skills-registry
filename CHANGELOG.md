# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-01-04

### Added
- Initial release of Skills Registry
- **21 skills** from 9 different repositories
- **9 categories**: document, development, scientific, productivity, creative, automation, business, operations, tools
- **6 management tools** for easy skill repository management
  - `batch_add.py` - Interactive batch addition tool
  - `repo_manager.py` - Advanced repository manager
  - `import_from_repo.py` - Quick single repository import
  - `add_skill.py` - Interactive single skill addition
  - `validate_registry.py` - Registry validation tool
  - `generate_readme.py` - README generator
- **Configuration files**
  - `repositories.txt` - Simple text-based repository list
  - `repositories.json` - Advanced configuration with metadata
  - `skills/skills-registry.json` - Main registry database
- **Documentation**
  - Comprehensive README with usage guides
  - BATCH_TOOLS_GUIDE.md - Detailed batch tools documentation
  - QUICKSTART.md - Quick reference guide
  - CONTRIBUTING.md - Contribution guidelines
  - DEPLOY.md - Deployment instructions
  - CHANGELOG.md - Version history

### Features
- **Smart deduplication** - Automatically detects and skips existing skills
- **Interactive selection** - Choose which skills to add
- **Color-coded output** - Beautiful terminal output with emojis
- **Auto-categorization** - Automatically categorize skills based on keywords
- **Cross-platform** - Works on Windows, macOS, and Linux
- **GitHub API integration** - Scan repositories directly from GitHub
- **Validation system** - Ensure registry integrity
- **Batch operations** - Import from multiple repositories at once

### Source Repositories
- anthropics/skills (8 skills)
- obra/superpowers (20+ available)
- alirezarezvani/claude-skills (3 skills)
- K-Dense-AI/claude-scientific-skills (138 available)
- mrgoonie/claudekit-skills (10 available)
- czlonkowski/n8n-skills (5 skills)
- huggingface/skills (5 skills)
- bear2u/my-skills (3 skills)
- yusufkaraaslan/Skill_Seekers (1 skill)

### Documentation
- Quick start guide with 4 different usage options
- Comprehensive tool documentation
- Configuration examples
- Common workflow examples
- Skills Store integration guide

### Statistics
- Total Skills: 21
- Total Repositories: 9
- Total Categories: 9
- Total Tools: 6

---

## [Unreleased]

### Planned
- Automatic registry updates from GitHub
- Web interface for browsing skills
- Skill versioning support
- Dependency management
- Community ratings and reviews
- Skill recommendation engine
- REST API for registry access
