# Напишите программу, которая упорядочивает три числа от
# большего к меньшему.

a, b, c = int(input()), int(input()), int(input())

if a < b:
    a, b = b, a
if b < c:
    b, c = c, b
if a < b:
    a, b = b, a

print(a, b, c, sep='\n')
