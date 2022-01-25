# Дано натуральное число nn. Напишите программу, которая выводит
# значение суммы 1!+2!+3!+..+n!

n = int(input())
acc = 0
for i in range(1, n + 1):
    fct = 1
    for j in range(1, i + 1):
        fct *= j
    acc += fct
print(acc)