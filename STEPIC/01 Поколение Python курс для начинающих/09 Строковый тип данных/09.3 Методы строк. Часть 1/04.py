# На вход программе подается строка. Напишите программу, которая
# подсчитывает количество буквенных символов в нижнем регистре.

s = input()
counter = 0
for c in s:
    if c != c.upper():
        counter += 1
print(counter)