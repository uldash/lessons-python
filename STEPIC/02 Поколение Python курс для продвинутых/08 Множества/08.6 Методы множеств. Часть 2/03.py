# Числа первой строки
# На вход программе подаются две строки текста, содержащие числа.
# Напишите программу, которая выводит все числа в порядке
# возрастания, которые есть в первой строке, но отсутствуют во второй.

text1 = {int(i) for i in input().split()}
text2 = {int(i) for i in input().split()}

text3 = text1 - text2
print(*sorted(text3))
