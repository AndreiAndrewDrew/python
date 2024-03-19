my_nums = (12, 34, 12, 56, 78, 34)
print(my_nums)
print(type(my_nums))

print(my_nums.count(12))
print(my_nums.index(12))

index_one = my_nums.index(12)
index_two = my_nums.index(12, index_one + 1)
print(index_two)

my_list = list(my_nums)  # convertam tuple in list
my_list.append(7)  # adaugam elemtul '7' in lista
print(my_list)

my_nums= tuple(my_list) # convertam list in tuple, inapoi
print(my_nums)

my_touple = tuple('abc')
print(my_touple)

my_touple = tuple({'firts':1, 'second':2}) # convertam dictionar in tiple
                                           # primim tuple din cheile dictionarului
print(my_touple)

