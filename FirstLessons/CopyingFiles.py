# This program is going to copy text files

# copyfile() copies the contents of a file
# copy() = copyfile() + permissions mode + destination can be a directory
# copy2() = copy() + copies metadata files creation and modification times

import shutil

shutil.copy('text.txt', 'text_copy.txt')
shutil.copyfile('text.txt', 'I:\PythonCode\LearningPython\FirstLessons\copied_text.txt')