import os
from jinja2 import Environment, FileSystemLoader

class MarkdownSummaryService:
    def __init__(self):
        self.j2_env = Environment(loader=FileSystemLoader('path/to/your/templates'), trim_blocks=True)

    def generate_markdown_summary(self, folder_path):
        summary = {}
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                summary[file_path] = {"filename": file}

        return summary

    def save_markdown_summary(self, summary, output_path):
        # Generate markdown from template
        markdown = self.j2_env.get_template("markdown_summary.j2").render(summary=summary)

        with open(output_path, 'w') as f:
            f.write(markdown)

        print(f"Markdown summary for codebase saved to {output_path}")
