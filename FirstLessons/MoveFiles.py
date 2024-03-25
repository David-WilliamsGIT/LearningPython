# Program to move files from one directory to another

import os

source = "text.txt " # source directory of file
destination = "I:\\PythonCode\\LearningPython\\FirstLessons\\text.txt " # destination directory

try:
    if os.path.exists(destination):
        print("The file already exists in the destination directory")
    else:
        os.replace(source, destination)
        print("The file has been moved successfully")  
except FileNotFoundError:
    print(source+" was not found")