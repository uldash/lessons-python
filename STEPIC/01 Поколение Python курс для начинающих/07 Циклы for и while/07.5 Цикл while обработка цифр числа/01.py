# Дано натуральное число. Напишите программу, которая выводит его цифры
# в столбик в обратном порядке.

num = int(input())
while num:
    last_digit = num % 10
    print(last_digit)
    num = num // 10