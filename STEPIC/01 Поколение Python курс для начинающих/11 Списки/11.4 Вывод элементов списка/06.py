# На вход программе подается натуральное число n, затем n строк, затем
# число k — количество поисковых запросов, затем k строк — поисковые
# запросы. Напишите программу, которая выводит все введенные строки,
# в которых встречаются все поисковые запросы.

n = int(input())
strings = list(input() for _ in range(n))
k = int(input())
keys = list(input().lower() for _ in range(k))

results = list()
for str in strings:
    flag = True
    for key in keys:
        if str.lower().find(key) == -1:
            flag = False
            break
    if flag and not str in results:
        results.append(str)

print(*results, sep='\n')