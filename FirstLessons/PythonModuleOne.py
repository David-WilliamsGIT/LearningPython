# Python interpreter sets "specil variables", on of which is __name__

# Basically this is in relation to Python modules
# example: Modules can be run as a standalon program
# Modules can be imported and used by other modules


import PythonModuleTwo # Python module with the name PythonModuleTwo
print(__name__)
print(PythonModuleTwo.__name__)

def hello(): # Python module with the function name hello to be called from PythonModuleTwo
    print("Hello")