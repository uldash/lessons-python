# На вход программе подается натуральное число n, а затем n строк.
# Напишите программу, которая создает из указанных строк список
# и выводит его.

n = int(input())
lst = list()
for _ in range(n):
    elmnt = input()
    lst.append(elmnt)
print(lst)