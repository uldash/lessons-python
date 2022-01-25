# Напишите программу определяющую евклидово расстояние между двумя
# точками, координаты которых заданы.

import math as mt

x1, y1, x2, y2 = float(input()), float(input()), float(input()), \
    float(input())

res = mt.sqrt(mt.pow(x1 - x2, 2) + mt.pow(y1 - y2, 2))
print(res)