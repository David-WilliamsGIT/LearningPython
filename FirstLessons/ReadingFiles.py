# Program to read the text inside a file and print it back to the screen
import os 
try:
    with open('I:\\PythonCode\\LearningPython\\FirstLessons\\HelloPython.txt') as file:
        contents = file.read()
        print(contents)
except FileNotFoundError as e:
    print("That File was not found: ")

#print(file.closed) use this if you are not using with open which automatically closes the file after execution

