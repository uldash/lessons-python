# Дано натуральное число. Напишите программу, которая определяет,
# является ли последовательность его цифр при просмотре справа налево
# упорядоченной по неубыванию.

num = int(input())
flag = True
while num > 9:
    curent_digital = num % 10
    num = num // 10
    if curent_digital > num % 10:
        flag = False
        break

if flag:
    print('YES')
else:
    print('NO')