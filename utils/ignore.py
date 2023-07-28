import fnmatch
import os

def check_ignore(file_path, ignore_list):
    """
    Function to check if a file or directory should be ignored.
    
    :param file_path: the path of the file to check
    :param ignore_list: a list of filenames, directory names, or patterns to ignore
    :return: True if the file or directory should be ignored, False otherwise
    """
    base_name = os.path.basename(file_path)
    for pattern in ignore_list:
        if fnmatch.fnmatch(base_name, pattern):
            return True
    return False
