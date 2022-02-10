# Онлайн-школа BEEGEEK 4
# Руководитель онлайн-школы BEEGEEK и его помощник составили списки
# учеников их школы.

# Напишите программу, которая выведет все фамилии учеников, которые
# вспомнили руководитель и его помощник.

# Формат входных данных
# На вход программе в первой строке подаются фамилии,
# записанные руководителем школы, а на второй строке -
# помощником руководителя. Фамилии указываются через пробел.

# Формат выходных данных
# Программа должна вывести все фамилии учеников, отсортированных
# в лексикографическом порядке, записанные руководителем и его помощником.

# Примечание. Гарантируется, что среди учеников школы BEEGEEK нет однофамильцев.

fio1 = {*input().split()}
fio2 = {*input().split()}
print(*sorted(fio1.union(fio2)))