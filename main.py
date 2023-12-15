import os

def get_command(line_number):
    os.system("clear")
    command = (input(f"{line_number}- "))
    return command

def evaluate_command(command: str):
    print ("Soppusly process of command done...")


# Read command from termianl
line_number = 1
while (True):
    command = get_command(line_number)
    if command == "halt":
        input("bye")
        break
    evaluate_command(command)
    input()
    line_number += 1