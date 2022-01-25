# На вход программе подается натуральное число n. Напишите программу,
# которая вычисляет значение выражения
# (1+1/2 + 1/3 + ... + 1/n) - ln(n).

import math as mt

n = int(input())
total = 0
for i in range(1, n + 1):
    total += 1 / i
total -= mt.log(n)
print(total)