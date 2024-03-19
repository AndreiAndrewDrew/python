my_set = {'abc', 'd', 'f', 'y'}
other_set = {'a', 'f', 'd'}
print("Multimea my_set=", my_set)
print("Multimea other_set=", other_set)
print("Interesctia=", my_set.intersection(other_set))
print("Interesctia=", my_set & other_set)  # aceeasi ca ".intersection"
print("Interesctia=", other_set.intersection(my_set))  # rezultat la fel

print("Unirea=", my_set.union(other_set))
print("Unirea=", my_set | other_set)  # aceeasi ca ".union"

print("Diferentsa=", my_set.difference(other_set))  # diferentsa

my_set.discard('d')  # Astfel se sterge elementul din Set(multsime)
print("Eliminam 'd' din my_set:", my_set)
my_set.remove('abc')  # La fel se sterge elemtul 'abc'
print("Eliminam 'abc' din my_set:", my_set)

copied_set = my_set.copy()
print("Copiem my_set in copied_set:", copied_set)
my_set.add('t')
copied_set.add('l')
print("Am adaugat 't' in my_set:", my_set)
print("Am adugat 'l' in copied_set:", copied_set)

print("Diferentsa simetrica 'my_set' si 'copied_set':", my_set.symmetric_difference(copied_set))

print("Exemplu 2 de diferentsa simetrica:")
a = {'abc', 'd', 'f', 'y'}
b = {'abc', 'd', 'f', 'l'}
print("Multimea 'a':",a)
print("Multimea 'b':",b)
print("Diferentsa simetrica 'a' si 'b':", a.symmetric_difference(b))
print("Diferentsa simetrica 'a' si 'b':", (a | b) - (a & b))  # aceeashi cu operanzi
