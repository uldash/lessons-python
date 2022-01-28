# Напишите функцию is_password_good(password), которая принимает в качестве аргумента строковое значение пароля password и возвращает значение True если пароль является надежным и False в противном случае.

# Пароль является надежным если:

# его длина не менее 8 символов;
# он содержит как минимум одну заглавную букву (верхний регистр);
# он содержит как минимум одну строчную букву (нижний регистр);
# он содержит хотя бы одну цифру.


# объявление функции
def is_password_good(password):
    if len(password) < 8:
        return False
    flag1, flag2, flag3 = False, False, False
    for c in password:
        if c.isdigit():
            flag1 = True
        if c.isalpha() and c.isupper():
            flag2 = True
        if c.isalpha() and c.islower():
            flag3 = True
        if flag1 and flag2 and flag3:
            return True
    return False


# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))