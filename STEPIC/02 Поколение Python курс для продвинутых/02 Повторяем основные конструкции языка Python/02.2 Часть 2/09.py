# Дана строка текста, состоящая из букв русского алфавита "О" и "Р".
# Буква "О" – соответствует выпадению Орла, а буква "Р" – соответствует
# выпадению Решки. Напишите программу, которая подсчитывает
# наибольшее количество подряд выпавших Решек.

op = input()
res = []
counter = 0
for i in range(len(op)):
    if op[i] == 'Р':
        counter += 1
        continue
    res.append(counter)
    counter = 0
res.append(counter)
print(max(res))

# s = input().split('О')
# print(len(max(s)))
