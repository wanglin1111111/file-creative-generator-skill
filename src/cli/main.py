import argparse
import sys
from core.generator import FileGenerator
from core.template_manager import TemplateManager

def main():
    parser = argparse.ArgumentParser(description="File Creative Generator CLI")
    subparsers = parser.add_subparsers(dest='command', help='可用命令')
    
    generate_parser = subparsers.add_parser('generate', help='生成文件')
    generate_parser.add_argument('--type', required=True, help='模板类型')
    generate_parser.add_argument('--output', '-o', help='输出文件路径')
    generate_parser.add_argument('--project-name', help='项目名称')
    generate_parser.add_argument('--description', help='项目描述')
    generate_parser.add_argument('--features', nargs='+', help='功能特性列表')
    
    generate_all_parser = subparsers.add_parser('generate-all', help='批量生成文件')
    generate_all_parser.add_argument('--preset', required=True, help='预设类型: python, javascript, rust')
    generate_all_parser.add_argument('--dir', '-d', default='.', help='输出目录')
    generate_all_parser.add_argument('--project-name', required=True, help='项目名称')
    
    preview_parser = subparsers.add_parser('preview', help='预览生成内容')
    preview_parser.add_argument('--type', required=True, help='模板类型')
    
    templates_parser = subparsers.add_parser('templates', help='模板管理')
    templates_parser.add_argument('action', choices=['list'], help='操作: list')
    
    args = parser.parse_args()
    
    if args.command == 'generate':
        generator = FileGenerator()
        params = {}
        if args.project_name:
            params['project_name'] = args.project_name
        if args.description:
            params['description'] = args.description
        if args.features:
            params['features'] = args.features
        
        content = generator.generate(args.type, **params)
        
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"文件已生成: {args.output}")
        else:
            print(content)
    
    elif args.command == 'generate-all':
        generator = FileGenerator()
        params = {'project_name': args.project_name}
        files = generator.generate_batch(args.preset, args.dir, **params)
        print(f"已生成文件:")
        for f in files:
            print(f"  - {f}")
    
    elif args.command == 'preview':
        generator = FileGenerator()
        content = generator.generate(args.type)
        print(content)
    
    elif args.command == 'templates' and args.action == 'list':
        manager = TemplateManager()
        templates = manager.list_templates()
        print("可用模板:")
        for template in templates:
            print(f"  {template['id']}: {template['name']}")
            print(f"      {template['description']}")
    
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
