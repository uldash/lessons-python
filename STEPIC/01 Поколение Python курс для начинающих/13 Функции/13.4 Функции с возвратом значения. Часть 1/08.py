# На вход программе подается число nn, а затем nn строк,
# содержащих целые числа в порядке возрастания. Из данных строк
# формируются списки чисел. Напишите программу, которая объединяет
# указанные списки в один отсортированный список с помощью функции
# quick_merge(), а затем выводит его.


def merge(list1, list2):
    result = []
    p1, p2 = 0, 0
    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1
    result += list1[p1:] + list2[p2:]
    return result


def quick_merge(lists):
    result = []
    for lst in lists:
        result = merge(result, lst)
    return result


lists = [[int(i) for i in input().split()] for _ in range(int(input()))]
print(*quick_merge(lists))