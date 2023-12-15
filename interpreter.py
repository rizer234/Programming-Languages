from entities import Equation
from methods import eval_equation,plot_equation

def command_processor(command: str, vars: dict, declared_vars: list, line_number: int):
    parts  = command.split(" ")
    opcode = parts[0]

    # check for empty or comment line
    if opcode == "" or opcode.startswith('!--'):
        return line_number + 1

    # check if its a label
    if opcode.endswith(":"):
        return line_number + 1
    
    elif opcode == "declare":
        declared_vars.append(parts[1])
        vars[parts[1]] = Equation("")
        return line_number+1
    
    elif opcode == "set":
        if parts[1] not in declared_vars:
            print (parts[1].equation + " not declared")
        else:
            vars[parts[1]].equation = parts[2]
        return line_number+1

    elif opcode == "print":
        print_string = ' '.join(parts[1:])[1:-1]
        print (print_string)
        return line_number+1
    
    elif opcode == "eval":
        if parts[1] not in declared_vars:
            print (parts[1] + " not declared")
        else:
            vars[parts[1]].finalEquation, vars[parts[1]].varCount = eval_equation(vars[parts[1]].equation)
        return line_number+1
    
    elif opcode == "plot":
        if parts[1] not in declared_vars:
            print (parts[1] + " not declared")
        else:
            plot_equation(vars[parts[1]], ((int(parts[2])), int(parts[3])) )
        return line_number+1

    elif len(parts) == 1 and opcode in declared_vars:
        print (vars[opcode].equation)
        return line_number+1

    elif opcode == "--help":
        print ("""
               commands:
               - declare x string: creates x var
               - {\\var}: returns {var} value
               - set x eq: sets eq to x var
               - print 'string': displayes your statement
               - eval eq: evaluates your eq equation
               - plot eq x1 x2: plotting your eq equation in range x1 to x2
               - halt: for exit from app
               """)
        return line_number+1

    else:
        print (""""Please enter correct statement
               "--help" command for view commands""")
        return line_number