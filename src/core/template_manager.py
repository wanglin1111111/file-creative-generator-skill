import os
import json
from typing import List, Dict

class TemplateManager:
    def __init__(self):
        self.templates_dir = "templates"
        self.custom_templates = {}
        self._load_custom_templates()
    
    def list_templates(self) -> List[Dict]:
        templates = []
        
        built_in_templates = [
            {"id": "readme", "name": "README 模板", "description": "生成项目 README 文件", "categories": ["文档", "基础"]},
            {"id": "gitignore_python", "name": "Python .gitignore", "description": "Python 项目的 .gitignore 文件", "categories": ["配置", "Python"]},
            {"id": "gitignore_js", "name": "JavaScript .gitignore", "description": "JavaScript 项目的 .gitignore 文件", "categories": ["配置", "JavaScript"]},
            {"id": "gitignore_rust", "name": "Rust .gitignore", "description": "Rust 项目的 .gitignore 文件", "categories": ["配置", "Rust"]},
            {"id": "setup_py", "name": "setup.py", "description": "Python 项目的 setup.py 文件", "categories": ["配置", "Python"]},
            {"id": "requirements", "name": "requirements.txt", "description": "Python 依赖列表", "categories": ["配置", "Python"]},
            {"id": "package_json", "name": "package.json", "description": "Node.js 项目配置文件", "categories": ["配置", "JavaScript"]},
            {"id": "babel_config", "name": ".babelrc", "description": "Babel 配置文件", "categories": ["配置", "JavaScript"]},
            {"id": "cargo_toml", "name": "Cargo.toml", "description": "Rust 项目配置文件", "categories": ["配置", "Rust"]}
        ]
        
        templates.extend(built_in_templates)
        
        for name, template in self.custom_templates.items():
            templates.append({
                "id": name,
                "name": template.get("name", name),
                "description": template.get("description", "自定义模板"),
                "categories": ["自定义"]
            })
        
        return templates
    
    def add_template(self, name: str, content: str, variables: List[str] = []):
        self.custom_templates[name] = {
            "name": name,
            "content": content,
            "variables": variables
        }
        self._save_custom_templates()
    
    def delete_template(self, name: str):
        if name in self.custom_templates:
            del self.custom_templates[name]
            self._save_custom_templates()
        else:
            raise ValueError(f"模板 {name} 不存在")
    
    def get_template(self, name: str) -> str:
        if name in self.custom_templates:
            return self.custom_templates[name]["content"]
        
        template_path = os.path.join(self.templates_dir, f"{name}.j2")
        if os.path.exists(template_path):
            with open(template_path, "r", encoding="utf-8") as f:
                return f.read()
        
        raise ValueError(f"模板 {name} 不存在")
    
    def _load_custom_templates(self):
        try:
            with open("custom_templates.json", "r", encoding="utf-8") as f:
                self.custom_templates = json.load(f)
        except FileNotFoundError:
            self.custom_templates = {}
    
    def _save_custom_templates(self):
        with open("custom_templates.json", "w", encoding="utf-8") as f:
            json.dump(self.custom_templates, f, ensure_ascii=False, indent=2)
