import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()
ROOT.withdraw()

def get_input(statement: str):
    inputs = []
    while True:
        USER_INP = simpledialog.askstring(title="Math Interpreter",
            prompt=statement)
        
        if USER_INP == '0' or USER_INP == None or USER_INP == '':
            break
        inputs.append(USER_INP)

    return inputs

    