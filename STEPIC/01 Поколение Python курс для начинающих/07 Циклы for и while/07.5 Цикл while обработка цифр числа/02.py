# Дано натуральное число. Напишите программу, которая
# меняет порядок цифр числа на обратный.

import re
from unittest import result

num = int(input())
res = 0
while num:
    last_digit = num % 10
    res = res * 10 + last_digit
    num = num // 10
print(res)
