immutable_var = (1, 'name', 3.7, True, [1, 2])
print(immutable_var)
# immutable_var [3] = False Проверка, что кортеж не поддерживает изменение по элементам
print(immutable_var.__sizeof__()) # Занимаемое место в памяти
mutable_list = [3, False, 'name', 4.8, 'str']
print(mutable_list)
mutable_list[0] = 'right' # Изменим первый элемент списка
mutable_list[-1] = 333 # Изменим ппоследний элемент списка
print(mutable_list)
mutable_list.append('straight') # Добавим элемент в конец списка
print(mutable_list)
mutable_list.extend('13579') # Добавим еще элемент в список
print(mutable_list)
print(mutable_list.__sizeof__()) # Занимаемое место в памяти