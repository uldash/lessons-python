# Напишите программу, которая сравнивает пароль и его
# подтверждение. Если они совпадают, то программа выводит:
# «Пароль принят», иначе: «Пароль не принят».

pass_first, pass_second = input(), input()

if pass_first != pass_second:
    print('Пароль не принят')
else:
    print('Пароль принят')