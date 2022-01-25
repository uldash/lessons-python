# Дано натуральное число. Напишите программу, которая определяет,
# состоит ли указанное число из одинаковых цифр.

num = int(input())
flag = True

while num > 9:
    current_digital = num % 10
    num = num // 10
    if current_digital != num % 10:
        flag = False
        break
if flag:
    print('YES')
else:
    print('NO')
