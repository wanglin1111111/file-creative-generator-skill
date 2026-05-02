# 系统文件创意生成技能

> 一款基于人工智能的系统文件智能生成工具，助力开发者快速创建高质量的项目文档和配置文件。

## 项目概述

### 功能介绍

系统文件创意生成技能是一款智能化的文件生成工具，具备以下核心功能：

- **智能模板匹配**：根据项目类型自动匹配最佳模板
- **多格式支持**：支持 Markdown、JSON、XML、YAML 等多种文件格式
- **上下文感知**：理解项目结构和已有文件，生成风格一致的内容
- **自定义规则**：支持用户自定义生成规则和模板
- **批量生成**：支持一次性生成多个相关文件

### 应用场景

| 场景 | 描述 |
|------|------|
| **新项目初始化** | 快速生成项目基础结构和配置文件 |
| **文档编写** | 自动生成 API 文档、README、CHANGELOG 等 |
| **配置管理** | 生成各类配置文件（.gitignore、Dockerfile、CI配置等） |
| **代码注释** | 为代码自动生成规范的注释文档 |

## 技术架构与实现原理

### 架构设计

```
┌─────────────────────────────────────────────────────────────┐
│                     应用层 (Application)                     │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐ │
│  │ Web UI      │  │ CLI 工具    │  │ API 服务           │ │
│  └──────┬──────┘  └──────┬──────┘  └──────────┬──────────┘ │
└─────────┼────────────────┼─────────────────────┼───────────┘
          │                │                     │
┌─────────▼────────────────▼─────────────────────▼───────────┐
│                     业务层 (Service)                         │
│  ┌──────────────────┐  ┌──────────────────┐                 │
│  │ 文件生成服务      │  │ 模板管理服务    │                 │
│  │ FileGenerator    │  │ TemplateManager  │                 │
│  └──────────┬───────┘  └──────────┬───────┘                 │
└─────────────┼──────────────────────┼───────────────────────┘
              │                      │
┌─────────────▼──────────────────────▼───────────────────────┐
│                     核心层 (Core)                            │
│  ┌──────────────────────────────────────────────────────┐   │
│  │           AI 驱动的内容生成引擎                        │   │
│  │  - 上下文分析模块    - 模板匹配算法                    │   │
│  │  - 内容生成模块      - 格式转换模块                    │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

### 核心技术栈

| 分类 | 技术 | 版本 |
|------|------|------|
| 语言 | Python | 3.10+ |
| 框架 | FastAPI | 0.100+ |
| AI 接口 | OpenAI API / Claude API | - |
| 数据库 | SQLite | 3.30+ |
| 文档处理 | Jinja2 | 3.1+ |

### 实现原理

1. **上下文分析**：扫描项目目录结构，提取关键信息（语言、框架、依赖等）
2. **模板匹配**：基于机器学习算法匹配最适合的模板
3. **内容生成**：调用 AI 模型生成符合风格的内容
4. **格式转换**：将生成内容转换为目标格式并保存

## 环境要求与安装步骤

### 环境要求

- Python 3.10 或更高版本
- Node.js 16+（可选，用于 Web UI）
- 至少 4GB 内存
- 网络连接（用于调用 AI API）

### 安装步骤

#### 方式一：使用 pip 安装

```bash
# 安装依赖
pip install -r requirements.txt

# 安装技能包
pip install .
```

#### 方式二：本地开发模式

```bash
# 克隆项目
git clone https://github.com/your-username/system-file-creative-generator-skill.git
cd system-file-creative-generator-skill

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# 安装依赖
pip install -r requirements.txt
pip install -e .
```

#### 方式三：Docker 部署

```bash
# 构建镜像
docker build -t file-generator-skill .

# 运行容器
docker run -p 8000:8000 -v $(pwd)/data:/app/data file-generator-skill
```

### 配置说明

创建 `.env` 文件并配置以下环境变量：

```env
# AI 服务配置
OPENAI_API_KEY=your_openai_api_key
CLAUDE_API_KEY=your_claude_api_key

# 服务配置
PORT=8000
DEBUG=false

# 数据库配置
DATABASE_URL=sqlite:///./data/example_db.sqlite
```

## 使用指南

### 基础使用

#### CLI 命令

```bash
# 生成 README 文件
filegen generate --type readme --output ./README.md

# 根据目录结构生成多个文件
filegen generate-all --dir ./my-project

# 预览生成内容
filegen preview --type changelog

# 列出可用模板
filegen templates list
```

#### Python API

```python
from file_generator import FileGenerator

# 初始化生成器
generator = FileGenerator()

# 生成 README
readme_content = generator.generate(
    template_type='readme',
    project_name='My Awesome Project',
    description='A fantastic project description',
    features=['Feature 1', 'Feature 2']
)

# 保存文件
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme_content)
```

### 使用示例

#### 示例 1：生成项目 README

```bash
# 交互式生成
filegen generate readme
```

输出示例：

```markdown
# My Project

> 一个简洁的项目描述

## 功能特性

- 特性一
- 特性二
- 特性三

## 安装指南

```bash
npm install my-project
```

## 使用方法

```javascript
import myProject from 'my-project';
```

## 许可证

MIT
```

#### 示例 2：批量生成配置文件

```bash
# 为 Python 项目生成全套配置文件
filegen generate-all --preset python
```

生成的文件列表：
- `.gitignore`
- `README.md`
- `setup.py`
- `requirements.txt`
- `Dockerfile`
- `.github/workflows/test.yml`

#### 示例 3：自定义模板

```python
from file_generator import FileGenerator, CustomTemplate

# 创建自定义模板
custom_template = CustomTemplate(
    name='custom_license',
    content='Copyright {{ year }} {{ author }}. All rights reserved.',
    variables=['year', 'author']
)

# 使用自定义模板生成
generator = FileGenerator()
result = generator.generate_from_template(
    custom_template,
    year='2024',
    author='John Doe'
)
```

## API 接口说明

### 接口列表

| 方法 | 路径 | 描述 |
|------|------|------|
| GET | `/api/templates` | 获取所有可用模板列表 |
| POST | `/api/generate` | 生成单个文件 |
| POST | `/api/generate/batch` | 批量生成文件 |
| POST | `/api/templates/custom` | 添加自定义模板 |
| DELETE | `/api/templates/{id}` | 删除模板 |

### 接口详情

#### 1. 获取模板列表

**请求**：
```
GET /api/templates
```

**响应**：
```json
{
  "templates": [
    {
      "id": "readme",
      "name": "README 模板",
      "description": "生成项目 README 文件",
      "categories": ["文档", "基础"],
      "variables": ["project_name", "description", "features"]
    }
  ]
}
```

#### 2. 生成文件

**请求**：
```
POST /api/generate
Content-Type: application/json

{
  "template_type": "readme",
  "output_path": "./README.md",
  "parameters": {
    "project_name": "My Project",
    "description": "一个测试项目",
    "features": ["功能A", "功能B"]
  }
}
```

**响应**：
```json
{
  "success": true,
  "message": "文件生成成功",
  "output_path": "./README.md",
  "content": "# My Project\n\n> 一个测试项目\n..."
}
```

#### 3. 批量生成

**请求**：
```
POST /api/generate/batch
Content-Type: application/json

{
  "preset": "python",
  "output_dir": "./my-project",
  "parameters": {
    "project_name": "My Python Project",
    "author": "John Doe"
  }
}
```

**响应**：
```json
{
  "success": true,
  "files_generated": [
    "./my-project/README.md",
    "./my-project/setup.py",
    "./my-project/.gitignore"
  ]
}
```

### 错误响应格式

```json
{
  "success": false,
  "error": "TemplateNotFound",
  "message": "未找到指定的模板类型"
}
```

## 贡献指南

欢迎贡献代码！请遵循以下流程：

### 贡献步骤

1. **Fork 项目**：点击 GitHub 页面上的 Fork 按钮
2. **克隆仓库**：
   ```bash
   git clone https://github.com/your-username/system-file-creative-generator-skill.git
   ```
3. **创建分支**：
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **提交修改**：
   ```bash
   git add .
   git commit -m "feat: 添加新功能描述"
   ```
5. **推送分支**：
   ```bash
   git push origin feature/your-feature-name
   ```
6. **创建 Pull Request**：在 GitHub 上创建 PR

### 代码规范

- 遵循 PEP 8 代码风格
- 使用 `black` 进行代码格式化
- 添加必要的单元测试
- 更新相关文档

### 开发命令

```bash
# 运行测试
pytest tests/

# 代码格式化
black src/

# 代码检查
flake8 src/

# 生成文档
sphinx-build docs/ docs/_build
```

## 许可证

本项目采用 **MIT License** 许可证，详见 [LICENSE](LICENSE) 文件。

## 联系方式

- **项目主页**：[https://github.com/your-username/system-file-creative-generator-skill](https://github.com/your-username/system-file-creative-generator-skill)
- **问题反馈**：[GitHub Issues](https://github.com/your-username/system-file-creative-generator-skill/issues)
- **邮件联系**：support@example.com

## 致谢

感谢以下项目和工具对本项目的支持：

- [FastAPI](https://fastapi.tiangolo.com/) - 高性能 API 框架
- [OpenAI](https://openai.com/) - AI 能力支持
- [Jinja2](https://jinja.palletsprojects.com/) - 模板引擎
- [SQLAlchemy](https://www.sqlalchemy.org/) - 数据库 ORM

---

**版权所有 2024 System File Creative Generator Skill**
