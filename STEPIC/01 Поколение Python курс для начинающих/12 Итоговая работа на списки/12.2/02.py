# На вход программе подаются две строки текста, содержащие целые числа.
# Из данных строк формируются списки чисел L и M. Напишите программу,
# которая создает третий список, элементами которого являются суммы
# соответствующих элементов списков L и M. Далее программа должна
# вывести каждый элемент полученного списка на одной строке
# через 1 пробел.

L = [int(i) for i in input().split()]
M = [int(i) for i in input().split()]
LM = list()
for i in range(len(L)):
    LM.append(L[i] + M[i])
print(*LM)