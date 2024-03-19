a = 10  # 1.Se declara variabila a si se atribuie valoara 10


def my_fn():
    a = True  # 3. Se declara variabila locala "a" si ii
    b = 15    # se atribuie valoarea 'True'
    print(a)  # 4. Se controleaza daca este declarata variabila
    print(b)  # 'a' in cadrul functiei si se afisheaza valoarea ei


my_fn()  # 2. Se cheama functaia "my_fn()"

print(a)  # 4. Se controleaza daca este declarata variabila
#    'a' in zona globala si se afisheaza valoarea ei

# print(b) # NameError: name 'b' is not defined
