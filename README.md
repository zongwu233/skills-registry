# Claude Skills Registry

A centralized registry of Claude Skills available for installation via Skills Store.

## About

This registry contains a curated list of Claude Skills that can be discovered and installed
using [Skills Store](https://github.com/your-username/skills-store). Each skill entry includes
metadata, source information, and installation details.

## Statistics

- **Total Skills**: 8
- **Total Sources**: 1
- **Last Updated**: 2026-01-02T15:30:00Z

## Quick Links

- [Creative & Design](#creative) (1 skills)
- [Development Tools](#development) (3 skills)
- [Document Processing](#document) (4 skills)

## Skills by Category

### Creative & Design

Skills for creative work and art generation

#### algorithmic-art

**Description**: Creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration. Use this when users request creating art using code, generative art, algorithmic art, flow fields, or particle systems

**Source**: [GitHub](https://github.com/anthropics/anthropic-skills)

**Author**: Anthropic
**License**: Proprietary
**Tags**: `creative, art, generative, p5.js, algorithmic`

**Installation**:

```bash
python scripts/install_skill.py algorithmic-art
```

### Development Tools

Skills for software development and tooling

#### frontend-design

**Description**: Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, artifacts, posters, or applications

**Source**: [GitHub](https://github.com/anthropics/anthropic-skills)

**Author**: Anthropic
**License**: Proprietary
**Tags**: `frontend, web, design, ui, react`

**Installation**:

```bash
python scripts/install_skill.py frontend-design
```

#### mcp-builder

**Description**: Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools

**Source**: [GitHub](https://github.com/anthropics/anthropic-skills)

**Author**: Anthropic
**License**: Proprietary
**Tags**: `development, mcp, server, api`

**Installation**:

```bash
python scripts/install_skill.py mcp-builder
```

#### skill-creator

**Description**: Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Claude's capabilities

**Source**: [GitHub](https://github.com/anthropics/anthropic-skills)

**Author**: Anthropic
**License**: Proprietary
**Tags**: `development, skill, authoring, tools`

**Installation**:

```bash
python scripts/install_skill.py skill-creator
```

### Document Processing

Skills for working with documents (PDF, DOCX, PPTX, XLSX)

#### docx

**Description**: Comprehensive document creation, editing, and analysis with support for tracked changes, comments, formatting preservation, and text extraction

**Source**: [GitHub](https://github.com/anthropics/anthropic-skills)

**Author**: Anthropic
**License**: Proprietary
**Tags**: `document, docx, word, editing`

**Installation**:

```bash
python scripts/install_skill.py docx
```

#### pdf

**Description**: Comprehensive PDF manipulation toolkit for extracting text and tables, creating new PDFs, merging/splitting documents, and filling forms

**Source**: [GitHub](https://github.com/anthropics/anthropic-skills)

**Author**: Anthropic
**License**: Proprietary
**Tags**: `document, pdf, manipulation, forms`

**Installation**:

```bash
python scripts/install_skill.py pdf
```

#### pptx

**Description**: Presentation creation, editing, and analysis. When Claude needs to work with presentations (.pptx files) for creating new presentations, modifying content, working with layouts, or adding comments

**Source**: [GitHub](https://github.com/anthropics/anthropic-skills)

**Author**: Anthropic
**License**: Proprietary
**Tags**: `presentation, pptx, powerpoint, slides`

**Installation**:

```bash
python scripts/install_skill.py pptx
```

#### xlsx

**Description**: Comprehensive spreadsheet creation, editing, and analysis with support for formulas, formatting, data analysis, and visualization

**Source**: [GitHub](https://github.com/anthropics/anthropic-skills)

**Author**: Anthropic
**License**: Proprietary
**Tags**: `spreadsheet, excel, xlsx, data`

**Installation**:

```bash
python scripts/install_skill.py xlsx
```

## Usage

### Prerequisites

1. Install [Skills Store](https://github.com/your-username/skills-store)
2. Ensure you have Python 3.7+ and required dependencies

### Installing a Skill

```bash
# Search for skills
python scripts/search_skills.py "keyword"

# Install a specific skill
python scripts/install_skill.py <skill-name>
```

## Contributing

To add a new skill to the registry:

1. Fork this repository
2. Edit `skills/skills-registry.json`
3. Add your skill following the [schema](docs/SCHEMA.md)
4. Run validation: `python tools/validate_registry.py`
5. Regenerate this README: `python tools/generate_readme.py`
6. Submit a pull request

## Schema Reference

For detailed information about the registry schema, see [SCHEMA.md](docs/SCHEMA.md).

---

**Maintained by**: The Claude Skills Community

*This README is automatically generated from skills-registry.json*

*Generated: 2026-01-02T23:54:45.596126*