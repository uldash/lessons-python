# На вход программе подается натуральное число n, а затем n целых
# чисел. Напишите программу, которая создает из указанных чисел
# список, затем удаляет все элементы стоящие по нечетным
# индексам, а затем выводит полученный список.

n = int(input())
lst = list()
for _ in range(n):
    lst.append(int(input()))
for i in range(1, n // 2 + 1):
    del lst[i]
print(lst)