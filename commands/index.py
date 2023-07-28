import os
from services.llm_service import LLMService
from services.json_summary_service import JSONSummaryService
from services.markdown_summary_service import MarkdownSummaryService
from exceptions.token_limit_exception import TokenLimitException
from utils.ignore import is_ignored

def index_repository(repo_path: str):
    # Instantiate the services
    llm_service = LLMService()
    json_summary_service = JSONSummaryService()
    markdown_summary_service = MarkdownSummaryService()

    # Traverse the repository
    for root, dirs, files in os.walk(repo_path):
        for file in files:
            file_path = os.path.join(root, file)

            # Check if the file type should be ignored
            if is_ignored(file):
                print(f"Ignored file: {file_path}")
                continue

            try:
                # Generate the summary using LLM
                summary = llm_service.generate_summary(file_path)

                # Write the summaries to JSON and Markdown
                json_summary_service.write_summary(file_path, summary)
                markdown_summary_service.write_summary(file_path, summary)

                print(f"Indexed file: {file_path}")

            except TokenLimitException as e:
                print(f"Failed to index file due to token limit: {file_path}. Error: {str(e)}")

    print(f"Finished indexing the repository: {repo_path}")
