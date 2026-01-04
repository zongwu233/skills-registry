# Claude Skills Registry

> 📦 Centralized registry for discovering and managing Claude Skills

A centralized registry of Claude Skills available for installation via [Skills Store](https://github.com/zongwu233/skills-store). This registry provides tools and utilities for easily managing and importing skills from multiple GitHub repositories.

---

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- Git
- [Skills Store](https://github.com/zongwu233/skills-store) installed (optional)

### Option 1: Interactive Batch Import (Recommended)

The easiest way to add skills from multiple repositories:

```bash
cd skills-registry

# Launch interactive batch tool
python tools/batch_add.py

# Choose from:
# 1. Enter repositories interactively
# 2. Load from file
# 3. Use popular repositories

# Follow the prompts to select skills to add
# Tools will automatically add them to the registry
```

### Option 2: Repository Manager (For Long-term Maintenance)

Advanced tool for managing multiple repositories with configuration:

```bash
# Initialize repository manager
python tools/repo_manager.py

# Choose from:
# 1. List repositories    - View configured repositories
# 2. Add repository       - Add new repository to monitor
# 3. Scan and import      - Scan all enabled repos and add skills
# 4. Toggle repository    - Enable/disable repositories

# Use command-line mode
python tools/repo_manager.py list
python tools/repo_manager.py scan
```

### Option 3: Quick Single Repository Import

Import skills from a single repository quickly:

```bash
python tools/import_from_repo.py anthropics/skills
python tools/import_from_repo.py obra/superpowers
```

### Option 4: Manual Entry

Add skills manually by editing the registry:

```bash
# Edit registry file
vim skills/skills-registry.json

# Validate changes
python tools/validate_registry.py

# Regenerate README (optional)
python tools/generate_readme.py
```

---

## 📊 Current Statistics

| Metric | Count |
|--------|-------|
| **Total Skills** | 21 |
| **Repositories** | 9 |
| **Categories** | 9 |

### Categories

- 📄 Document Processing (4)
- 💻 Development Tools (4)
- 🔬 Scientific Computing (5)
- ⚡ Productivity (3)
- 🎨 Creative & Design (1)
- 🤖 Automation (1)
- 💼 Business (1)
- 🔧 Operations (1)
- 🛠️ Tools (1)

### Source Repositories

- **anthropics/skills** - Official Anthropic skills
- **obra/superpowers** - Core productivity skills (20+)
- **alirezarezvani/claude-skills** - Architecture, Product, DevOps
- **K-Dense-AI/claude-scientific-skills** - Scientific computing (138)
- **mrgoonie/claudekit-skills** - Agent and reasoning skills
- **czlonkowski/n8n-skills** - Workflow automation
- **huggingface/skills** - Machine learning skills
- **bear2u/my-skills** - Common utilities
- **yusufkaraaslan/Skill_Seekers** - Documentation converter

---

## 🛠️ Available Tools

### 1. batch_add.py - Interactive Batch Tool

**Best for**: One-time bulk imports from multiple repositories

```bash
python tools/batch_add.py

# Features:
- Colorful terminal output
- Interactive skill selection
- Smart duplicate detection
- Multiple input modes
- Real-time progress
```

**Usage Examples**:
```bash
# Interactive mode
python tools/batch_add.py

# Command-line mode
python tools/batch_add.py anthropics/skills obra/superpowers

# From file
python tools/batch_add.py < repositories.txt
```

### 2. repo_manager.py - Repository Manager

**Best for**: Long-term maintenance and regular updates

```bash
python tools/repo_manager.py

# Features:
- Configuration-based (repositories.json)
- Enable/disable repositories
- Priority-based ordering
- Auto-categorization
- Interactive and CLI modes
```

**Commands**:
```bash
python tools/repo_manager.py list    # List all repos
python tools/repo_manager.py add     # Add new repo
python tools/repo_manager.py scan    # Scan and import
python tools/repo_manager.py toggle  # Enable/disable
```

### 3. import_from_repo.py - Quick Import

**Best for**: Fast single repository imports

```bash
python tools/import_from_repo.py owner/repo [branch]

# Features:
- Simple one-line command
- Fast scanning
- Preview before import
- Script-friendly
```

### 4. add_skill.py - Interactive Single Skill

**Best for**: Adding individual skills with full control

```bash
python tools/add_skill.py

# Features:
- Prompts for all required info
- Validates input
- Updates registry automatically
```

### 5. validate_registry.py - Validation Tool

Validate the registry file format and content:

```bash
python tools/validate_registry.py

# Checks:
- JSON syntax
- Required fields
- Valid sources
- Proper formatting
```

### 6. generate_readme.py - README Generator

Regenerate this README from registry data:

```bash
python tools/generate_readme.py

# Updates:
- Statistics
- Category listings
- Skill descriptions
```

---

## 📖 Configuration Files

### repositories.txt

Simple text file for quick repository lists:

```
# Comments start with #

anthropics/skills
obra/superpowers
username/your-repo
```

### repositories.json

Advanced configuration with metadata:

```json
{
  "repositories": [
    {
      "name": "Anthropic Skills",
      "repo": "anthropics/skills",
      "branch": "main",
      "enabled": true,
      "priority": 1,
      "description": "Official skills"
    }
  ],
  "categories": {
    "development": {
      "keywords": ["code", "api"],
      "default_category": "development"
    }
  }
}
```

---

## 🎯 Common Workflows

### Workflow 1: Initial Setup

```bash
# 1. Import from popular repositories
python tools/batch_add.py

# 2. Validate
python tools/validate_registry.py

# 3. Generate README
python tools/generate_readme.py

# 4. Commit
git add .
git commit -m "Initial import: Add 21 skills from 9 repositories"
git push
```

### Workflow 2: Regular Updates

```bash
# 1. Scan for new skills
python tools/repo_manager.py scan

# 2. Review and edit descriptions
vim skills/skills-registry.json

# 3. Validate and generate
python tools/validate_registry.py
python tools/generate_readme.py

# 4. Commit
git add .
git commit -m "feat: Weekly scan update"
git push
```

### Workflow 3: Add New Repository

```bash
# 1. Quick import
python tools/import_from_repo.py username/new-repo

# 2. Edit metadata
vim skills/skills-registry.json

# 3. Validate
python tools/validate_registry.py

# 4. Commit
git add skills/skills-registry.json
git commit -m "Add: username/new-repo"
git push
```

---

## 🔍 Using with Skills Store

### Method 1: Copy Registry File

```bash
cd skills-store

# Copy registry
cp ../skills-registry/skills/skills-registry.json data/

# Use skills store commands
/skills list-all
/skills install pdf
```

### Method 2: Configure Remote Source

Edit `data/skills-registry.json` in Skills Store:

```json
{
  "sources": [
    {
      "name": "skills-registry",
      "type": "github",
      "url": "https://github.com/zongwu233/skills-registry",
      "branch": "main",
      "skills_path": "skills"
    }
  ]
}
```

---

## 🤝 Contributing

### Adding New Skills

1. Fork this repository
2. Add skills using any of the tools above
3. Edit `skills/skills-registry.json` to add descriptions
4. Run validation: `python tools/validate_registry.py`
5. Regenerate README: `python tools/generate_readme.py`
6. Submit a pull request

### Adding New Repositories

```bash
# Option 1: Use repo manager
python tools/repo_manager.py
# Choose: 2. Add repository

# Option 2: Edit config file
vim repositories.json

# Option 3: Quick import
python tools/import_from_repo.py username/repo
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## 📚 Documentation

- **[BATCH_TOOLS_GUIDE.md](BATCH_TOOLS_GUIDE.md)** - Comprehensive batch tools guide
- **[QUICKSTART.md](QUICKSTART.md)** - Quick reference for all operations
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - Contribution guidelines
- **[DEPLOY.md](DEPLOY.md)** - Deployment instructions

---

## 📦 Project Structure

```
skills-registry/
├── skills/
│   └── skills-registry.json     # Main registry file
├── tools/
│   ├── batch_add.py            # Interactive batch tool
│   ├── repo_manager.py         # Repository manager
│   ├── import_from_repo.py     # Quick single import
│   ├── add_skill.py            # Interactive single skill
│   ├── validate_registry.py   # Validator
│   └── generate_readme.py      # README generator
├── repositories.txt            # Simple repo list
├── repositories.json           # Advanced config
├── BATCH_TOOLS_GUIDE.md        # Tools guide
├── QUICKSTART.md               # Quick reference
├── CONTRIBUTING.md             # Contribution guide
└── README.md                   # This file
```

---

## 🔗 Links

- [Skills Store](https://github.com/zongwu233/skills-store) - Package manager
- [GitHub Repository](https://github.com/zongwu233/skills-registry) - This repo
- [Issues](https://github.com/zongwu233/skills-registry/issues) - Bug reports
- [Discussions](https://github.com/zongwu233/skills-registry/discussions) - Discussions

---

## 📊 License

MIT License - See [LICENSE](LICENSE) file for details

---

**Last Updated**: 2026-01-04 | **Version**: 1.0.0

*Maintained by the Claude Skills Community*
