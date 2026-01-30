"""
Завдання 3. Створити програму для розв’язування квадратного рівняння. Коефіцієнти
рівняння вводяться користувачем з клавіатури.
"""

import math

print("Expresion: ax2 + bx + c = 0")

a = 0
while a == 0:
    print("The a value must not be equal to 0")
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))

D = math.pow(b, 2) - 4*a*c
solutions = list()
if D < 0:
    print("No real solutions")
elif D == 0:
    solutions.append(-b/(2*a))
else:
    solutions.append((b + math.sqrt(D))/(2*a))
    solutions.append((b - math.sqrt(D))/(2*a))

print(solutions)