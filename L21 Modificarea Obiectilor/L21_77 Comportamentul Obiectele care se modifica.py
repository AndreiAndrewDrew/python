print("Exemplu 1")
my_list = [1, 2, 3]
print("Id listei 'my_list':", id(my_list))
other_list = [1, 2, 3]
print("Id listei 'other_list':", id(other_list))  # id diferite in memorie

other_list.append(4)
print("my_list:", my_list)
print("other_list:", other_list)
print("Id listei 'other_list':", id(other_list))  # id ramine ne schimbat cu adaugarea elementului nou

print("Exemplu 2")
info = {  # dictionar
    'name': 'Bogdan',
    'is_instructor': True
}
print("Id dict 'info':", id(info))

info_copy = info  # Astfel copiem doar linkul spre memorie
print("Id dict 'info_copy'", id(info_copy))  # rezulta ca au acealasi id

info['reviews_qty'] = 5  # adaugam o cheie noua in dictionar
print("Id dict 'info'", id(info))  # id ramine acelasi, se modifica obiectul in memorie

print("Valoare cheiei 'reviews_qty' din 'info':", info['reviews_qty'])  # acelasi valori 5 deaorece info_copy
print("Valoare cheiei 'reviews_qty' din 'info_copy':",
      info_copy['reviews_qty'])  # este doar linkul la obiect in memorie

info_copy['reviews_qty'] = 100  # deja cu ajutorul info_copy modificam obiectul
# putem modific obiectul ori cu info ori cu info_copy

print("Valoare cheiei 'reviews_qty' din 'info':", info['reviews_qty'])  # 100
print("Valoare cheiei 'reviews_qty' din 'info_copy':",info_copy['reviews_qty'])  # 100

print("Exemplu 3")
my_info = {
    'name': 'Bogdan',
    'is_instructor': True
}

other_info = {
    'name': 'Bogdan',
    'is_instructor': True
}

print(id(my_info))  # la toate trei contsinul dictionarului este la fel
print(id(other_info))  # dar id sunt diferite, respectiv se creaza 3
print(id(info))  # obiecte in memorie

# !!! Dupa copiere Obiectului care se modifica, Modificarile au loc
# pentru toate copiile !!!
