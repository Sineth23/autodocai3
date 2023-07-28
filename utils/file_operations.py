import os

import ast

def get_files_in_directory(dir_path):
    # Function to get all files in a directory (recursively)
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            yield os.path.join(root, file)

def read_file_content(file_path):
    # Function to read content of a file
    with open(file_path, 'r') as file:
        return file.read()


def chunkify_python(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    module = ast.parse(content)

    chunks = []
    for node in module.body:
        # Handle functions, classes, if statements, for and while loops, try/except blocks, 
        # and top-level assignments
        if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.If, ast.For, ast.While, ast.Try, ast.Assign)):
            chunk = ast.unparse(node)
            chunks.append(chunk)

    return chunks
