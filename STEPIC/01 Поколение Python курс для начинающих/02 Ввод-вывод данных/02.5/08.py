# Дано трехзначное число abc, в котором все цифры различны.
# Напишите программу, которая выводит шесть чисел,
# образованных при перестановке цифр заданного числа.

num = int(input())
a = num % 10
b = (num % 100) // 10
c = num // 100

print(c, b, a, sep='')
print(c, a, b, sep='')
print(b, c, a, sep='')
print(b, a, c, sep='')
print(a, c, b, sep='')
print(a, b, c, sep='')
