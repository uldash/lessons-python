# Напишите программу, которая считает стоимость трех компьютеров,
# состоящих из монитора, системного блока, клавиатуры и мыши.

# Sample Input 1:

# 9900
# 55600
# 3999
# 2990
# Sample Output 1:

# 217467

cost_display = int(input())
cost_box = int(input())
cost_keyboard = int(input())
cost_mouse = int(input())

print(3 * (cost_display + cost_box + cost_keyboard + cost_mouse))
