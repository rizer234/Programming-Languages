
from entities import Equation
from methods import eval_equation,plot_equation


####### examples #########
#(x2+y2-1)^3-(x2)*y3=0
#2.8x^2*(x^2*(2.5x^2+y^2-2)+1.2y^2*(y*(3y-0.75)-6.0311)+3.09)+0.98y^2*((y^2-3.01)*y^2+3)-1.005=0

if __name__ == "__main__":

    inputEquation = input("Enter a mathematical equation (use 'x,y,z' as the variable): ")

    equ = Equation(inputEquation)

    equ.finalEquation, equ.varCount = eval_equation(inputEquation)

    plot_equation(equ)
