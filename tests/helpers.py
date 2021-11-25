import os

# To run pytest from the root then we need to use absolute path
# To open file easier we can use below function
def open_file(path: str):
    current_dir = os.path.dirname(__file__)
    absolute_path = os.path.join(current_dir, path)
    return open(absolute_path, "rb")