# Напишите программу, которая считывает целое положительное
# число n, n∈[1;9] и выводит значение числа n+nn+nnn

num = int(input())
print(num + (num * 10 + num) + (num * 100 + num * 10 + num))