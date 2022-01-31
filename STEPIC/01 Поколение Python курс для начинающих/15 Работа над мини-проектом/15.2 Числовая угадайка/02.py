import random as rnd


def is_valid(text):
    if text.isdigit() and 1 <= int(text) <= 100:
        return True
    else:
        return False


def right_border():
    return int(input('Введите правую границу для случайного выбора числа: '))


counter = 0
print('Добро пожаловать в числовую угадайку')
m = right_border()
n = rnd.randint(1, m)

while True:
    user_n = input()
    if is_valid(user_n):
        user_n = int(user_n)
    else:
        print(f'А может быть все-таки введем целое число от 1 до {m}?')
        continue
    counter += 1
    if user_n < n:
        print('Ваше число меньше загаданного, попробуйте еще разок')
        continue
    elif user_n > n:
        print('Ваше число больше загаданного, попробуйте еще разок')
        continue
    else:
        print('Вы угадали, поздравляем!')
        print(f'Количество попыток: {counter}')
        print('Сыграть еще раз (y/n)?')
        if input().lower() == 'y':
            m = right_border()
            n = rnd.randint(1, m)
            counter = 0
            print('Добро пожаловать в числовую угадайку')
            continue
        else:
            break
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')