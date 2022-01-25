# На вход программе подается два натуральных числа a и b
# (a< b). Напишите программу, которая находит все простые
# числа от a до b включительно.

a, b = int(input()), int(input())
if a == 1:
    a += 1
for i in range(a, b + 1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
