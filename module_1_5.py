immutable_var = 1, 2, 3, True, 'string'
print(immutable_var)

#в кортеже нельзя изменять элементы, так как данные фиксируются в памяти
immutable_var[0] = 5

mutable_list = [1, 2, 3, 4, 5]
mutable_list[3] = 33
print(mutable_list)