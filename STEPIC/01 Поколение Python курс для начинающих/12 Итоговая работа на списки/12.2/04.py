# На вход программе подается строка текста. Напишите программу,
# которая определяет является ли введенная строка корректным
# телефонным номером. Строка текста является корректным телефонным
# номером если она имеет формат:

# abc-def-hijk или
# 7-abc-def-hijk
# где a, b, c, d, e, f, h, i, j, k – цифры от 0 до 9.

num = input().split('-')
flag = True

if len(num) != 3 and len(num) != 4:
    flag = False
# print(flag)
if len(num) == 4 and num[0] != '7':
    flag = False
# print(flag)
if len(num) == 4:
    del num[0]
# print(flag)
if not (len(num[0]) == 3 and len(num[1]) == 3 and len(num[2]) == 4):
    flag = False
# print(num)
# print(flag)
for c in num:
    if not c.isdigit():
        flag = False
        break

if flag:
    print('YES')
else:
    print('NO')