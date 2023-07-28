def directory_prompt(directory_path):
    """
    Function to generate a prompt for summarizing a directory.

    :param directory_path: the path of the directory to generate a prompt for
    :return: a string containing the prompt
    """
    return f"This is a summary of the directory '{directory_path}':\n"

def file_prompt(file_path):
    """
    Function to generate a prompt for summarizing a file.

    :param file_path: the path of the file to generate a prompt for
    :return: a string containing the prompt
    """
    return f"This is a summary of the file '{file_path}':\n"
