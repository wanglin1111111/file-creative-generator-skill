from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Optional
from core.generator import FileGenerator
from core.template_manager import TemplateManager

app = FastAPI(title="File Creative Generator Skill", version="1.0.0")

generator = FileGenerator()
template_manager = TemplateManager()

class GenerateRequest(BaseModel):
    template_type: str
    output_path: Optional[str] = None
    parameters: Dict[str, str] = {}

class BatchGenerateRequest(BaseModel):
    preset: str
    output_dir: str
    parameters: Dict[str, str] = {}

class CustomTemplateRequest(BaseModel):
    name: str
    content: str
    variables: List[str] = []

@app.get("/api/templates")
def get_templates():
    return {"templates": template_manager.list_templates()}

@app.post("/api/generate")
def generate_file(request: GenerateRequest):
    try:
        content = generator.generate(
            template_type=request.template_type,
            **request.parameters
        )
        if request.output_path:
            with open(request.output_path, "w", encoding="utf-8") as f:
                f.write(content)
        return {
            "success": True,
            "message": "文件生成成功",
            "output_path": request.output_path,
            "content": content
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/generate/batch")
def batch_generate(request: BatchGenerateRequest):
    try:
        files_generated = generator.generate_batch(
            preset=request.preset,
            output_dir=request.output_dir,
            **request.parameters
        )
        return {
            "success": True,
            "files_generated": files_generated
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/templates/custom")
def add_custom_template(request: CustomTemplateRequest):
    try:
        template_manager.add_template(
            name=request.name,
            content=request.content,
            variables=request.variables
        )
        return {"success": True, "message": "模板添加成功"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.delete("/api/templates/{template_id}")
def delete_template(template_id: str):
    try:
        template_manager.delete_template(template_id)
        return {"success": True, "message": "模板删除成功"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/")
def root():
    return {"message": "File Creative Generator Skill API"}
