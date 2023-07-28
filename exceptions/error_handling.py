import time

from .api_limit_exception import APILimitException
from .token_limit_exception import TokenLimitException
from utils.file_operations import chunkify_python

def handle_exception(e):
    if isinstance(e, APILimitException):
        print("API Limit Reached. Sleeping for 1 hour...")
        time.sleep(3600)
        return "retry"  # signal to retry the operation
    elif isinstance(e, TokenLimitException):
        print("Token Limit Reached. Splitting file into smaller chunks...")
        chunks = chunkify_python(e.file_path)
        return chunks  # return the smaller chunks to be processed separately
    else:
        print(f"Unknown exception: {e}")
        return "abort"  # signal to abort the operation
