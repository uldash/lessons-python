# Напишите программу, которая считывает три числа и подсчитывает
# сумму только положительных чисел.

a, b, c = int(input()), int(input()), int(input())

summ = 0
if a > 0:
    summ += a
if b > 0:
    summ += b
if c > 0:
    summ += c

print(summ)
