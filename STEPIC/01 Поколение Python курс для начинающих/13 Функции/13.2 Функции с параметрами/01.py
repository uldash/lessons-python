# Напишите функцию draw_triangle(fill, base), которая принимает два
# параметра:

# fill – символ заполнитель;
# base – величина основания равнобедренного
# треугольника;
# а затем выводит его.

# Примечание. Гарантируется, что основание треугольника – нечетное
# число.


def draw_triangle(fill, base):
    # for i in range(1, base + 1):
    #     print(fill * min(i, base - i + 1))
    for i in range(-base // 2 + 1, base // 2 + 1):
        print(fill * (-abs(i) + base // 2 + 1))


fill = input()
base = int(input())

draw_triangle(fill, base)