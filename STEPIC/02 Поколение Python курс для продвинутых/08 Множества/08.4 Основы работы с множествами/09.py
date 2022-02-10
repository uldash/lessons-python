# Три слова
# На вход программе подается строка, состоящая из трех слов. Верно
# ли, что для записи всех трех слов был использован один и тот
# же набор букв?

flag = True
text = [set(s) for s in input().split()]
for i in range(1, len(text)):
    if text[0] != text[i]:
        flag = False

if flag:
    print('YES')
else:
    print('NO')