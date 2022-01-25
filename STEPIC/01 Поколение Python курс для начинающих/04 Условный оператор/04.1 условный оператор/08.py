# Напишите программу, которая определяет наименьшее из четырёх чисел.

a, b, c, d = int(input()), int(input()), int(input()), int(input())

min_digit = a

if b < min_digit:
    min_digit = b
if c < min_digit:
    min_digit = c
if d < min_digit:
    min_digit = d

print(min_digit)