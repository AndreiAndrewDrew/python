print("Ex.1")
c = 7  # variabila globala


def my_fn(a, b):
    d = 8
    c = 10
    print("Variabila locala 'c':", c)
    print("Variabilele laocale 'a','b':", a, b)


my_fn(12, 14)
print("Variabila globala 'c':", c)
print("Variabile globale:", dir())  # In afara functiei chemam functia dir, aflam variabile globale

print("Ex.2")

c1 = 5


def my_fn2(a, b):
    d = 10
    print("Variabila globala 'c1':", c1)
    print("Variabilele laocale 'a','b':", a, b)
    print("Variabile locale:", dir())  # Aflam variabile din cadrul functiei
    # ['a', 'b', 'd'] acestea sunt variabile din functie


my_fn2(3, 5)
