import os
from services.json_summary_service import JSONSummaryService

def initialize_repository(repo_path: str):
    # Validate that the provided path is a directory
    if not os.path.isdir(repo_path):
        print(f"The provided path is not a directory: {repo_path}")
        return

    try:
        # Instantiate the services
        json_summary_service = JSONSummaryService()

        # Initialize the JSON summary for the repository
        json_summary_service.initialize_summary(repo_path)

        print(f"Repository at {repo_path} initialized successfully")
    except Exception as e:
        print(f"Failed to initialize repository due to error: {str(e)}")
