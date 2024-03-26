# Modules = a file containting python code. Can contain functions, classes and more
# Used with modular programming, which is to separate a program into parts
# This will be used with messages.py program

#from messages import * # imports all functions from messages.py, not recommended in large projects
# or many used modules

import messages as msg # msg for short to make it easier, a nickname

# alternative way to import messages
#from messages import hello, bye
# hello()
# bye()

msg.hello()
msg.bye()

help("modules") # shows a list of modules already in python
