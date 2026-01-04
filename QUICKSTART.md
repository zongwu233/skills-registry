# Skills Registry 快速参考指南

## 🎯 三种添加方式

### 方式 1️⃣：交互式添加（推荐新手）

```bash
cd skills-registry
python tools/add_skill.py
```

按提示输入信息：
- Skill name: `my-awesome-skill`
- Description: `Does amazing things`
- GitHub repo: `username/repo`
- Branch: `main`
- Path: `skills/my-awesome-skill`
- Author: `Your Name`
- License: `MIT`
- Category: `development`
- Tags: `category, tag1, tag2`

然后：
```bash
python tools/validate_registry.py
python tools/generate_readme.py
git add . && git commit -m "Add: my-awesome-skill" && git push
```

---

### 方式 2️⃣：批量导入 GitHub 仓库（推荐快速添加）

```bash
cd skills-registry

# 从整个仓库导入所有 skills
python tools/import_from_repo.py anthropic/skills

# 指定分支
python tools/import_from_repo.py anthropic/skills main

# 从其他仓库导入
python tools/import_from_repo.py obra/superpowers
```

然后编辑描述和元数据：
```bash
vim skills/skills-registry.json
```

然后验证、生成、提交：
```bash
python tools/validate_registry.py
python tools/generate_readme.py
git add . && git commit -m "Import skills from xxx" && git push
```

---

### 方式 3️⃣：手动编辑 JSON（推荐精确控制）

```bash
cd skills-registry
vim skills/skills-registry.json
```

添加技能：
```json
{
  "skills": {
    "my-skill": {
      "name": "my-skill",
      "description": "Clear description",
      "source": {
        "type": "github",
        "repo": "username/repo",
        "url": "https://github.com/username/repo",
        "branch": "main",
        "path": "skills/my-skill"
      },
      "metadata": {
        "author": "Author Name",
        "license": "MIT",
        "tags": ["tag1", "tag2"],
        "category": "development"
      }
    }
  }
}
```

然后：
```bash
python tools/validate_registry.py
python tools/generate_readme.py
git add . && git commit -m "Add: my-skill" && git push
```

---

## 📂 支持的 Category

- `document` - 文档处理
- `development` - 开发工具
- `productivity` - 生产力
- `scientific` - 科学计算
- `creative` - 创意设计
- `automation` - 自动化
- `business` - 商业产品
- `operations` - 运维 DevOps
- `tools` - 工具实用

---

## 🔍 验证和生成

```bash
# 验证 registry 格式
python tools/validate_registry.py

# 生成 README.md
python tools/generate_readme.py

# 查看所有 skills
python -c "import json; print(json.dumps(json.load(open('skills/skills-registry.json'))['skills'].keys(), indent=2))"
```

---

## 🚀 常见场景

### 场景 1：发现一个新的 awesome skills 仓库

```bash
# 快速导入整个仓库
python tools/import_from_repo.py username/awesome-skills

# 编辑描述
vim skills/skills-registry.json

# 验证并提交
python tools/validate_registry.py
python tools/generate_readme.py
git add . && git commit -m "Add awesome-skills repository" && git push
```

### 场景 2：只添加一个特定 skill

```bash
# 交互式添加
python tools/add_skill.py

# 或者手动编辑 JSON
vim skills/skills-registry.json

# 验证并提交
python tools/validate_registry.py
python tools/generate_readme.py
git add . && git commit -m "Add: specific-skill" && git push
```

### 场景 3：更新现有 skill 信息

```bash
# 编辑 JSON
vim skills/skills-registry.json

# 验证并提交
python tools/validate_registry.py
python tools/generate_readme.py
git add . && git commit -m "Update: skill-name" && git push
```

---

## 📦 从 GitHub Actions 自动化

创建 `.github/workflows/auto-import.yml`：

```yaml
name: Auto Import Skills

on:
  workflow_dispatch:
    inputs:
      repo:
        description: 'GitHub repo (owner/repo)'
        required: true
      branch:
        description: 'Branch'
        required: false
        default: 'main'

jobs:
  import:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      - name: Import skills
        run: |
          branch="${{ github.event.inputs.branch }}"
          python tools/import_from_repo.py "${{ github.event.inputs.repo }}" "${branch}"
      - name: Validate
        run: python tools/validate_registry.py
      - name: Generate README
        run: python tools/generate_readme.py
      - name: Create Pull Request
        uses: peter-evans/create-pull-request@v5
        with:
          title: "Import skills from ${{ github.event.inputs.repo }}"
          body: "Automatically imported skills"
          branch: "auto-import-${{ github.event.inputs.repo }}"
```

然后在 GitHub 网页上手动触发，输入仓库地址即可。

---

## 🎓 最佳实践

### ✅ 推荐做法

1. **先验证再提交**：每次编辑后都运行 `validate_registry.py`
2. **使用有意义的描述**：描述要说明技能**何时使用**
3. **正确的分类**：使用合适的 category
4. **丰富的标签**：添加多个相关标签便于搜索
5. **定期更新**：删除失效的技能

### ❌ 避免做法

1. 不要添加重复的技能
2. 不要添加没有 SKILL.md 的"技能"
3. 不要添加私有仓库（除非你自己用）
4. 不要破坏 JSON 格式

---

## 🔗 与 Skills Store 集成

Skills Store 会自动从你的 registry 读取：

```bash
# 在 skills-store 项目中
cd ../skills-store

# 复制 registry
cp ../skills-registry/skills/skills-registry.json data/

# 或者设置远程源
# 编辑 data/skills-registry.json 添加源
```

---

## 📊 统计信息

查看当前统计：

```bash
cd skills-registry

python -c "
import json
with open('skills/skills-registry.json') as f:
    registry = json.load(f)

print(f'Total Skills: {registry[\"stats\"][\"total_skills\"]}')
print(f'Total Sources: {registry[\"stats\"][\"total_sources\"]}')
print(f'Last Updated: {registry[\"last_updated\"]}')

# Count by category
categories = {}
for skill in registry['skills'].values():
    cat = skill['metadata']['category']
    categories[cat] = categories.get(cat, 0) + 1

print('\nBy Category:')
for cat, count in sorted(categories.items(), key=lambda x: x[1], reverse=True):
    print(f'  {cat}: {count}')
"
```

---

## 🆘 故障排查

### Problem: `validate_registry.py` 报错

**Solution**:
```bash
# 检查 JSON 语法
python -m json.tool skills/skills-registry.json

# 查找具体错误
python tools/validate_registry.py 2>&1 | grep "Error"
```

### Problem: GitHub API rate limit

**Solution**:
```bash
# 设置 token
export GITHUB_TOKEN=your_token_here

# 或者在脚本中添加认证
# 修改 import_from_repo.py 添加：
# headers = {'Authorization': f'token {os.environ.get("GITHUB_TOKEN")}'}
```

### Problem: Skill 安装失败

**Solution**:
1. 检查 GitHub 仓库是否公开
2. 检查 path 是否正确
3. 检查 branch 是否存在
4. 检查 SKILL.md 是否存在

---

## 📝 相关文档

- `CONTRIBUTING.md` - 贡献指南
- `DEPLOY.md` - 部署指南
- `README.md` - 自动生成的文档

---

**Happy adding skills! 🚀**
