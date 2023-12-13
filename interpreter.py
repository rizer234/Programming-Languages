import sys
from entities import Equation
from methods import eval_equation,plot_equation


# read arguments
# program_filepath = sys.argv[1]
program_filepath = "Program.oll"

###########################
#     Tokenize Program
###########################


# read file lines
program_lines = []
with open(program_filepath, "r") as program_file:
    program_lines = [
        line.strip()
            for line in program_file.readlines()]



program = []
token_counter = 0
label_tracker = {}


for line in program_lines:
    parts  = line.split(" ")
    opcode = parts[0]

    # check for empty line
    if opcode == "" or opcode.startswith('!--'):
        continue

    # check if its a label
    if opcode.endswith(":"):
        label_tracker[opcode[:-1]] = token_counter
        continue

    # store opcode token
    program.append(opcode)
    token_counter += 1

    # handle each opcode
    if opcode == "declare":
        program.append(parts[1])
        program.append(parts[2])
        token_counter += 2
    
    elif opcode == "set":
        # parse string literal
        label = parts[1]
        value = ' '.join(parts[3:])[1:-1]
        program.append(label)
        program.append(value)
        token_counter += 2

    elif opcode == "print":
        # read label
        print_string = ' '.join(parts[1:])[1:-1]
        program.append(print_string)
        token_counter += 1
    
    elif opcode == "get":
        # read label
        label = parts[1]
        program.append(label)
        token_counter += 1
    
    elif opcode == "eval":
        # read label
        label = parts[1]
        program.append(label)
        token_counter += 1
    
    elif opcode == "plot":
        # read plot
        label = parts[1]
        start = parts[2]
        end = parts[3]
        program.append(label)
        program.append(start)
        program.append(end)
        token_counter += 3



###########################
#     Interpret Program
###########################


pc = 0
variables = {}

while program[pc] != "halt":
    opcode = program[pc]
    pc += 1

    if opcode == "declare":
        variables[program[pc]] = Equation("")
        pc += 2
    elif opcode == "set":
        variables[program[pc]].equation = program[pc+1]
        pc += 2
    elif opcode == "print":
        print(program[pc])
        pc += 1
    elif opcode == "get":
        variables[program[pc]].equation = input()
        pc += 1
    elif opcode == "eval":
        variables[program[pc]].finalEquation, variables[program[pc]].varCount = eval_equation(variables[program[pc]].equation)
        pc += 1
    elif opcode == "plot":
        plot_equation(variables[program[pc]],(int(program[pc+1]), int(program[pc+2])))
        pc += 3

