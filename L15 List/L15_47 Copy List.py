# Varianta 1
my_cars = ['BMW', 'Mercedes']
copied_cars = my_cars  # copiem lista prin atribuire(dupa link)
# (2 variabile se adreseaza la aceeeas lista din memorie)
copied_cars.append('Audi')
print("l_copiata :", copied_cars)
print("l_original:", my_cars)
print("id(my_cars) == id(copied_cars)-", id(my_cars) == id(copied_cars))

# Varianta 2
my_cars2 = ['BMW', 'Toyota']
copied_cars2 = my_cars2[:]  # se creaza lista noua in memorie (with slice)
copied_cars2.append('Audi')
print("l_copiata :", copied_cars2)
print("l_original:", my_cars2)
print("id(my_cars2) == id(copied_cars2)-", id(my_cars2) == id(copied_cars2))

# Varianta 3
my_cars3 = ['BMW', 'Toyota']
copied_cars3 = my_cars3.copy()  # Cu metoda '.copy()'
copied_cars3.append('Audi')
print("l_copiata :", copied_cars3)
print("l_original:", my_cars3)
print("id(my_cars3) == id(copied_cars3)-", id(my_cars3) == id(copied_cars3))

# Varianta 4
my_cars4 = ['BMW', 'Toyota']
copied_cars4 = list(my_cars4)
copied_cars4.append('Audi')
print("l_copiata :", copied_cars4)
print("l_original:", my_cars4)
print("id(my_cars4) == id(copied_cars4)-", id(my_cars4) == id(copied_cars4))
