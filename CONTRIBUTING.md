# Contributing to Skills Registry

Thank you for your interest in contributing to the Claude Skills Registry! This document provides guidelines and instructions for contributing.

## Table of Contents

1. [How to Contribute](#how-to-contribute)
2. [Adding a New Skill](#adding-a-new-skill)
3. [Validation](#validation)
4. [Pull Request Process](#pull-request-process)
5. [Code Standards](#code-standards)

## How to Contribute

There are several ways to contribute:

- **Add new skills** to the registry
- **Update existing skill** information
- **Report issues** with current skills
- **Improve documentation** and tools
- **Submit bug fixes** or enhancements

## Adding a New Skill

### 1. Prepare Your Skill

Before adding a skill to the registry, ensure it:

- Has a valid `SKILL.md` file with YAML frontmatter
- Includes required fields: `name` and `description`
- Is publicly accessible (GitHub) or properly documented (local)
- Meets the [validation criteria](tools/validate_registry.py)

### 2. Fork and Clone

```bash
# Fork this repository on GitHub
# Clone your fork
git clone https://github.com/YOUR_USERNAME/skills-registry.git
cd skills-registry
```

### 3. Add Your Skill

Edit `skills/skills-registry.json` and add your skill entry:

```json
{
  "skills": {
    "your-skill-name": {
      "name": "your-skill-name",
      "description": "A clear description of what your skill does",
      "source": {
        "type": "github",
        "repo": "your-username/your-repo",
        "url": "https://github.com/your-username/your-repo",
        "branch": "main",
        "path": "skills/your-skill"
      },
      "metadata": {
        "author": "Your Name",
        "license": "MIT",
        "tags": ["category", "specific-tags"],
        "category": "development"
      }
    }
  }
}
```

### 4. Update Statistics

Update the `stats` section at the end of the file:

```json
{
  "stats": {
    "total_skills": 9,  // Increment this
    "total_sources": 2,  // Increment if new source
    "last_sync": "2026-01-02T16:00:00Z"  // Update timestamp
  }
}
```

### 5. Update Categories (if needed)

If you're adding a new category, add it to the `categories` section:

```json
{
  "categories": {
    "your-new-category": {
      "name": "Your New Category",
      "description": "Description of the category",
      "count": 1
    }
  }
}
```

### 6. Validate

Run the validation script to ensure everything is correct:

```bash
python tools/validate_registry.py
```

Fix any errors before proceeding.

### 7. Generate README

Regenerate the README with your new skill:

```bash
python tools/generate_readme.py
```

### 8. Commit and Push

```bash
git add .
git commit -m "Add: your-skill-name - Description of skill"
git push origin main
```

### 9. Submit Pull Request

Go to your fork on GitHub and submit a pull request with:

- **Title**: Clear description (e.g., "Add: pdf-processing skill")
- **Description**: Details about the skill and what it does
- **Link**: Link to the skill repository or documentation

## Validation

The registry enforces these validation rules:

### Required Fields

Every skill MUST have:
- `name` - Unique identifier (lowercase, hyphens)
- `description` - What the skill does
- `source` - Where to get the skill

### Source Types

**GitHub source** must include:
- `type`: "github"
- `repo`: "owner/repo" format
- `url`: Full GitHub repository URL
- `path`: Path to skill within repository

**Local source** must include:
- `type`: "local"
- `path`: File system path

### Metadata (Optional but Recommended)

- `author` - Skill author name
- `license` - License identifier (SPDX format)
- `tags` - Array of searchable tags
- `category` - One of: document, creative, development, or other

### Naming Conventions

- Skill names should be **lowercase**
- Use **hyphens** to separate words (e.g., `my-awesome-skill`)
- Names should be **descriptive but concise**
- Avoid special characters

## Pull Request Process

### What We Look For

✅ **Good Pull Requests**:
- Follow the schema and validation rules
- Include clear descriptions
- Have properly formatted JSON
- Pass validation tests
- Add value to the community

❌ **What We Avoid**:
- Duplicate skills
- Incomplete information
- Broken or inaccessible sources
- Skills without clear purpose
- Proprietary skills without redistribution rights

### Review Process

1. **Automated Checks**: PR must pass validation
2. **Manual Review**: Maintainers review the skill
3. **Testing**: Skill is tested for accessibility
4. **Merge**: Once approved, PR is merged
5. **README Update**: README is regenerated

### Timeline

- Simple additions: 1-3 days
- Complex skills: 3-7 days
- New categories: Discussion required

## Code Standards

### JSON Formatting

- Use 2-space indentation
- Use double quotes for strings
- Include trailing commas
- Sort skills alphabetically within categories

### Commit Messages

Follow conventional commits format:

```
Add: new-skill - Brief description
Update: existing-skill - What changed
Fix: correct-error-in-skill
Docs: update documentation
```

### Documentation

- Keep skill descriptions **concise but informative**
- Mention **when to use** the skill
- Include **key features** in description
- Use **active voice**

## Questions or Issues?

- **GitHub Issues**: Report bugs or request features
- **Discussions**: Start a discussion for ideas
- **Email**: Contact maintainers for private questions

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Thank You!

We appreciate all contributions to the Claude Skills Registry. Your skills help the entire Claude ecosystem grow! 🎉
