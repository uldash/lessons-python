# На вход программе подается натуральное число n, затем n строк, затем
# еще одна строка — поисковый запрос. Напишите программу, которая
# выводит все введенные строки, в которых встречается поисковый запрос.

n = int(input())
strings = list()

for _ in range(n):
    strings.append(input())

key = input().lower()

for str in strings:
    if str.lower().find(key) != -1:
        print(str)
