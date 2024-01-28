from sympy import solve
from sympy.abc import *
import re
import copy

from text_box import get_input


def solve_equations_system(equationArray) :

    variable_symbols = set()

    for i in range(len(equationArray)):
        eq: str = equationArray[i]
        if '=' not in eq:
            print('wrong equations,try again!')
        else:
            eq=eq.replace(" ", "")
            variable_symbols.update(eq[0])
            equationArray[i] = re.sub(r'(\d)([A-Za-z])', r'\1*\2', equationArray[i])
            equationArray[i] = re.sub(r'([A-Za-z])(\d)', r'\1^\2', equationArray[i])
            equationArray[i] = equationArray[i].replace('=', '-(') + ')'

    independent_eqs = solve(equationArray, variable_symbols , dict=True)
    solvedDic = copy.deepcopy(independent_eqs)

    userInputVariables = set()
    pattern = r'\b[a-z]\b'

    for item in solvedDic:
        for value in item.values():
            vari = re.findall(pattern, str(value))
            userInputVariables.update(vari)

    userInputDic = {}

    for item in userInputVariables:
        user_value = get_input(f"Please enter the value for {item}: ")[0]
        userInputDic[item] = user_value

    for num in userInputDic.keys():
        for item in solvedDic:
            for value in item.keys():
                item[value]=item[value].subs(symbols(num), userInputDic[num])

    return {
            "solved_vars": solvedDic,
            "independent_eqs": independent_eqs
            }


#result = solve_equations_system(["y=x+2","z=2y-1","w=z+y"])
#print(result)