import random as rnd


def generate_password(length, chars):
    psw = ''
    for i in range(length):
        psw += rnd.choice(chars)
    return psw


def user_question(q):
    if input(q).lower() == 'y':
        return True
    else:
        return False


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''
bad_symbols = 'il1Lo0O'

rpt = int(input('Количество паролей для генерации: '))
length = int(input('Введите длину одного пароля: '))

flag_digit = user_question('Включать ли цифры 0123456789? (y/n): ')
flag_alpha_upper = user_question(
    'Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n): ')
flag_alpha_lower = user_question(
    'Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n): ')
flag_symbol = user_question('Включать ли символы !#$%&*+-=?@^_? (y/n): ')
flag_bad_symbol_disable = user_question(
    'Исключать ли неоднозначные символы il1Lo0O? (y/n): ')

if flag_digit:
    chars += digits
if flag_alpha_upper:
    chars += uppercase_letters
if flag_alpha_lower:
    chars += lowercase_letters
if flag_symbol:
    chars += punctuation
if flag_bad_symbol_disable:
    for c in bad_symbols:
        chars = chars.replace(c, '')

for _ in range(rpt):
    print(generate_password(length, chars))