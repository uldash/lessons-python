# Напишите программу, которая считывает 10 чисел и выводит
# произведение отличных от нуля чисел.

total = 1
for _ in range(10):
    tmp = int(input())
    if tmp:
        total *= tmp
print(total)