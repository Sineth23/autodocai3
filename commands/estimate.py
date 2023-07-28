import os
from services.llm_service import LLMService
from constants import API_LIMIT

def estimate_cost(repo_path: str):
    # Check if the path exists
    if not os.path.isdir(repo_path):
        raise ValueError(f"The provided path {repo_path} does not exist or is not a directory")

    # Count the number of files in the repository
    num_files = 0
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(repo_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link or other non-file
            if not os.path.isfile(fp):
                continue
            num_files += 1
            total_size += os.path.getsize(fp)

    # Calculate the average file size
    avg_file_size = total_size / num_files if num_files else 0

    # Calculate the estimated cost based on the number of files and their average size
    estimated_cost = (num_files * avg_file_size) / API_LIMIT

    print(f"The estimated cost of indexing this repository is: {estimated_cost}")

    return estimated_cost
