# Даны названия трех городов. Напишите программу, которая определяет
# самое короткое и самое длинное название города.

name1, name2, name3 = input(), input(), input()

if len(name1) > len(name2):
    name1, name2 = name2, name1
if len(name2) > len(name3):
    name2, name3 = name3, name2
if len(name1) > len(name2):
    name1, name2 = name2, name1

# print(min(a, b, c, key=len ))
# print(max(a, b, c, key=len ))

print(name1)
print(name3)