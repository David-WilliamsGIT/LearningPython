# A program that deletes files and directories

import os
import shutil


file_to_delete = "test.txt"


os.remove(file_to_delete) # delete test.txt from this directory
# use directory path instead, if you want to delete a file elsewhere on the pc

# My attempt of the program
try:
    if os.path.exists(file_to_delete):
        os.remove(file_to_delete)
        print("this file is deleted")
    else:
        print("this file is not deleted")
except FileNotFoundError:
    print(path+"this file was not found")
except PermissionError:
    print("You don't have permission to delete this file")
    


# Bro codes
# path= "empty_folder"

# try:
#     #os.remove(file_to_delete)
#     #os.rmdir(file_to_delete)
#     shutil.rmtree(path) # need this in order to delete a folder with files inside
#     #also considered dangerous
# except FileNotFoundError:
#     print("That file was not found")
# except PermissionError:
#     print("You don't have permission to delete this file")
# except OSError:
#     print("You cannot delete this file")
# else:
#     print(path+" deleted successfully")
