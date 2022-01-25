# Будем считать email адрес корректным, если в нем есть символ
# собачки (@) и точки. Напишите программу проверяющую
# корректность email адреса.

text = input()
text1 = '@'
text2 = '.'
if text1 in text and text2 in text:
    print('YES')
else:
    print('NO')