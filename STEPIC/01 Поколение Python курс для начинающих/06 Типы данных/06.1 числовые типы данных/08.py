# Напишите программу, которая находит наименьшее и
# наибольшее из пяти чисел.

a1, a2, a3, a4, a5 = int(input()), int(input()), int(input()), \
    int(input()), int(input())

num_max = max(a1, a2, a3, a4, a5)
num_min = min(a1, a2, a3, a4, a5)

print('Наименьшее число =', num_min)
print('Наибольшее число =', num_max)
