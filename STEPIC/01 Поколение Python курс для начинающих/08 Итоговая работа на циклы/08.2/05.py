# Дано натуральное число n , (n>99). Напишите программу, которая
# определяет его третью (с начала) цифру.

n = int(input())

while n > 99:
    digit = n % 10
    n //= 10
print(digit)