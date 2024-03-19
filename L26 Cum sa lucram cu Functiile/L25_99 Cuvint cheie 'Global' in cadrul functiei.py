def my_fn():
    global a  # cu ajutorul cuvintului 'global' creeam variabila 'a'
    # care va fi globala
    a = 10


my_fn()

print("Variabila globala 'a':", a)

a2 = 12


def my_fn2():
    global a2
    a2 = 14


my_fn2()

print("Variabila Globala 'a2:'", a2)
