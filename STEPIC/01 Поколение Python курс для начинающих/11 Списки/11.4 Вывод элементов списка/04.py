# На вход программе подается натуральное число n, а затем n строк.
# Напишите программу, которая выводит только уникальные строки,
# в том же порядке, в котором они были введены.

n = int(input())
strings1 = list()
strings2 = list()
for _ in range(n):
    strings1.append(input())
for str in strings1:
    if str in strings2:
        continue
    else:
        strings2.append(str)
print(*strings2, sep='\n')