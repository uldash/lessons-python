# # На вход программе подается натуральное число n, а затем n
# # различных натуральных чисел, каждое на отдельной строке.
# # Напишите программу, которая выводит все общие цифры в порядке
# # возрастания у всех введенных чисел.
# Sample Input 1:
# 4
# 12345
# 236
# 3452222
# 9302
# Sample Output 1:
# 2 3

n = int(input())
nums = [{int(i) for i in input()} for _ in range(n)]
result = set(nums.pop())
result = result.intersection(*nums)
print(*sorted(result))