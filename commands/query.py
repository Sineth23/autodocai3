import os
from services.json_summary_service import JSONSummaryService

def query_summary(file_path: str):
    # Validate the file path
    if not os.path.isfile(file_path):
        print(f"Invalid file path: {file_path}")
        return

    # Instantiate the services
    json_summary_service = JSONSummaryService()

    try:
        # Query the JSON summary for the specified file
        summary = json_summary_service.query_summary(file_path)

        if summary:
            print(f"Summary for {file_path}:\n\n{summary}")
        else:
            print(f"No summary found for {file_path}")

    except Exception as e:
        print(f"Failed to query summary for file: {file_path}. Error: {str(e)}")
