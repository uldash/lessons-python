# Упаковка дубликатов
# На вход программе подается строка текста, содержащая символы.
# Напишите программу, которая упаковывает последовательности
# одинаковых символов заданной строки в подсписки.

# Формат входных данных
# На вход программе подается строка текста, содержащая символы,
# отделенные символом пробела.

# Формат выходных данных
# Программа должна вывести указанный вложенный список.

# Sample Input 2:
# w w w o r l d g g g g r e a t t e c c h e m g g p w w
# Sample Output 2:
# [['w', 'w', 'w'], ['o'], ['r'], ['l'], ['d'], ['g', 'g', 'g', 'g'],
#   ['r'], ['e'], ['a'], ['t', 't'], ['e'], ['c', 'c'], ['h'], ['e'],
#   ['m'], ['g', 'g'], ['p'], ['w', 'w']]

# def symbol_insert(lst, symbol, index):
#     pass

# text = input().split()
# text.append('0')
# result = []
# tmp = []
# for i in range(len(text) - 1):
#     if text[i] == text[i + 1]:
#         tmp.append(text[i])
#     else:
#         tmp.append(text[i])
#         result.append(tmp)
#         tmp = []

# print(result)

text = input().split()
result = []
smbl = ''

for c in text:
    if c != smbl:
        result.append(list(c))
    else:
        result[-1].append(c)
    smbl = c

print(result)