# GitHub 仓库部署指南

本指南将帮助你将 skills-registry 仓库部署到 GitHub。

## 前提条件

- GitHub 账户
- Git 已安装
- 本地仓库已初始化（已完成）

## 步骤 1: 在 GitHub 上创建仓库

### 选项 A: 通过 GitHub 网页创建

1. 访问 https://github.com/new
2. 填写仓库信息：
   - **Repository name**: `skills-registry`
   - **Description**: `A centralized registry of Claude Skills for the Skills Store`
   - **Public/Private**: 选择 Public（推荐）
   - **不要**勾选 "Add a README file"（我们已经有了）
   - **不要**勾选 "Add .gitignore"
   - **不要**勾选 "Choose a license"（我们已经有了）
3. 点击 "Create repository"

### 选项 B: 使用 GitHub CLI

```bash
# 如果安装了 gh CLI
gh repo create skills-registry --public --description "A centralized registry of Claude Skills for the Skills Store"
```

## 步骤 2: 连接本地仓库到 GitHub

### 方法 1: HTTPS（推荐）

```bash
cd skills-registry
git remote add origin https://github.com/YOUR_USERNAME/skills-registry.git
git branch -M main
git push -u origin main
```

### 方法 2: SSH

```bash
cd skills-registry
git remote add origin git@github.com:YOUR_USERNAME/skills-registry.git
git branch -M main
git push -u origin main
```

**注意**: 将 `YOUR_USERNAME` 替换为你的 GitHub 用户名。

## 步骤 3: 验证部署

访问你的 GitHub 仓库：
```
https://github.com/YOUR_USERNAME/skills-registry
```

你应该看到：
- ✅ README.md 显示在主页
- ✅ skills/ 目录包含 skills-registry.json
- ✅ tools/ 目录包含验证和生成工具
- ✅ LICENSE 和 CONTRIBUTING.md 文件

## 步骤 4: 配置仓库（可选）

### 添加 Topics

在仓库页面添加标签以帮助发现：
- `claude-skills`
- `skills-registry`
- `claude`
- `python`
- `skills`

### 启用 GitHub Actions（可选）

创建 `.github/workflows/validate.yml`:

```yaml
name: Validate Registry

on:
  push:
    paths:
      - 'skills/skills-registry.json'
  pull_request:
    paths:
      - 'skills/skills-registry.json'

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      - name: Validate Registry
        run: python tools/validate_registry.py
```

### 添加分支保护（推荐）

1. 进入 Settings → Branches
2. 点击 "Add rule"
3. Branch name pattern: `main`
4. 启用：
   - ✅ Require a pull request before merging
   - ✅ Require status checks to pass before merging
   - ✅ Require branches to be up to date before merging

## 步骤 5: 更新 skills-store 引用

更新 `data/skills-registry.json` 中的默认源：

```json
{
  "sources": [
    {
      "name": "community-skills-registry",
      "type": "github",
      "url": "https://github.com/YOUR_USERNAME/skills-registry",
      "branch": "main",
      "skills_path": "skills"
    }
  ]
}
```

## 步骤 6: 测试安装

从你的新仓库安装一个技能：

```bash
cd ../skills-store
python scripts/install_skill.py pdf
```

## 常见问题

### Q: 推送时出现认证错误

**A**: 使用 GitHub Personal Access Token:
1. Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token (classic)
3. 勾选 `repo` 权限
4. 使用 token 作为密码

### Q: 如何更新索引？

**A**:
1. 编辑 `skills/skills-registry.json`
2. 运行 `python tools/validate_registry.py`
3. 运行 `python tools/generate_readme.py`
4. 提交并推送

### Q: 如何接受社区贡献？

**A**:
1. 仓库设置为 Public
2. 社区成员 Fork 你的仓库
3. 他们提交 Pull Request
4. 你审查并合并 PR

### Q: 如何自动验证 PR？

**A**: 启用 GitHub Actions（见步骤 4）

## 下一步

- 📢 在社区分享你的仓库链接
- 🔗 在 skills-store README 中添加链接
- 📝 添加更多技能到索引
- 👥 邀请其他开发者贡献

## 维护建议

### 定期任务

- **每周**: 检查新的 Pull Requests
- **每月**: 更新统计信息
- **每季度**: 审查和清理失效技能

### 安全检查

- 验证每个技能的源仓库
- 检查技能内容是否安全
- 测试安装过程

## 获取帮助

- GitHub Issues: 报告问题
- Discussions: 社区讨论
- CONTRIBUTING.md: 贡献指南

---

**恭喜！** 🎉 你的 Skills Registry 现在已经在 GitHub 上了！

仓库位置: `https://github.com/YOUR_USERNAME/skills-registry`
