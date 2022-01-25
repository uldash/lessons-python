# Напишите программу, которая считывает последовательность из 10 целых
# чисел и определяет является ли каждое из них четным или нет.

flag = True
for _ in range(10):
    if int(input()) % 2:
        flag = False
if flag:
    print('YES')
else:
    print('NO')