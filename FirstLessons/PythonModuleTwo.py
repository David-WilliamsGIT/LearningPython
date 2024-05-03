# this is part of the PythonModuleOne.py file, please refer to that file for additional code

# this is a module file
import PythonModuleOne

PythonModuleOne.hello() # this is calling the function hello from PythonModuleOne

if __name__ == '__main__':
    print("running this module directly from PythonModuleTwo")
    
else:
    print("running other module indirectly")

