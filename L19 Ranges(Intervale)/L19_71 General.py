my_range = range(7)
print(type(my_range))
print("Intervalul 'my_range':", my_range)
my_list = list(my_range)
print("Convertam 'my_range' in 'my_list':", my_list)

my_range2 = range(10, 20, 2)  # a 3-lea valoare este pasul
my_list2 = list(my_range2)
print("Convertam 'my_range2' in 'my_lista2':", my_list2)
print("Lungimea listei 'my_lista2':", len(my_list2))
print("Afisham fiecare element din lista:")
print(my_range2[0])
print(my_range2[1])
print(my_range2[2])
print(my_range2[3])
print(my_range2[4])
# print(my_range2[5]) # eroare indexul iese din diapazon

print("Analagul cu ciclul 'for':")
for n in my_range2:
    print(n)
