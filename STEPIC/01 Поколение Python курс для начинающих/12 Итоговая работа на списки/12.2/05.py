# Самый длинный
# На вход программе подается строка текста. Напишите программу,
# использующую списочное выражение, которая находит длину
# самого длинного слова.

print(max([len(i) for i in input().split()]))