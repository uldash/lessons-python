# Урок биологии
# Даны по 10-балльной шкале оценки по биологии трех учеников. Напишите
# программу, которая выводит множество оценок, не встречающихся ни у
# одного из трех учеников.

# Формат входных данных
# На вход программе подаются оценки трех учеников, разделенные
# символом пробела (оценки каждого ученика на отдельной строке).

# Формат выходных данных
# Программа должна вывести множество оценок в порядке возрастания на
# одной строке, разделенных пробелами, в соответствии с условием задачи.

# Примечание. Оценка ученика находится в диапазоне от 0 до 10
# включительно.

text1 = {int(i) for i in input().split()}
text2 = {int(i) for i in input().split()}
text3 = {int(i) for i in input().split()}
text4 = {*range(11)}
text5 = text4 - (text1 | text2 | text3)
print(*sorted(text5))
