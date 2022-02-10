# На вход программе подаются две строки текста, содержащие числа.
# Напишите программу, которая определяет количество чисел, которые
# есть как в первой строке, так и во второй.

# Формат входных данных
# На вход программе подаются две строки текста, содержащие числа,
# отделенные символом пробела.

# Формат выходных данных
# Программа должна вывести количество чисел, содержащихся
# одновременно как в первой строке, так и во второй.

text1 = {int(i) for i in input().split()}
text2 = {int(i) for i in input().split()}

text3 = text1 & text2

print(len(text3))