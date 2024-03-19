my_range3 = range(5)

print("Intervalul 'my_range3'", my_range3)
print(type(my_range3))
# print(my_range3[-1])

print("AFisham fiecare element din 'my_range3':")
for n in my_range3:
    print(n)

my_range4 = range(15, 30, 5)  # pasul este 5
print("Afisham fiecare element din 'my_range4':")
for n in my_range4:
    print(n)

print(list(my_range4))  # convertam Intervalul in Lista
print(tuple(my_range4))  # convertam Intervalul in Cortedj
print(set(my_range4))  # convertam Intervalul in Set(Multsime/nabor)

print("Primul element:", my_range4.start)  # primim punctu de start la interval
print("Ultimul element:", my_range4.stop)  # primim sfirsitul diapazonului
print("Pasul intervalului:", my_range4.step)  # primim pasul diapazonului

print("Aflam indexul elemntului '25':",my_range4.index(25))
print("Numaram cite elemnte de '20':",my_range4.count(20))
