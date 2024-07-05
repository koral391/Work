immutable_var = 'Костюм', 1, 3, 5, False
print(immutable_var)
# Элементы кортежа не изменяемы и сохраняют свои значение, их можно только допоkнить за счет сложения или умножить на определенное количество тех же элементов
# Пример добавления
immutable_var = ('Костюм', 1, 3, 5, False) + (1, 2, 3)
print(immutable_var)
# Пример умножения
immutable_var = ('Костюм', 1, 3, 5, False) * 2
print(immutable_var)

mutable_list = ["Картошка", 'Философия', 47, 89]
print(mutable_list)
mutable_list [3] = 154
mutable_list. append('География')
print(mutable_list)