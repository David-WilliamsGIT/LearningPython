# A progrom that will detect the file in the directory
import os 

path = "I:\\PythonCode\\LearningPython\\FirstLessons\\HelloPython.txt"

if os.path.exists(path): # checking if it's the path exists
    print("That location exists")
    if os.path.isfile(path): # checking if its the file exists
        print("That is a file")
    elif os.path.isdir(path): # Checking if it is a directory
        print("That is a directory")
    elif os.path.islink(path): # Checking if it is a link to a file
        print("That is a link")
    elif os.path.ismount(path): # Checking if mount point exists
        print("That is a mount point")
else:
    print("file does not exist") # printing if all else fails
    

