# Выберите все способы создания копии списка letters:
# letters = ['a', 'b', 'c', 'd']

letters = ['a', 'b', 'c', 'd']

# new_letters = copy(letters)
# print(new_letters)
# new_letters = new_letters.copy(letters)
# print(new_letters)
new_letters = letters.copy()
print(new_letters)
new_letters = list(letters)
print(new_letters)
new_letters = letters[:]
print(new_letters)