# Claude Skills Registry

A centralized registry of Claude Skills available for installation via Skills Store.

## About

This registry contains a curated list of Claude Skills that can be discovered and installed
using [Skills Store](https://github.com/your-username/skills-store). Each skill entry includes
metadata, source information, and installation details.

## Statistics

- **Total Skills**: 17
- **Total Sources**: 5
- **Last Updated**: 2026-01-03T00:00:00Z

## Quick Links

- [Business & Product](#business) (1 skills)
- [Creative & Design](#creative) (2 skills)
- [Development Tools](#development) (3 skills)
- [Document Processing](#document) (4 skills)
- [Operations & DevOps](#operations) (1 skills)
- [Productivity & Workflow](#productivity) (1 skills)
- [Scientific Computing](#science) (3 skills)
- [Security & Testing](#security) (1 skills)
- [Quality Assurance](#testing) (1 skills)

## Skills by Category

### Business & Product

Skills for product management, strategy, and business operations

#### product-management

**Description**: Product management skills for roadmapping, user stories, prioritization frameworks, MVP definition, and product strategy. Bridges technical and business perspectives

**Source**: [GitHub](https://github.com/alirezarezvani/claude-skills)

**Author**: Alireza Rezvani
**License**: MIT
**Tags**: `product, management, strategy, roadmap, agile`

**Installation**:

```bash
python scripts/install_skill.py product-management
```

### Creative & Design

Skills for creative work, art generation, and visualization

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

#### d3js-visualization

**Description**: D3.js data visualization skills for creating interactive charts, graphs, and data-driven visualizations. Covers scales, axes, layouts, and animated transitions

**Source**: [GitHub](https://github.com/topics/claude-skills-hub)

**Author**: Community
**License**: MIT
**Tags**: `visualization, d3js, charts, data-viz`

**Installation**:

```bash
python scripts/install_skill.py d3js-visualization
```

### Development Tools

Skills for software development, architecture, and tooling

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

#### senior-architect

**Description**: Advanced software architecture skills for system design, microservices, event-driven architecture, and technical leadership. Guides through making architectural decisions and evaluating trade-offs

**Source**: [GitHub](https://github.com/alirezarezvani/claude-skills)

**Author**: Alireza Rezvani
**License**: MIT
**Tags**: `architecture, design, leadership, system-design`

**Installation**:

```bash
python scripts/install_skill.py senior-architect
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

### Operations & DevOps

Skills for DevOps, CI/CD, infrastructure, and deployment

#### devops-engineer

**Description**: DevOps engineering skills for CI/CD pipelines, infrastructure as code, container orchestration, monitoring, and deployment automation. Covers Docker, Kubernetes, and cloud platforms

**Source**: [GitHub](https://github.com/alirezarezvani/claude-skills)

**Author**: Alireza Rezvani
**License**: MIT
**Tags**: `devops, cicd, docker, kubernetes, automation`

**Installation**:

```bash
python scripts/install_skill.py devops-engineer
```

### Productivity & Workflow

Skills for improving productivity, TDD, debugging, and collaboration

#### superpowers

**Description**: Core skills library for Claude Code with 20+ battle-tested skills including TDD, debugging, and collaboration patterns. Provides brainstorming, planning, and execution commands

**Source**: [GitHub](https://github.com/obra/superpowers)

**Author**: Jesse Vincent
**License**: MIT
**Tags**: `productivity, tdd, debugging, collaboration, workflow`

**Installation**:

```bash
python scripts/install_skill.py superpowers
```

### Scientific Computing

Skills for bioinformatics, cheminformatics, data analysis, and research

#### bioinformatics

**Description**: Comprehensive bioinformatics skills for genomic data analysis, sequence alignment, phylogenetic analysis, and working with biological databases like GenBank and UniProt

**Source**: [GitHub](https://github.com/K-Dense-AI/claude-scientific-skills)

**Author**: K-Dense Team
**License**: MIT
**Tags**: `bioinformatics, genomics, sequence-analysis, biology`

**Installation**:

```bash
python scripts/install_skill.py bioinformatics
```

#### cheminformatics

**Description**: Cheminformatics skills for molecular analysis, drug discovery, chemical database queries, and molecular property prediction using RDKit and computational chemistry tools

**Source**: [GitHub](https://github.com/K-Dense-AI/claude-scientific-skills)

**Author**: K-Dense Team
**License**: MIT
**Tags**: `chemistry, drug-discovery, molecular, rdkit`

**Installation**:

```bash
python scripts/install_skill.py cheminformatics
```

#### data-analysis

**Description**: Scientific data analysis skills covering statistical methods, data visualization with matplotlib/seaborn, hypothesis testing, and exploratory data analysis

**Source**: [GitHub](https://github.com/K-Dense-AI/claude-scientific-skills)

**Author**: K-Dense Team
**License**: MIT
**Tags**: `data-science, statistics, visualization, analysis`

**Installation**:

```bash
python scripts/install_skill.py data-analysis
```

### Security & Testing

Skills for security testing, penetration testing, and vulnerability assessment

#### security-testing

**Description**: Security testing skills for penetration testing, vulnerability assessment, security auditing, and using tools like ffuf for web fuzzing and automated security scanning

**Source**: [GitHub](https://github.com/topics/claude-skills-hub)

**Author**: Community
**License**: MIT
**Tags**: `security, penetration-testing, vulnerability, ffuf`

**Installation**:

```bash
python scripts/install_skill.py security-testing
```

### Quality Assurance

Skills for testing, automation, and quality assurance

#### browser-automation

**Description**: Browser automation skills using Playwright for web testing, scraping, form filling, and browser interactions. Covers page navigation, element selection, and test automation

**Source**: [GitHub](https://github.com/topics/claude-skills-hub)

**Author**: Community
**License**: MIT
**Tags**: `testing, automation, browser, playwright`

**Installation**:

```bash
python scripts/install_skill.py browser-automation
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

*Generated: 2026-01-03T00:03:01.194487*