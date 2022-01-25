# Даны три вещественных числа a, b, c. Напишите программу, которая
# находит вещественные корни квадратного уравнения

import math as mt

a, b, c = float(input()), float(input()), float(input())

d = mt.pow(b, 2) - 4 * a * c
if d < 0:
    print('Нет корней')
elif d == 0:
    x = -b / (2 * a)
    print(x)
else:
    x1 = (-b + mt.sqrt(d)) / (2 * a)
    x2 = (-b - mt.sqrt(d)) / (2 * a)
    print(min(x1, x2))
    print(max(x1, x2))
