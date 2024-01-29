import os
from interpreter import command_processor
from colorama import Fore

statements = []

def display_statements(statements: list):
    for statement in statements:
        print (f"{Fore.WHITE}statement, '\n'")

def get_command(line_number):
    command = (input(f"{Fore.WHITE}{line_number}- "))
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

os.system("clear")


while (True):

    # check if line_number increases means new valid statement have been append
    last_number = line_number
    
    display_statements(statements)
    command = get_command(line_number)

    if (line_number - last_number):
        statements.append(str(line_number) + '- ' + command)

    if command == "halt":
        input("bye")
        break

    line_number = command_processor(command, variables, declared_variables, line_number)
    input()



    #(x2+y2-1)^3-(x2)*y3=0 
