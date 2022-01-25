# Вводятся 3 строки в случайном порядке. Напишите программу,
# которая выясняет можно ли из длин этих строк построить
# возрастающую арифметическую прогрессию.

a, b, c = input(), input(), input()

if len(a) > len(b):
    a, b = b, a
if len(b) > len(c):
    b, c = c, b
if len(a) > len(b):
    a, b = b, a

if len(b) - len(a) == len(c) - len(b):
    print('YES')
else:
    print('NO')