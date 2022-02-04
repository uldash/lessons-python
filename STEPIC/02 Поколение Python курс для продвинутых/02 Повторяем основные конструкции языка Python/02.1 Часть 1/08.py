# Задача Иосифа Флавия
# n человек, пронумерованных числами от 1 до n, стоят в кругу. Они
# начинают считаться, каждый k-й по счету человек выбывает из круга,
# после чего счет продолжается со следующего за ним человека.
# Напишите программу, определяющую номер человека, который
# останется в кругу последним.

# Формат входных данных
# На вход программе подаются два числа n и k, записанные на
# отдельных строках.

# Формат выходных данных
# Программа должна вывести одно число – номер человека,
# который останется в кругу последним.

# Примечание 1. Подробнее ознакомиться с классической
# задачей Иосифа Флавия можно тут.

# Примечание 2. Визуализацию работы алгоритма можно посмотреть тут.

n, k = [i for i in range(int(input()))], int(input())
i = 0
while len(n) > 1:
    i = (i + k - 1) % len(n)
    del n[i]
print(n[0] + 1)
