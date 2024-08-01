import math
a = float(input("Enter the value of a "))
b = float(input("Enter the value of b "))
c = float(input("Enter the value of c "))

qutraticEquation1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
qutraticEquation2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)

print(f"Roots of Qutratic Equation is  ", qutraticEquation1, qutraticEquation2)

