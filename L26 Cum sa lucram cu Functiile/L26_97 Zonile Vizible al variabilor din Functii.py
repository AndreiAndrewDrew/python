print("Ex.1")
a = 10  # Variabila Globala


def my_fn():
    a = True  # Variabila locala in functia "my_fn"
    b = 15
    print("Variabila locala 'a':", a)
    print("Variabila locala 'b':", b)


my_fn()  # chemam functia

print("Variabila Globala 'a':", a)
# print(b)  # NameError: name 'b' is not defined

print("Ex.2")

a2 = 5


def my_fn2():
    def inner_fn():
        print("Variabila globala 'a2':", a2)  # 5
        # Variabile Globale se vad in functie, invers NU!
    inner_fn()


my_fn2()
