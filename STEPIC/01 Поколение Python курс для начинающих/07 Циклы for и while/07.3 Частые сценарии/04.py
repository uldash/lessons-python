# На вход программе подается натуральное число n. Напишите программу,
# которая подсчитывает сумму тех чисел от 1 до n (включительно)
# квадрат которых оканчивается на 2, 5 или 8.

n = int(input())
total = 0
for i in range(1, n + 1):
    tmp = i**2 % 10
    if tmp == 2 or tmp == 5 or tmp == 8:
        total += i
print(total)
