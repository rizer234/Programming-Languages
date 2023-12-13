

def get_command():
    pass

def evaluate_command(command: str):
    pass

# Read command from termianl
while (True):
    command = get_command()
    if command == "halt":
        break
    evaluate_command(command)
