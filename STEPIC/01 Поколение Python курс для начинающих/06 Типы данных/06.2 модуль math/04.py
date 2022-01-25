# Напишите программу, вычисляющую значение тригонометрического выражения
# sin x + cos x + tan^2 x

import math as mt

x = float(input())

x = mt.radians(x)

print(mt.sin(x) + mt.cos(x) + mt.pow(mt.tan(x), 2))
