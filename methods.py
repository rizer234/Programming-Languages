import re
import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, sympify,solve,Eq, solveset, S

def plot_equation_2d(equationObj, x_range=(-10, 10), num_points=400):

    equation = equationObj.finalEquation

    x = np.linspace(x_range[0], x_range[1], num_points)

    newx=[]
    newy=[]

    for val in x:
        xx=equation.subs(symbols('x'), val)
        xxx = Eq(xx,0)
        y=symbols('y')
        sol =solveset(xxx, y, domain=S.Reals)

        for item in sol:
            newx.append(val)
            newy.append(item)



    plt.scatter(newx, newy)
    #plt.plot(newx, newy)

    plt.title(f'Plot of {equationObj.equation}')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.grid(True)
    plt.show()


def plot_equation_3d(equationObj, x_range=(-10, 10), num_points=15):
    equation = equationObj.finalEquation

    x = np.linspace(x_range[0], x_range[1], num_points)
    y = np.linspace(x_range[0], x_range[1], num_points)
    zz = []

    newx=[]
    newy=[]

    for xitem in x:
        for yitem in y:

            xx2 = equation.subs(symbols('x'), xitem).subs(symbols('y'), yitem)
            xxx2 = Eq(xx2, 0)
            z = symbols('z')
            sol = solveset(xxx2, z, domain=S.Reals)

            for item in sol:
                newx.append(xitem)
                newy.append(yitem)
                zz.append(item)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Scatter plot
    ax.scatter(newx, newy, zz, c='r', marker='o')

    plt.title(f'Plot of {equationObj.equation}')

    # Set labels
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')

    # Show the plot
    plt.show()


def eval_equation(value):

    value = re.sub(r'(\d)([A-Za-z])', r'\1*\2', value)
    value = re.sub(r'([A-Za-z])(\d)', r'\1^\2', value)
    #inputEquation = re.sub(r'([A-Za-z])([A-Za-z])', r'\1*\2', inputEquation)

    varCount = 0

    if 'x' in value:
        varCount += 1
    if 'y' in value:
        varCount += 1
    if 'z' in value:
        varCount += 1


    if '=' in value:
        value=value.replace('=', '-(')
        value = value + ')'
    else:
        varCount += 1
        if varCount == 2:
            value = value + '-y'

        elif varCount == 3:
            value = value + '-z'

    value = sympify(value)

    return value, varCount


def plot_equation(equ, x_range=(-10, 10)):

    if equ.varCount <= 2:
        plot_equation_2d(equ, x_range)

    elif equ.varCount == 3:
        plot_equation_3d(equ, x_range)
