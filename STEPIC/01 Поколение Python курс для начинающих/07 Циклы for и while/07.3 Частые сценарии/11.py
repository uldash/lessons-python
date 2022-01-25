# Напишите программу, которая считывает натуральное число n и
# выводит первые nn чисел последовательности Фибоначчи

n = int(input())

current1 = 0
current2 = 1

print(current2, end=' ')

for _ in range(n - 1):
    tmp = current1 + current2
    current1, current2 = current2, tmp
    print(tmp, end=' ')

# n = int(input())
# a, b = 1, 1

# for i in range(n):
#     print(a, end=' ')
#     a, b = b, a + b