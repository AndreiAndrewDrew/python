my_dict = {'a': True, 'b': 10}
print(my_dict)
del my_dict['a']  # stergem element din dictionar cu instruciunea 'del'
print(my_dict)
my_dict.__delitem__('b')  # instructiunea este la fel ca metoda magica '__delitem__'
print(my_dict)
print(my_dict.__delitem__)

my_list = [1, 3]
print(my_list)
del my_list[0]  # stergem primul element din lista
print(my_list)
my_list.__delitem__(0)  # din nou stergem primul element din lista
print(my_list)  # rezultat [] lista o sa fie goala
