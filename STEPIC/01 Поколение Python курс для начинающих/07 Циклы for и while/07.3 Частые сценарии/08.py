# На вход программе подается натуральное число n.
# Напишите программу вычисления знакочередующей суммы
# 1-2+3-4+5-6 + ... + n * (-1)^(n+1).

n = int(input())
flag = True
total = 0
for i in range(1, n + 1):
    if flag:
        total += i
    else:
        total -= i
    flag = not flag
print(total)
