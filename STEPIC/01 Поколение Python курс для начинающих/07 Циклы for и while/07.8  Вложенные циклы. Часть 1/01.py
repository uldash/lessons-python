# Дано натуральное число n , (n≤ 9). Напишите программу, которая
# печатает таблицу размером nx3 состоящую из данного числа
# (числа отделены одним пробелом).

n = int(input())
for _ in range(n):
    for _ in range(3):
        print(n, end=' ')
    print()