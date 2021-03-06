# Урок математики
# Даны по 10-балльной шкале оценки по математике трех учеников.
# Напишите программу, которая выводит множество оценок, имеющихся
# у учеников, которые встречаются не более, чем у двух из
# указанных учеников.
# Формат входных данных
# На вход программе подаются оценки трех учеников, разделенные
# символом пробела (оценки каждого ученика на отдельной строке).
# Формат выходных данных
# Программа должна вывести множество оценок в порядке возрастания
# на одной строке, разделенных пробелами, в соответствии с условием задачи.

text1 = {int(i) for i in input().split()}
text2 = {int(i) for i in input().split()}
text3 = {int(i) for i in input().split()}
text4 = (text1 | text2 | text3) - (text1 & text2 & text3)
print(*sorted(text4))