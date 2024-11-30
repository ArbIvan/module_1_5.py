# 2. Задайте переменные разных типов данных:
immutable_var = 1, 0.5, 'Ivan', False, [2, 3]
print(immutable_var)

# 3. Изменение значений переменных:
immutable_var[4][0] = 4
print(immutable_var)
# Кортеж - это неизменяемая упорядоченная колекция.
# В кортеже можно изменить только те элементы, которые являются изменяемыми типами данных.

# 4. Создание изменяемых структур данных:
mutable_list = [1, 0.5, 'Ivan', False, [2, 3]]
print(mutable_list)
mutable_list[0] = 10
mutable_list[1] = 0.50
mutable_list[2] = 'Arbuzov'
mutable_list[3] = True
mutable_list[4][1] = 30
print(mutable_list)