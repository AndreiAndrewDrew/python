users_ids = (23, 34, 13, 45, 566, 78, 689, 23)
print(users_ids.count(23))  # metoda count numara de cite ori se repete '23' in cortedj
print(users_ids.count(78))

print(users_ids.index(23))
print(users_ids.index(689))

tuple_ids = (12, 34)

posts_ids_list = list(tuple_ids)  # convertam cortedjul in lista
posts_ids_list.append(56)  # adaugam in lista valoare noua cu metoda 'append'
print(posts_ids_list)  # afisham lista

posts_ids_tuple = tuple(posts_ids_list)  # convertam inapoi in kortedj
print(posts_ids_tuple)  # afisham cortedju
