# Напишите программу, которая определяет, является число
# четным или нечетным.

# Sample Input 1:
# 10
# Sample Output 1:
# Четное
# Sample Input 2:
# 17
# Sample Output 2:
# Нечетное

num = int(input())

if num % 2:
    print('Нечетное')
else:
    print('Четное')