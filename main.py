print("     L1,2,3,4,5,6:")
# print("Hello World from PyChram")
# name = input("Enter your name: ")
#
# print(name)

# def my_name(name):
#     print(name)
#
#
# my_list = [1, 2, 3]
#
# print(my_list)  # This is comment

# This
# is
# comment (combinatia de taste 'Ctrl' + '/')

print('     L7: Введение в функции ')
print('         L7_01: Объявление функции, параметры и аргументы ')

# def hello(name):
#     print("hello there,", name)
#     print("Hi there,", name)
#
#
# hello('Andrew')
# hello('Evelina')

print('         L7_02: Ключевое слово return в функциях ')

# def sum_nums(a, b):
#     sum = a + b
#     print(sum)
#
#
# sum_nums(10, 5)
# sum_nums(50.34, 21)
#
#
# # Cu ajutorul return
#
# def sum_nums(a, b):
#     sum = a + b
#     return sum
#
# first_sum = sum_nums(10,5)
# print(first_sum)
# second_sum = sum_nums(50.22, 11)
# print(second_sum)


print('     L8: Выражения и инструкции')
# print(print(10 + 5))
# input("Enter your name:")
# name2 = 'Andrew'
# if name2:
#     print(name2)
#
# import datetime
#
# print(datetime.MAXYEAR)

print('     L10: Типы и структуры данных')
# def print_name(name):
#     print(name)
#
#
# print_name('oarecare text')
# print_name(324)
# print_name(23 + 7)
#
# print_name=15
#
# print_name('chemam functia') # Eroare
#
# my_name3 = 'Andrew'
# print(id(my_name3))
#
# other_name = my_name3
# print(id(other_name))

print('     L11: Strings')
# my_name10 = 'Lesson10'
# print(id(my_name10))
# print(type(my_name10))
#
# info_mesage = """Message
# cu mai multe runduri,
# folosind 3 ghelemeli"""
#
# print(info_mesage)
#
# print(len(my_name10))
# print(my_name10[0])  # L- primim primul simbol din rindrul my_name10
# print(my_name10[3:6])  # son- primim de la care simbol pin la care
#
# my_comment = "Este un commentariu scurt"
# print(len(my_comment))
# print(my_comment.replace('scurt', 'lung'))
# print(my_comment)
# print(my_comment.count(' '))  # numar spatsile goale in shir
# print(my_comment.count('c'))
# print(my_comment.count('mm'))
# print(my_comment[0])  # primul simbol din shir
# print(my_comment[-1])  # ultimul simbol din shir
# print(my_comment[-2])
# print(my_comment[1:10])
# print(my_comment[-8:-1])
# print(my_comment[8:])

print('     L12: Numbers in Python')
# user_input = input("Enter any number: ")
# any_number = int(user_input)  # inputul la user il convertam in
# # tipul 'int', po defaultu e 'str'
#
# any_number_v2 = int(input("Enter any number: "))
# # alta varianta de convertatsie
#
# print(any_number)
# print(type(any_number))

# base = 2
# power = 3
# print(pow(base, power))
# print(type(pow(base, power)))
# one_milion = 1_000_000  # cifrele mari spoate de separat cu '_'
# print(one_milion)
#
# number_d = 3_142
# print(number_d)
#
# str_temperature = '23.6'
# teperature = float(str_temperature)
# print(teperature)
# print(type(teperature))
#
# average_price = 28.6
# print(round(average_price))
#
# rate = 0.79
# print(round(rate))
# print(type(round(rate)))
#
# complex_a = 3 + 6j
# complex_b = 4 + 7j
# sum = complex_b + complex_a
# dif = complex_a - complex_b
# inmul = complex_a * complex_b
#
# print(sum)
# print(dif)
# print(inmul)
# print(type(sum))

print('     L13: Logics Types')
# is_authorized = True
# print(is_authorized)
# print(type(is_authorized))
#
# print(bool(10))
# print(bool('abc'))
# print(bool([]))
# print(bool([1, 2]))
# print(bool(None))
#
# print(100 > 10)
# print('Long string' > 'Short')
# print([] == [])
# print({'a': 3} == {'a': 6})

print('     L14: Magic Methods')
# int_num = 3
# float_num = 4.3
# print(int_num + float_num)
# print(float_num + int_num)
#
# bool_value = True
# int_value = 7
# print(bool_value + int_value)  # rez este 8 valoarea True este 1
# # respectiv 1 +7 = 8
# print(int_value + bool_value)
#
# str_value = 'abc'
# print(int_value * str_value)
#
# print(str_value * int_value)
#
# #print(float_num * str_value)# Eroare cu float string nu se imnulteste

print('     L15: List')
print('         L15_44: Lsit - General Info')
# empty_list = []
# my_fruits = ['apple', 'banana', 'lime']
# posts_ids = [123, 3423, 588, 345]
# user_inputs = [True, 'Hi!', ':D', 10.5]
#
# other_fruits = ['banana', 'apple', 'lime']
#
# print(my_fruits == other_fruits)  # False
#
# print(len(empty_list))
# print(len(my_fruits))
# print(len(posts_ids))
# print(len(other_fruits))
#
# print(posts_ids[0])
# print(posts_ids[10]) # IndexError: list index out of range
# print(my_fruits[1])
# print(other_fruits[0])
# print(other_fruits[-1])
#
# posts_ids[0] = 1111  # schimbam valoarea primului element din lista
# posts_ids[3] = 4444
#
# print(posts_ids)
#
# del other_fruits[0]  # stergem primul element din lista 'other_fruits'
# print(other_fruits)
# print(len(other_fruits))

# users = [  # Lista de Dictionare
#     {
#         'user_id': 111,
#         'user_name': 'Andrew'
#
#     },
#     {
#         'user_id': 222,
#         'user_name': 'Alice'
#     }
# ]
#
# print(len(users))  # 2
# print(users[1]['user_id'])  # 222
# print(users[0]['user_name'])  # Andrew
#
# my_fruit1 = 'apple'
# my_fruit2 = 'orange'
# my_fruit3 = 'banana'
#
# all_fruits = [my_fruit1, my_fruit2, my_fruit3]
#
# print(all_fruits)

print('         L15_45: Methods list')

# happy_smiles = []
#
# happy_smiles.append(':)')
# happy_smiles.append(':D')
# happy_smiles.append(';)')
#
# print(happy_smiles)
# print(len(happy_smiles))
#
# u_inputs = [True, 'Hi!', ':D', 10.5]
#
# u_inputs.pop()  # se sterge ultimul element din lista
# print(u_inputs)
#
# u_inputs.pop(0)  # se ssterge elementul cu indexul '0'
# print(u_inputs)
#
# remove_element = u_inputs.pop()
#
# print(remove_element)
# print(u_inputs)
#
# list_ids = [123, 3423, 588, 345]
# list_ids.sort()  # Sorteaza crescator lista cu nr intregi
# print(list_ids)
#
# list_ids.sort(reverse=True) # Sorteaza descrescator lista cu nr intregi
# print(list_ids)

print('         L15_46: Operations with Lists')
# greeting_str = "Hello from Python"
# greeting_list = list(greeting_str)  # Operatia 'list' se face convertatsie string in listsa
# print(greeting_list)
#
# my_dict = {'a': 10, 'b': True}
# my_dict_keys = list(my_dict)  # Convertatsie dictionarului in lista
#
# print(my_dict_keys)
#
# ratings = [2.1, 3.4, 5.0, 7.3, 6.2, 3.2]
# print(max(ratings))
# print(min(ratings))
# print(sum(ratings))
#
# print(sum(ratings) / len(ratings))  # Valoarea Medie
#
# my_ratings = [1.2, 2]
# other_ratings = [3.2, 5.3, 7.4, 10]
#
# all_ratings = my_ratings + other_ratings
# print(all_ratings)
#
# first_two_ratings = ratings[:2] # taiem primele 2 elemente
# print(first_two_ratings)
#
# middle_ratings = ratings[1:-1] # taiem de la al doilea pina la ultimul element
# print(middle_ratings)
#
# last_two_ratings = ratings[-2:] # ultimele 2 elemete
# print(last_two_ratings)

print('         L15_47: Copy List')
# # Varianta 1
# my_cars = ['BMW', 'Mercedes']
# copied_cars = my_cars # copiem lista prin atribuire(dupa link)
#                       # (2 variabile se adreseaza la aceeeas lista din memorie)
# copied_cars.append('Audi')
# print(copied_cars)
# print(my_cars)
# print(id(my_cars) == id(copied_cars))
#
# # Varianta 2
# my_cars2 = ['BMW','Toyota']
# copied_cars2 = my_cars2[:] # se creaza lista noua in memorie (with slice)
# copied_cars2.append('Audi')
# print(copied_cars2)
# print(my_cars2)
# print(id(my_cars2) == id(copied_cars2))
#
# # Varianta 3
# my_cars3 = ['BMW','Toyota']
# copied_cars3 = my_cars3.copy() # Cu metoda '.copy()'
# copied_cars3.append('Audi')
# print(copied_cars3)
# print(my_cars3)
# print(id(my_cars3) == id(copied_cars3))
#
# # Varianta 4
# my_cars4 = ['BMW','Toyota']
# copied_cars4 = list(my_cars4)
# copied_cars4.append('Audi')
# print(copied_cars4)
# print(my_cars4)
# print(id(my_cars4) == id(copied_cars4))

print('         L15_48: Practice')
# my_nums = [10, 20, 30, 0, 40, 58]
# my_nums.insert(2, -10)
# print(my_nums)
# # my_nums.clear()
# # print(my_nums)
# my_nums.extend('abc')
# print(my_nums)

print('         L15_49: HomeWork')
# # 1 Creati o lista cu 5 elemente de diferite tipuri
# home_list = [True, 'Hi!', ':D', 10.5, 100]
# # 2 stergetsi elemtul al 3-lea
# del home_list[2]
# print(home_list)
# # 3 Afishazi lungeamea lsitei
# print(len(home_list))
# # 4 Schimbatsi ordinea in lista
# del home_list[0]
# home_list[0] = 101.1
# home_list.sort()
# print(home_list)
# # 5 Creati inca o lista cu 2 elemte
# other_home_list = [23, 56.8]
# # 6 extindeti prima lista cu elematele ai a 2 lista
# home_list.extend(other_home_list)
# # 7 afishatsi in terminal
# print(home_list)

print('     L16: Dictionary')
print('         L16_50: Dictionary dict')
# my_motorbyke = {
#     'brand': 'Ducati',
#     'price': 25000,
#     'engine_vol': 1.2
# }
# other_motorbyke = {
#     'price': 25000,
#     'engine_vol': 1.2,
#     'brand': 'Ducati'
# }
#
# print(my_motorbyke == other_motorbyke)  # Dictionarel sunt echivalente
# print(id(my_motorbyke) == id(other_motorbyke))  # dar au id-uri diferite

print('         L16_51: Edit and Delete values in dict')
# print(my_motorbyke['brand'])  # afisharea valorii din dictionara
# print(other_motorbyke['price'])
#
# my_motorbyke['price'] = 20000  # modificarea valorii
# print(my_motorbyke['price'])
# print(my_motorbyke)
#
# my_motorbyke['is_new_key'] = True  # adaugarea kaiei noua
# print(my_motorbyke)
#
# del my_motorbyke['is_new_key']  # stergerea keiei
# print(my_motorbyke)

print('         L16_52: Use varaibles in dict')
# key_name = 'brand'
# my_motorbyke[key_name] = 'BMW' # se modifica valoarea cu ajutorul variabilei
# print(my_motorbyke)
#
# my_motorbyke2 = {  # ex de dictonar care inculde alt dictionar
#     'brand': 'Ducati',
#     'engine_vol': 1.2,
#     'price_info': {
#         'price': 20000,
#         'is_avaible': True
#     }
# }
# print(my_motorbyke2['price_info']['price'])
# print(my_motorbyke2['price_info']['is_avaible'])
#
# # Crearea dictocarului cu ajutorul variabilor
# brand = 'Ducati'
# engine_vol = 1.2
# bike_price = 30000
#
# my_motorbyke3 = {
#     'brand':brand,
#     'price':bike_price,
#     'engine_volume':engine_vol
# }
# print(my_motorbyke3)
#
print('         L16_53: Lenght of the dict')
# print(len(my_motorbyke3)) # 3
#
print('      L16_54: Methode GET dict')
# # print(my_motorbyke['model']) # eraore si python opresete eexecutisa
# print(my_motorbyke.get('model')) # metoda .get nu opreste executia
# print(my_motorbyke.get('price'))

print('         L16_56-58: Practice')
# my_disk ={}
#
# print(id(my_disk))
# print(type(my_disk))
#
# my_disk['price'] = 70
# my_disk['brand'] = 'Samsung'
#
# print(my_disk)
# print(id(my_disk))
#
# print(my_disk.items())
# print(my_disk.keys())
# print(list(my_disk.keys()))
#
# new_disk = my_disk.copy() # copiem dictonarul
#
# new_disk['type'] = 'ssd' # adaugam o pereche noua
# print(my_disk)
# print(new_disk)
# print(len(my_disk))
#
# my_list = [['first',0], ['second',True]] # creem o lista din liste
# my_dict = dict(my_list) # Convertam lista in dictionar
# print(my_dict)

print('         L16_59: HomeWork')
#
# hw_cars = {}
#
# key_name1 = input("Enter key_name1: ")
# value1= input("Enter value1: ")
# hw_cars[key_name1] = value1
# key_name2 = input("Enter key_name2: ")
# value2= input("Enter value2: ")
# hw_cars[key_name2] = float(value2)
# key_name3 = input("Enter key_name3: ")
# value3= input("Enter value3: ")
# hw_cars[key_name3] = int(value3)
#
# print(hw_cars)
#
# hw_cars['add1key'] = 'sdkjfsjkda'
# print(hw_cars)
# del hw_cars['add1key']
# del hw_cars[key_name3]
# print(hw_cars)

print('     L17: Tuples(Кортежи)')
print('         L17_60: General')
# my_fruits = ('banana', 'apple', 'orange')  # exemplu de tuple
# # tilpe cum se creeaza asa si ramine nu se moade de modificat, de sters
# # de adugata elemente...tuple ramine neschimbat
# print(my_fruits)
# print(type(my_fruits))
#
# users = (  # creeam 3 dictionare in interiorul Kortedjilui Tuple
#     {
#         'user_id': 123,
#         'user_name': 'Andrew'
#     },
#     {
#         'user_id': 834,
#         'user_name': 'Vasile'
#     }
# )
#
# print(users[1]['user_id'])  # afisham valaore 'user_id' din dictionarul 2
# users[1]['user_id'] = 100  # modificam valoarea user_id din dictionar 2
# print(users[1]['user_id'])
#
# one_ids = (12, 23, 34)
# two_ids = (67, 89)
#
# all_ids = one_ids + two_ids # unirea a 2 tuples
# print(all_ids)

print('         L17_61: Tuples Methodes')

# users_ids = (23,34,13,45,566,78,689,23)
# print(users_ids.count(23)) # metoda count numara de cite ori se repete '23' in cortedj
# print(users_ids.count(78))
#
# print(users_ids.index(23))
# print(users_ids.index(689))
#
# tuple_ids = (12, 34)
#
# posts_ids_list = list(tuple_ids) # schimbam cortedjul in lista
# posts_ids_list.append(56) # adaugam in lista valoare noua cu metoda 'append'
#
# print(posts_ids_list) # afisham lista
#
# posts_ids_tuple = tuple(posts_ids_list) # cinvertam inapoi in kortedj
# print(posts_ids_tuple) # afisham cortedju

print('     L18: Set(Наборы)')
print('         L18_63: General')
# my_fruits = {'banana', 'apple', 'orange'}
# posts_ids = {342, 345, 345, 53745, 8567, 5795}
# users_inputs = {True, 'hi!', 10.5}
#
# print(my_fruits)
# print(type(my_fruits))
# print(posts_ids)  # valore care se repeta se sterg in Set ramin numai valori unicale
#
# other_fruits = {'apple', 'banana', 'orange'}
# print(my_fruits == other_fruits)  # True
# print(len(my_fruits))
# print(len(posts_ids))
# # print(posts_ids[0]) # eroare...Set nu are indexuri
#
print('         L18_65: Change objects in the set ')
# # list_set = {[1, 2], [23, 34]}  # eroare nu putem crea un set de liste

print('         L18_66: Practice Set ')
# photo_dimensuions = {'1920x1080', '800x600'}
# print(len(photo_dimensuions))
# # del photo_dimensuions[1] # eraore..set nu suporta operatiunea 'del'
# # exista alete metode dea sterge din set
# my_set = {10,10,5,15,15}
# print(my_set)
# print(len(my_set))
#
# my_set_tuple ={(10,10),5,15,15}
# print(my_set_tuple)
#
# my_set_empty = set() # creem un set gol(empty)
# print(my_set_empty)
# print(type(my_set_empty))

print('         L18_67: Methods of the Set ')
#
# photo_size = {'1920x1080', '800x600'}
# other_size = {'800x600', '1024x768'}
# photo_size.add('1024x768')
# all_size = photo_size.union(other_size)
# print(len(photo_size))
# print(photo_size)
# print(all_size)
# intersection_size = photo_size.intersection(other_size)
# print(intersection_size)
#
# nums = {10, 5, 35}
# others_nums = {20, 5, 12, 10, 35}
# res = nums.issubset(others_nums)
# print(res)
# res2 = others_nums.issuperset(nums)
# print(res2)
#
print('         L18_68-69:Practice Methods of the Set ')
#
# my_set = {'abc', 'd', 'f', 'y'}
# other_set = {'a', 'f', 'd'}
# print(my_set.intersection(other_set))
# print(my_set & other_set)  # aceeasi ca ".intersection"
# print(other_set.intersection(my_set))  # rezultat la fel
# print(my_set.union(other_set))
# print(my_set | other_set)  # aceeasi ca ".union"
# print(my_set.difference(other_set))
# print(my_set.discard('d'))  # Astfel se sterge elementul din Set(multsime)
# print(my_set)
# print(my_set.remove('abc'))
# print(my_set)
# copied_set = my_set.copy()
# my_set.add('t')
# copied_set.add('l')
# print(my_set)
# print(copied_set)
#
# print(my_set.symmetric_difference(copied_set))
#
# a = {'abc','d','f','y'}
# b = {'abc','d','f','l'}
#
# print(a.symmetric_difference(b))
# print((a | b) - (a & b)) # aceeashi cu operanzi
#
print('      L18_70: HomeWork')

# h_set = {10,20,30,40,50}
# h_set.add(35)
# print(h_set)
# h_other_set = {10,20,33,44,55}
# intersection_set = list(h_set.intersection(h_other_set))
# print(intersection_set)

print('     L19: Ranges(Диапазоны)')
print('         L19_71: General')
# my_range = range(7)
# print(type(my_range))
# print(my_range)
# print(list(my_range))
#
# my_range2 = range(10, 20, 2)  # a 3-lea valoare este pasul
# print(list(my_range2))
# print(my_range2[0])
# print(my_range2[1])
# print(my_range2[2])
# print(my_range2[3])
# print(my_range2[4])
# # print(my_range2[5]) # eroare indexul iese din diapazon
#
# # analagul cu ciclul for
# for n in my_range2:
#     print(n)
#
print('         L19_72: Practice')
# my_range3 = range(5)
#
# print(my_range3)
# print(type(my_range3))
# # print(my_range3[-1])
#
# # for n in my_range3:
# #     print(n)
#
# for n in range(12, 25, 5):  # pasil este 5
#     print(n)
#
# print(list(range(12, 25, 5)))  # convertatie diapazonului in Lista
# print(tuple(range(12, 25, 5)))  # convertatie diapazonului in Cortedj
# print(set(range(12, 25, 5)))  # convertatie diapazonului in Set(Multsime/nabor)
# print(my_range3.start)  # primim punctu de start la diapazon
# print(my_range3.stop) # primim sfirsitul diapazonului
# print(my_range3.step) # primim pasul diapazonului
#
# print(my_range3.index(0))
# print(my_range3.count(2))

print('     L20: Functsia Zip')
print('         L20_74: General')
# fruits = ['apple', 'banana', 'orange']
# quantities = [100, 80, 24]
# avaibility = [True, False, False]
#
# fruits_quantities_zip = zip(fruits, quantities, avaibility)  # unim cu Zip
# print(fruits_quantities_zip)
# fruits_quantities_zip = list(fruits_quantities_zip)
# print(fruits_quantities_zip)
#
print('         L20_75: Convertatsia Zip in Dict')
#
# fruits2 = ['apple', 'banana', 'orange']
# quantities2 = [100, 80, 24]
#
#
# fruits_quantities_zip2 = zip(fruits2, quantities2)  # unim cu Zip
# print(fruits_quantities_zip2)
# fruits_quantities_zip2 = dict(fruits_quantities_zip2)
# print(fruits_quantities_zip2)

print('     L21: Modificarea Obiectilor')
print('         L21_77: Comportamentul Obiectele care se modifica ')
#
# # Exemplu 1
# # my_list = [1, 2, 3]
# # print(id(my_list))
# # other_list = [1, 2, 3]
# # print(id(other_list))  # id diferite in memorie
# #
# # other_list.append(4)
# # print(my_list)
# # print(other_list)
# # print(id(other_list))  # id ramine ne schimbat cu adaugarea elementului nou
#
# # Exemplu 2
# info = { # dictionar
#     'name' : 'Bogdan',
#     'is_instructor':True
# }
# print(id(info))
#
# info_copy = info # In asa kaz copiem doar linkul spre memorie
# print(id(info_copy)) # rezulta ca au acealasi id
#
# info ['reviews_qty'] = 5 # adaugam o cheie noua in dictionar
# print(id(info)) # id ramine acelasi, se modifica obiectul in memorie
#
# print(info['reviews_qty'])      # acelasi valori 5 deaorece info_copy
# print(info_copy['reviews_qty']) # este doar linkul la obiect in memorie
#
# info_copy ['reviews_qty'] = 100 # deja cu ajutorul info_copy modificam obiectul
# # putem modific obiectul ori cu info ori cu info_copy
#
# print(info['reviews_qty']) # 100
# print(info_copy['reviews_qty']) # 100
#
# # exemplu 3
# my_info = {
#     'name' : 'Bogdan',
#     'is_instructor' : True
# }
#
# other_info = {
#     'name' : 'Bogdan',
#     'is_instructor' : True
# }
#
# print(id(my_info))    # la toate trei contsinul dictionarului este la fel
# print(id(other_info)) # dar id sunt diferite, respectiv se creaza 3
# print(id(info))       # obiecte in memorie
#
# # !!! Dupa copiere Obiectului care se modifica, Modificarile au loc
# # pentru toate copiile !!!

print('         L21_78: Cum sa evitam modificarea copiilor')
# # Varianta 1
#
# info = {
#     'name' : 'Bogdan',
#     'is_instructor' : True
# }
#
# info_copy = info.copy() # Folosim metoda 'copy()'
# info_copy['keie_noua'] = 5
# print(info)
# print(info_copy) # Modifcarile sau produs numai in inf0_copy
# print(id(info))
# print(id(info_copy)) # Respectiv au id diferite
#
# # Varianta 2
#
# info2 = {
#     'name' : 'Bogdan',
#     'is_instructor' : True,
#     'reviews' : []
# }
#
# info_copy2 = info2.copy()
# info_copy2['reviews'].append('Great course!')
#
# print(info2)      # se modifica si originalul de oarece contine cimp
# print(info_copy2) # cu keie de tip obiect care se modifica
#
# print(id(info2))
# print(id(info_copy2)) # dar id-rile sunt diferite!!!
#
# # rezolvarea problemei Varianta 3
#
# from copy import deepcopy
#
# info3 = {
#     'name' : 'Bogdan',
#     'is_instructor' : True,
#     'reviews' : []
# }
#
# info_copy3 = deepcopy(info3) # varianta 3 pentru a crea copie unicale
# info_copy3['reviews'].append('Great course!')
#
# print(info3)
# print(info_copy3)
#
# print(id(info3))
# print(id(info_copy3))

print('         L21_79: Peactica')
#
# from copy import deepcopy
#
# info_practica = {
#     'name' : 'Bogdan',
#     'is_instructor' : True,
#     'reviews' : []
# }
#
# info_copy_practica = deepcopy(info_practica) # varianta 3 pentru a crea copie unicale
# info_copy_practica['reviews'].append('Great course!')
# info_copy_practica['reviews'].append('Super!')
# info_practica['reviews'].append('Super2!')
#
# print(info_practica)
# print(info_copy_practica)
#
# print(id(info_practica))
# print(id(info_copy_practica))

print('     L22: Functii')
print('         L22_80: General')
#
#
# def sum(a, b):
#     c = a + b
#     print(c)
#
#
# a = 3
# b = 8
# sum(a, b)
# sum(23, 24)
# print(type(sum))  # calasa function
#
#
# def my_function(a, b):
#     a = a + 1
#     c = a + b
#     return c
#
#
# res = my_function(12, 3)
# print(res)

print('         L22_81: functia pass, cea mai scurta functie')
#
#
# def my_fn():
#     pass
#

# print(my_fn())
#
print('         L22_82: Transmiterea obiectelor nemodificabile in functie')
#
#
# def my_fun(a, b):
#     a = a + 1
#     c = a + b
#     print(id(a))
#     print(id(b))
#     return c
#
#
# num_one = 10
# num_two = 5
#
# res = my_fun(num_one, num_two)
# print(res)
# print(num_one)
# print(id(num_one))
# print(id(num_two))
#
print('         L22_83: Transmiterea obiectelor modificabile in functie')
#
#
# def increase_persone_age(person):
#     print(id(person))
#     person['age'] += 1
#     return person
#
#
# person_one = {
#     'name': 'Andrew',
#     'age': 36
# }
#
# print(id(person_one))
#
# increase_persone_age(person_one)
# print(person_one['age'])

print('         L22_84: Crearea copiiei obiectului din Functie ')
#
#
# def increase_person_age(person):
#     person_copy = person.copy()  # creem copie obiectului 'person'
#     person_copy['age'] += 1
#     return person_copy
#
#
# person_one = {
#     'name': 'Bob',
#     'age': 3
# }
#
# new_person = increase_person_age(person_one)
# print(new_person['age'])
# print(person_one['age'])
#
print('         L22_85: HomeWork')
#
#
# def merge_lists_to_dict(list_a=[], list_b=[]):
#     zip_list_a_list_b = zip(list_a, list_b)
#     dict_list_a_list_b = dict(zip_list_a_list_b)
#     return dict_list_a_list_b
#
#
# fruits = ['apple', 'banana', 'orange']
# quantities = [100, 80, 20]
# avaibility = [True, False, False]
#
# fruits_quantities_dict = merge_lists_to_dict(fruits, quantities)
# print(fruits_quantities_dict)
#
# quantities_avaibility_dict = merge_lists_to_dict(quantities, avaibility)
# print(quantities_avaibility_dict)
#
# fruits_avaibility_dict = merge_lists_to_dict(fruits, avaibility)
# print(fruits_avaibility_dict)

print('     L23: Argumnetele Functiei')
print('         L23_87: Unim argumentele in Tuple(kortedj)')
#
#
# # Ex.1
# def sum_nums(*args):
#     print(args)
#     print(type(args))
#     print(args[0])
#     return sum(args)  # 'sum' - functie integrata in Python
#
#
# print(sum_nums(2, 3, 7, 9))
#
#
# # Ex.2
# def get_post_info(name, posts_qty):
#     info = f"{name} vorbeste {posts_qty} de cuvinte"  # f"" - f rinduri
#     return info
#
#
# info = get_post_info('Andrew', 45)
# print(info)
#
print('         L23_88: Argumente cu cuvinte-cheie')
#
#
# def get_post_info2(name, posts_qty):
#     info2 = f"{name} vorbeste {posts_qty} de cuvinte"
#     return info2
#
#
# info2 = get_post_info(name='Andrew', posts_qty=45) # argumrntr cuvinte-cheie
# print(info2)

print('         L23_89: Unim argumentele in Dictionar')
#
#
# # EX.1
# def get_posts_info(**person):  # operator ** unidrtr srgurmtrlr in dict
#     print(person)
#     print(type(person))
#     info = (
#         f"{person['name']} vorbeste "
#         f"{person['posts_qty']} cuvinte"
#     )
#     return info
#
#
# info = get_posts_info(name='Andrew', posts_qty=25)
# print(info)
#
#
# # EX.2
#
# def get_posts_info2(**person):  # operator ** unidrtr srgurmtrlr in dict
#     print(person)
#     info2 = f"{person['name2']} vorbeste {person['posts_qty2']} cuvinte "
#     return info2
#
#
# info2 = get_posts_info2(posts_qty2=30, name2='Andrew',id=1231)
# print(info2)

print('     L24: Parametrii Functiei Default')
print('         L24_91-92: Valorile Parametrii Functiei Default & Practice')
#
#
# # Exemplu 1
# def mult_by_factor(value, multipler=1):  # po defaultu multipler are vaoloarea 1
#     return value * multipler
#
#
# print(mult_by_factor(10, 2))  # dam valoare 2
# print(mult_by_factor(5))
#
# # Exemplu 2
# from datetime import date
#
#
# def get_weekday():
#     return date.today().strftime('%A')
#
#
# def create_new_post(post, weekday=get_weekday()):
#     post_copy = post.copy()
#     post_copy['created_on_weekday'] = weekday
#     return post_copy
#
# initial_post = {
#     'id' : 243,
#     'author':'Andrew'
# }
#
# post_with_weekday = create_new_post(initial_post)
#
# print(post_with_weekday)
# print(initial_post)
#

print('     L25: CallBack Functiei')
print('         L25_93-94: General & Practice')
#
#
# def other_fn():
#     # someting operation...
#     pass
#
#
# def fn_with_callback(callback_fn):
#     callback_fn()
#
#
# fn_with_callback(other_fn)  # aici nu chemam functia 'otehr_fn'
#
#
# # dar trasnmite numele functiei
#
# # Ex.1
# #
# # def print_nummber_info(num):
# #     if (num % 2) == 0:
# #         print("Entered number is even")
# #     else:
# #         print("Entered number is odd")
# #
# #
# # def print_square_num(num):
# #     print("Square of the num is:", num * num)
# #
# # def process_number(num, callback_fn):
# #     callback_fn(num)
# #
# #
# # entered_num = int(input('Enter any number: '))
# #
# # process_number(entered_num, print_nummber_info)
# #
# # process_number(entered_num, print_square_num)
#
# # Ex.2 generalizat
#
# def send_data(data):
#     # seding data to the remote server...
#     pass
#
#
# def process_data(input_data, send_data_fn):
#     update_data = input_data.copy()
#     # actiuni cu update_data
#     send_data_fn(update_data)
#
#
# process_data({'name':'Andrew'}, send_data)

print('     L26: Cum sa lucram cu Functiile')
print('         L26_96: Documnetatsia Functiilor')
#
#
# # Ex.1
# def mult_by_factor(value, mult=1):
#     """Multiplicam nr cu multiplicator"""
#     return value * mult
#
#
# print(mult_by_factor(5, 5))
#
#
# # EX.2
#
# def print_number_info(num):
#     """
#     Controlam daac numarul este impar sau par
#
#     :param num:int
#     :return:Par sau Impar
#     """
#
#     if (num % 2) == 0:
#         print("Numarul este par")
#     else:
#         print("Numarul este impar")
#
#     return num
#
#
# print_number_info(30)

print('         L26_97: Zonile Vizible al variabilor din Functii')
# Ex.1
# a = 10  # Variabila Globala
#
#
# def my_fn():
#     a = True  # Variabila locala in functia "my_fn"
#     b = 15
#     print(a)
#     print(b)
#
#
# my_fn()
#
# print(a)
# print(b)  # NameError: name 'b' is not defined

# Ex.2
#
# a2 = 5
#
#
# def my_fn2():
#     def inner_fn():
#         print(a2)  # 5
#
#     inner_fn()
#
#
# my_fn2()

print('         L26_98: Ciclu de viatsa a variabelor')
# # Ex.1
# a = 10  # 1.Se declara variabila a si se atribuie valoara 10
#
#
# def my_fn():
#     a = True  # 3. Se declara variabila locala "a" si ii
#     b = 15    #    se atribuie valoarea 'True'
#     print(a)  # 4. Se controleaza daca este declarata variabila
#     print(b)  #    'a' in cadrul functiei si se afisheaza valoarea ei
#
#
# my_fn() # 2. Se cheama functaia "my_fn()"
#
# print(a) # 4. Se controleaza daca este declarata variabila
#          #    'a' in zona globala si se afisheaza valoarea ei
#
# print(b) # NameError: name 'b' is not defined

print('         L25_99: Cuvint cheie "Global" in cadrul functiei')
# # Ex.1
#
# def my_fn():
#     global a  # cu ajutorul cuvintului 'global' creeam variabila 'a'care va fi globala
#     a = 10
#
#
# my_fn()
#
# print(a)
#
# # Ex.1
#
# a2 = 12
#
#
# def my_fn2():
#    global a2
#    a2 = 14
#
# my_fn2()
#
# print(a2)

print('         L26_100: Practice ')
# # ex.1
# c = 5
#
#
# def my_fn(a, b):
#     d = 10
#     print(c)
#     print(a, b)
#
#
# print(dir())  # in afara functiem chemam functia dir, aflam variabile
# # globale
#
# # ex.2
#
# c1 = 5
#
#
# def my_fn2(a, b):
#     d = 10
#     print(c)
#     print(a, b)
#     print(dir()) #Aflam variabile din cadrul functiei
#
# my_fn2(3,5) #['a', 'b', 'd'] acestea sunt variabile din functie

print('     L27: Operatori')
print('         L27_101: General')

# a = 10
# b = a
#
# c = a + b
#
# print(a is b) #True
# print(c is b) #False

print('         L27_102: operatori si metodele magice')

# a = [1, 2]
# b = [1, 2]
#
# print(a == b) # operatorul egal, are analogul in metodele magice
# print(a.__eq__(b)) # operator magic

print('         L27_104: operatori binari si unari')

# my_num = 10
# print(+my_num)
#
# my_bool = True
# print(+my_bool)
#
# my_num2 = 9
# print(not my_num2)

print('         L27_105: operatori "in" si "not in"')

# my_car = {
#     'brand': 'Toyota',
#     'price': 10_000
# }
# print('brand' in my_car)
# print('year' in my_car)
# print('year' not in my_car)

print('         L27_107: HomeWork')

# my_fruits1 = {'banana', 'apple', 'orange'}
# my_fruits2 = {'apple', 'banana', 'orange'}
#
# var1 = my_fruits1
# var2 = my_fruits2
#
# print(var1 == var2)
# print(var1 is var2)
#
# print('apple' in var1)
# print('banana' in var2)

print('         L27_108: Valori False')

# print(bool(0))
# print(bool(0.0))
# print(bool(0j))
# print(bool(None))
# print(bool({}))
# print(bool([]))
# print(bool(()))
# print(bool(set()))
# print(bool(range(0)))
# print(bool(''))
#
# print(not not {}) # spoate in loc de functaie "bool"
#                   # sa folosim operantul "not not"

# my_list = [1,2]
#
# if len(my_list) > 0: # Astfel nu e acceptabil de scris
#     print("Lista are elemente")
# else:
#     print("Lista NU are elemente")
#
# if my_list: # Verianta acceptabila de scris, python automat controleaza daca e true
#     print("Lista are elemente")
# else:
#     print("Lista NU are elemente")

print('     L28: Operatori logici')
print('         L28_109-111: Operaturi de scurt-circuit "or" si "and"')
#
# my_list = [1,2]
# other_list = ['a','b']
# my_dict = {}
#
# my_dict1 = {
#     'a':5,
#     'b':4
# }
# my_dict2 = {
#     'b':4,
#     'a':5
# }
#
#
# print(my_list or other_list) # intorce prima valoare Adevarate '[1,2]'
# print(len(my_list)>0 or other_list) # Prima valoare este 'True'
# print(len(my_list)<0 or other_list) # ['a','b']
# print(my_list and other_list) # ['a','b']
#
# print(my_list and my_dict) # {} - dictionar gol
# print(bool(my_list and my_dict)) # False
#
# my_list and print("List is not empty!")
#
# print(len(my_dict1) and len(my_dict2))
# (my_dict1 and my_dict2) and print("Dictionary is equals")

print('     L29: Despachetarea dicționarelor')
print('         L29_112: Operatori de despachetare dictionarelor')
# grey_button = {
#     'width':200,
#     'text':'Buy',
#     'color':'grey'
# }
#
# red_button = {
#     **grey_button, # folosim operatorul de despachetare a dictionarului
#     'color':'red'
# }
#
# print(grey_button)
# print(red_button)

print('         L29_113: Unirea Dictionarilor')
# button_info = {
#     'text': 'Buy'
# }
# button_default = {
#     'text': 'Ok',
#     'color': 'black',
#     'width': 0,
#     'height': 0
# }
# button_style = {
#     'color': 'yellow',
#     'width': 200,
#     'height': 300
#
# }
#
# new_button = {
#     **button_info,
#     **button_style
# }
#
# new_button2 = button_info | button_style
#
# new_button3 = button_default | button_style
# rev_new_button3 = button_style | button_default
#
# print(new_button)
# print(new_button2)
# print(new_button3)
# print(rev_new_button3)

print('     L30: Инструкция del')
print('         L30_114: General')

# my_dict = {'a': True, 'b': 10}
# del my_dict['a']  # stergem element din dictionar cu instruciunea 'del'
# my_dict.__delitem__('b')  # instructiunea este la fel ca metoda magica '__delitem__'
# print(my_dict)
# print(my_dict.__delitem__)
#
# my_list = [1, 3]
# del my_list[0]  # stergem primul element din lista
# my_list.__delitem__(0)  # din nou stergem primul element din lista
# print(my_list)  # rezultat [] lista o sa fie goala


print('     L31: Concatenarea șirurilor')
print('         L31_115: General')

# h = 'Hello'
# w = 'World'
#
# greeting = h + ' ' + w
# print(greeting)

print('         L31_116: Formatarea șirurilor cu f-strings')

# h1 = 'Hello'
# w1 = 'World'
#
# greeting1 = f"{h1} {w1}"
#
# print(greeting)

print('         L31_117: Exersați unirea șirurilor folosind "+"')

# my_name = 'Andrew'
# my_hobby = 'Table Tennis'
# time = 18
#
# info = my_name + ' likes ' + my_hobby + ' at ' + str(time) + " o'clock."
#
# print(info)

print('         L31_118: Practica - f-strings')

# my_name1 = 'Andrew'
# my_hobby1 = 'Table Tennis'
# time1 = 18
#
# info1 = f"{my_name1} likes {my_hobby1} at {time} o'clock"
#
# print(info)

print('     L32: Funcții lambda')
print('         L32_119: General')

# def mult(a, b):
#     return a * b

# mult = lambda a, b: a * b # aicea trebuie definire a functie clasica
#
# print(mult(10, 3))

print('         L32_120: Pracica')
# Exemplu de folosire a functiei Lambda
# se foloseste cind avem nevoie dintro functoi
# sa intorcem alta functie, atunci se folosete Lambda functii


# def greeting(greet):
#     return lambda name: f"{greet},{name}!"
#
#
# morninig_greeting = greeting("Buna Dimineatsa")
# print(morninig_greeting(' Andrew!!!'))
#
# evening_greeting = greeting("Buna Seara")
# print(evening_greeting(' Anastasia!!!'))
#
# # Aceeasi functie fara lambda! folosim functie clasica
#
#
# def greeting1(greet):
#     def info(name):
#         return f"{greet},{name}!"
#     return info
#
#
# morninig_greeting1 = greeting1("Buna Dimineatsa")
# print(morninig_greeting1(' Andrew!!!'))
#
# evening_greeting1 = greeting1("Buna Seara")
# print(evening_greeting1(' Anastasia!!!'))

print('     L33: Prelucrarea Erorilor')
print('         L33_121: General')
#
# try:
#     print(10 / 0)  # eroare ZeroDivisionError
# except ZeroDivisionError:
#     print(ZeroDivisionError)
#     print("Eroare - Impartirea la zero")
#
# print('Continue...')

print('         L33_122: Obtinera informatieie despre Eroare')

# try:
#     print(10 / 0)  # eroare ZeroDivisionError
# except ZeroDivisionError as e:
#     print(type(e))
#     print(dir(e))
#     print(e)
#
# print('Continue...')

print('         L33_123: Diferite tipuri de Erori in blocul try')

# try:
#     print(10 / 0)
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
#
# print('Continue...')

print('         L33_124: Blocuri "else" si "finally"')

# try:
#     print(10 / 2)
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# else:
#     print("There was no error!!!")
# finally:
#     print('Continue...')

print('         L33_125: Fără tip de eroare și clasa Exception')

# # V1
# try:
#     print(10 / 0)
#     # print(10/'a')
# except Exception as e:
#     print(type(e))
#     print(e)
#
# # V2 nu se recomnda de folosit V2
# try:
#     print(10 / 0)
# except:
#     print("A aparut oaricare eroare")
#
# print('Continue...')

print('         L33_126: Crearea Erorilor')
#
#
# def divide_nums(a, b):
#     if b == 0:
#         raise ValueError("Second argument can't be 0!!!")
#     return print(a / b)
#
#
# try:
#     divide_nums(10, 0)
# except ValueError as e:
#     print(e)
#
# print('Continue...')

print('         L33_127: HomeWork')

# image_id = 234
# image_title = 'Andrew'
#
# image_info = f"Image {image_title} has id {image_id}"
# print(image_info)

print('     L34: Распаковка списков и кортежеи')
print('         L34_128: General')

# # my_fruits = ['apple', 'banana', 'lime']
# #
# # my_apple = my_fruits[0]  # metoda clasa de atribuire
# # my_banana = my_fruits[1]
# # my_lime = my_fruits[2]
# #
# # print(my_apple)
# # print(my_banana)
# # print(my_lime)
#
# my_list = [1, 2, 3]
#
# first, second, third = my_list
#
# print(first)
# print(second)
# print(third)
#
# my_fruits_t = ('apple', 'banana', 'lime')  # deja nu lista dar tuple
#
# my_apple_t, my_banana_t, my_lime_t = my_fruits_t
#
# print(my_apple_t)
# print(my_banana_t)
# print(my_lime_t)
#
# my_fruits = ['apple', 'banana', 'lime']
#
# my_apple, *remaning_fruits = my_fruits
#
# print(my_apple)
# print(remaning_fruits)
#
# print(type(remaning_fruits))

print('         L34_129: Распаковка словаря в именованые аргументы')

# user_profile = {
#     'name':'Andrew',
#     'comments_qty':12,
# }
#
# def user_info(name, comments_qty=0):
#     if not comments_qty:
#         return f"{name} has no comments"
#
#     return f"{name} has {comments_qty} comments"
#
#
# print(user_info(**user_profile)) # '**' raspakovka dictionarului

print('         L34_130: Распаковка списка в позиционные аргументы')
# # Exemplu 1
# user_data = ['Andrew', 37]
#
#
# def user_info(name, comments_qty):
#     if not comments_qty:
#         return f"{name} has no comments"
#
#     return f"{name} has {comments_qty} comments"
#
#
# my_name, my_comments_qty = user_data  # raspakovka listei in variabile
#
# print(user_info(my_name, my_comments_qty))
#
# # print(user_info(*user_data)) # '*' raspakovka listei

print('     L35: Условные инструкции')
print('         L35_132: Инструкция if')
# # Exemplu1
# number = 37
#
# if number > 0:
#     print(number, "is positive number")
#
# # Exemplu 2
# person_info = {
#     'name': 'Andrew',
#     'age': 20
# }
#
# if not person_info.get('name'):
#     print("Numele lipseste!")
# else:
#     print("numele este", person_info.get('name'))
#
# # Exemplu 3
#
# num_one = 10
# num_two = 5
#
# if (num_one > 0 and num_two > 0 and
#         isinstance(num_one, int) and isinstance(num_two, int)):
#     print("Ambele numere sunt intregi si pozitive")
# else:
#     print("Erore")
#
print('         L35_133: Инструкция if else')
# # Exemplu 1
# my_number = 22.4
#
# if type(my_number) is int:
#     print(type(my_number), my_number, "is integer")
# else:
#     print(type(my_number), my_number, "is not an integer")
#
# # Exemplu 2
#
# my_phone = {
#     'price': 300,
#     'brand': 'Motorola'
# }
#
# if my_phone.get('brand'):
#     print("Phone's brand is", my_phone['brand'])
# else:
#     print("There is no phone brand")

print('         L35_134: Инструкция if elif')

# n = -10
#
# if n > 0:
#     print(n, "is positive number")
# elif n < 0:
#     print(n, "is negative number")
# else:
#     print(n, "is zero")

print('         L35_135: Использование if в функциях')

#
# # Varianta 1 cea mai reusita
#
# def nums_info(a, b):
#     if (type(a) is not int) or (type(b) is not int):
#         return "Unul din argumente nu e cifra intreaga"
#
#     if a > b:
#         return f"{a} este mai mare ca {b}"
#
#     if a < b:
#         return f"{a} este mai mic ca {b}"
#
#     return f"Ambele numere sunt egale cu {a}"
#
#
# # Varianta 2 de functie cu elif si else
# # def nums_info(a, b):
# #     if (type(a) is not int) or (type(b) is not int):
# #         info =  "Unul din argumente nu e cifra intreaga"
# #     elif a > b:
# #         info = f"{a} este mai mare ca {b}"
# #     elif a < b:
# #         info = f"{a} este mai mic ca {b}"
# #     else:
# #         info = f"Ambele numere sunt egale cu {a}"
# #     return info
#
#
# print(nums_info(True, 10))
# print(nums_info(10, 2))
# print(nums_info(-10, -3))
# print(nums_info(2, 6))
# print(nums_info(3, 3))

print('         L35_136: HomeWork')

# car_info = {
#     'distance': 100,
#     'speed': 40,
#     'time': 0
#
# }
#
#
# def route_info(**a):
#     if (a.get('distance')) and (type(a.get('distance')) is int):
#         return f"Distance to your destination is {a['distance']}"
#
#     if (a.get('speed')) and (a.get('time')):
#         return f"Distance to your destination is {a['speed'] * a['time']}"
#
#     return f"No distance info is avaibale"
#
#
# print(route_info(**car_info))
