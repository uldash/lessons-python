# Дано натуральное число n , (n>9). Напишите программу, которая
# определяет его вторую (с начала) цифру.

num = int(input())

while num > 99:
    num = num // 10
print(num % 10)