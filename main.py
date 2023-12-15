import os
from interpreter import command_processor

def get_command(line_number):
    os.system("clear")
    command = (input(f"{line_number}- "))
    return command

# Read command from termianl
line_number = 1
variables = {}
declared_variables = []

os.system("clear")
print ("""
       *** welcome to plotting language ***
       enter "--help" to see commands
       """)
input("Press Enter to Start Program")

while (True):
    command = get_command(line_number)

    if command == "halt":
        input("bye")
        break

    line_number = command_processor(command, variables, declared_variables, line_number)
    input()