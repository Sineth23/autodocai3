import os
from jinja2 import Environment, FileSystemLoader
from services.file_summary_service import FileSummaryService  # ensure this is the correct path to your service

class FolderSummaryService:
    def __init__(self, template_path='path/to/your/templates'):
        self.file_summary_service = FileSummaryService()
        self.j2_env = Environment(loader=FileSystemLoader(template_path), trim_blocks=True)

    def generate_folder_summary(self, folder_path):
        if not os.path.isdir(folder_path):
            raise ValueError(f"Provided path {folder_path} is not a directory")
        
        summary = {}
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                # Assuming you're focusing only on Python files
                if file.endswith('.py'):
                    file_path = os.path.join(root, file)
                    file_summary = self.file_summary_service.generate_file_summary(file_path)
                    summary[file_path] = file_summary

        return summary

    def save_folder_summary(self, summary, output_path):
        # Check if summary is empty
        if not summary:
            raise ValueError("Summary is empty, please ensure there are python files in the directory")
        
        # Generate markdown from template
        markdown = self.j2_env.get_template("folder_summary.j2").render(summary=summary)

        # Create directories if they don't exist
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        with open(output_path, 'w') as f:
            f.write(markdown)

        print(f"Summary for folder saved to {output_path}")
