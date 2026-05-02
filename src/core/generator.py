import os
from jinja2 import Environment, FileSystemLoader
from typing import Dict, List

class FileGenerator:
    def __init__(self):
        self.env = Environment(loader=FileSystemLoader("templates"))
    
    def generate(self, template_type: str, **kwargs) -> str:
        try:
            template = self.env.get_template(f"{template_type}.j2")
            return template.render(**kwargs)
        except Exception as e:
            raise ValueError(f"模板生成失败: {str(e)}")
    
    def generate_batch(self, preset: str, output_dir: str, **kwargs) -> List[str]:
        files_generated = []
        os.makedirs(output_dir, exist_ok=True)
        
        presets = {
            "python": ["readme", "gitignore_python", "setup_py", "requirements"],
            "javascript": ["readme", "gitignore_js", "package_json", "babel_config"],
            "rust": ["readme", "gitignore_rust", "cargo_toml"]
        }
        
        if preset not in presets:
            raise ValueError(f"未知的预设类型: {preset}")
        
        for template_name in presets[preset]:
            content = self.generate(template_name, **kwargs)
            output_path = os.path.join(output_dir, self._get_output_filename(template_name))
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(content)
            files_generated.append(output_path)
        
        return files_generated
    
    def _get_output_filename(self, template_name: str) -> str:
        mapping = {
            "readme": "README.md",
            "gitignore_python": ".gitignore",
            "gitignore_js": ".gitignore",
            "gitignore_rust": ".gitignore",
            "setup_py": "setup.py",
            "requirements": "requirements.txt",
            "package_json": "package.json",
            "babel_config": ".babelrc",
            "cargo_toml": "Cargo.toml"
        }
        return mapping.get(template_name, f"{template_name}.txt")
