# На вход программе подается четное число n, n≥2. Напишите программу,
# которая выводит список четных чисел
#  [2, 4, 6, ..., n].

even_list = [i for i in range(1, int(input()) + 1) if i % 2 == 0]
print(even_list)