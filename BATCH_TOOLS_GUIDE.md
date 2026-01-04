# 批量工具使用指南

## 🎯 三种批量添加工具

### 1️⃣ batch_add.py - 友好的交互式批量添加

最友好的批量添加工具，带彩色输出和交互式选择。

#### 使用方式

**方式 A: 交互式模式（推荐）**

```bash
cd skills-registry
python tools/batch_add.py
```

会显示菜单：
```
🎯 Batch Skills Manager
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Options:
  1. Enter repository URLs interactively
  2. Load from file
  3. Use popular repositories

Choose option [1-3]:
```

**方式 B: 命令行模式**

```bash
# 直接指定仓库列表
python tools/batch_add.py anthropics/skills obra/superpowers

# 或使用文件列表
python tools/batch_add.py $(cat repositories.txt | grep -v '^#')
```

**方式 C: 从文件加载**

创建 `my_repos.txt`:
```
# My favorite skills repositories
anthropics/skills
obra/superpowers
username/awesome-skills
```

然后运行：
```bash
python tools/batch_add.py < my_repos.txt
```

#### 特点

✅ **彩色输出** - 清晰的视觉反馈
✅ **智能去重** - 自动跳过已存在的技能
✅ **交互式选择** - 选择要添加哪些技能
✅ **实时统计** - 显示扫描进度和结果
✅ **下一步指引** - 提示后续操作

#### 工作流程

1. **扫描阶段** - 扫描所有仓库
2. **汇总阶段** - 显示找到的所有技能
3. **去重阶段** - 标记已存在的技能
4. **选择阶段** - 交互式选择要添加的技能
5. **添加阶段** - 批量添加到 registry
6. **完成** - 提示后续步骤

---

### 2️⃣ repo_manager.py - 高级仓库管理器

基于配置文件的高级管理工具，支持启用/禁用仓库。

#### 初始化配置

首次使用会自动创建 `repositories.json`:
```bash
python tools/repo_manager.py
```

配置文件格式：
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
      "keywords": ["code", "api", "dev"],
      "default_category": "development"
    }
  }
}
```

#### 命令

**交互式模式**:
```bash
python tools/repo_manager.py
```

菜单：
```
1. List repositories    - 列出所有仓库
2. Add repository       - 添加新仓库
3. Scan and import      - 扫描并导入
4. Toggle repository    - 启用/禁用仓库
5. Exit
```

**命令行模式**:
```bash
python tools/repo_manager.py list     # 列出所有仓库
python tools/repo_manager.py add      # 添加新仓库
python tools/repo_manager.py scan     # 扫描并导入
python tools/repo_manager.py toggle   # 切换仓库状态
```

#### 特点

✅ **配置文件管理** - 持久化仓库列表
✅ **启用/禁用** - 控制哪些仓库参与扫描
✅ **优先级排序** - 按优先级扫描仓库
✅ **自动分类** - 根据关键词自动分类技能
✅ **增量更新** - 只添加新技能，跳过已存在的

#### 工作流程

1. **配置仓库** - 添加要监控的仓库
2. **启用/禁用** - 选择要扫描的仓库
3. **扫描** - 自动扫描所有启用的仓库
4. **导入** - 批量导入新技能
5. **更新** - 定期运行扫描获取更新

---

### 3️⃣ import_from_repo.py - 快速单个仓库导入

最简单的方式，快速导入单个仓库的所有技能。

#### 使用

```bash
# 基本用法
python tools/import_from_repo.py anthropics/skills

# 指定分支
python tools/import_from_repo.py anthropic/skills main

# 批量导入多个
for repo in anthropics/skills obra/superpowers; do
    python tools/import_from_repo.py $repo
done
```

#### 特点

✅ **最简单** - 一行命令完成
✅ **快速** - 直接导入，无需配置
✅ **脚本友好** - 易于在脚本中使用
✅ **预览模式** - 导入前预览

---

## 📊 工具对比

| 特性 | batch_add.py | repo_manager.py | import_from_repo.py |
|------|-------------|-----------------|---------------------|
| **易用性** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **功能** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **配置** | 无需配置 | 需配置文件 | 无需配置 |
| **交互性** | 高 | 中 | 低 |
| **批量处理** | ✅ | ✅ | ⚠️ (需循环) |
| **启用/禁用** | ❌ | ✅ | ❌ |
| **自动分类** | ❌ | ✅ | ❌ |
| **彩色输出** | ✅ | ✅ | ✅ |
| **适用场景** | 一次性批量导入 | 长期维护管理 | 快速导入单个仓库 |

---

## 🎓 使用场景

### 场景 1: 首次设置，导入多个热门仓库

**推荐**: `batch_add.py` (选择选项 3)

```bash
cd skills-registry
python tools/batch_add.py

# 选择: 3. Use popular repositories
# 选择: 1. Add all new skills
```

### 场景 2: 发现一个新仓库，想快速导入

**推荐**: `import_from_repo.py`

```bash
python tools/import_from_repo.py username/new-repo

# 编辑添加描述
vim skills/skills-registry.json

# 验证和生成
python tools/validate_registry.py
python tools/generate_readme.py
git add . && git commit -m "Add new-repo" && git push
```

### 场景 3: 长期维护，定期更新

**推荐**: `repo_manager.py`

```bash
# 1. 初始化配置
python tools/repo_manager.py

# 2. 添加新仓库
# 选择: 2. Add repository

# 3. 扫描更新
# 选择: 3. Scan and import

# 4. 定期运行（每周/每月）
python tools/repo_manager.py scan
```

### 场景 4: 从自定义列表批量导入

**推荐**: `batch_add.py` + 文件

```bash
# 创建列表
cat > my_repos.txt << EOF
anthropics/skills
obra/superpowers
username/custom-repo
EOF

# 批量导入
python tools/batch_add.py < my_repos.txt

# 或者选择选项 2
python tools/batch_add.py
# 选择: 2. Load from file
# 输入: my_repos.txt
```

### 场景 5: 只导入特定仓库

**推荐**: `repo_manager.py` (启用/禁用功能)

```bash
python tools/repo_manager.py

# 1. 列出所有仓库
# 选择: 1. List repositories

# 2. 禁用不需要的
# 选择: 4. Toggle repository

# 3. 扫描
# 选择: 3. Scan and import
```

---

## 🚀 完整工作流示例

### 示例 1: 从零开始建立 registry

```bash
# 1. 克隆/进入 registry
cd skills-registry

# 2. 批量导入热门仓库
python tools/batch_add.py
# 选择: 3 (热门仓库)
# 选择: 1 (添加全部)

# 3. 验证
python tools/validate_registry.py

# 4. 生成文档
python tools/generate_readme.py

# 5. 提交
git add .
git commit -m "Initial: Add 21 skills from 9 repositories"
git push
```

### 示例 2: 日常维护流程

```bash
# 1. 初始化仓库管理器（首次）
python tools/repo_manager.py
# 选择: 2 (添加新发现的仓库)

# 2. 定期扫描更新
python tools/repo_manager.py scan

# 3. 验证和生成
python tools/validate_registry.py
python tools/generate_readme.py

# 4. 提交
git add .
git commit -m "feat: Add new skills from weekly scan"
git push
```

### 示例 3: 紧急添加单个技能

```bash
# 快速导入
python tools/import_from_repo.py username/urgent-skill

# 编辑描述
vim skills/skills-registry.json

# 快速验证和提交
python tools/validate_registry.py
git add skills/skills-registry.json
git commit -m "fix: Add urgent skill"
git push
```

---

## 💡 最佳实践

### ✅ 推荐做法

1. **使用 repo_manager.py 进行长期维护**
   - 配置一次，持续使用
   - 便于控制哪些仓库参与扫描

2. **定期扫描更新**
   ```bash
   # 每周运行一次
   python tools/repo_manager.py scan
   ```

3. **批量导入后检查**
   ```bash
   python tools/validate_registry.py
   python tools/generate_readme.py
   ```

4. **分类管理**
   - 在 `repositories.json` 中配置分类规则
   - 自动分类更准确

### ❌ 避免做法

1. **不要重复导入** - 工具会自动去重，但最好先检查
2. **不要跳过验证** - 始终运行 `validate_registry.py`
3. **不要忘记生成 README** - 保持文档同步

---

## 🔧 故障排查

### Problem: GitHub API rate limit

**Solution**:
```bash
# 设置环境变量
export GITHUB_TOKEN=your_token_here

# 或在工具中添加认证（需要修改代码）
```

### Problem: 找不到 SKILL.md

**Solution**:
- 检查仓库结构
- 确认 SKILL.md 文件名大小写正确
- 确认路径正确

### Problem: 导入失败

**Solution**:
```bash
# 检查网络连接
ping github.com

# 检查仓库是否存在
curl https://api.github.com/repos/owner/repo

# 查看详细错误
python tools/batch_add.py 2>&1 | tee import.log
```

---

## 📝 配置文件参考

### repositories.txt (简单列表)

```
# 注释行会被忽略

# 官方仓库
anthropics/skills

# 社区仓库
obra/superpowers
alirezarezvani/claude-skills

# 你的仓库
username/your-repo
```

### repositories.json (高级配置)

```json
{
  "version": "1.0",
  "repositories": [
    {
      "name": "Display Name",
      "repo": "owner/repo",
      "branch": "main",
      "enabled": true,
      "priority": 1,
      "description": "Description"
    }
  ],
  "categories": {
    "category-name": {
      "keywords": ["keyword1", "keyword2"],
      "default_category": "category-name"
    }
  }
}
```

---

## 🎉 总结

选择合适的工具：

- **新手** / **一次性导入**: `batch_add.py`
- **长期维护**: `repo_manager.py`
- **快速导入单个**: `import_from_repo.py`

开始使用：
```bash
cd skills-registry
python tools/batch_add.py
```

祝你使用愉快！🚀
