import json
import os
from .folder_summary_service import FolderSummaryService

class JSONSummaryService:

    def __init__(self):
        self.folder_summary_service = FolderSummaryService()

    def generate_json_summary(self, codebase_path):
        summary = {}
        # Loop through all directories in the codebase and generate a summary for each
        for root, dirs, _ in os.walk(codebase_path):
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                dir_summary = self.folder_summary_service.generate_folder_summary(dir_path)
                summary[dir_path] = dir_summary

        return summary

    def save_json_summary(self, summary, output_path):
        with open(output_path, 'w') as f:
            json.dump(summary, f, indent=4)

        print(f"JSON summary for codebase saved to {output_path}")
