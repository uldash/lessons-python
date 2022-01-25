# Дано натуральное число n, (n≥10). Напишите программу, которая
# определяет его максимальную и минимальную цифры.

num = int(input())
max_digit = num % 10
min_digit = num % 10
num = num // 10
while num:
    last_digit = num % 10
    if max_digit < last_digit:
        max_digit = last_digit
    if min_digit > last_digit:
        min_digit = last_digit
    num = num // 10
print('Максимальная цифра равна', max_digit)
print('Минимальная цифра равна', min_digit)