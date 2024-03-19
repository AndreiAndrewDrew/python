import random

print(random.random())  # [0,1) din intervalul acesta random, 1 nu se include
print(random.randint(1, 10))  # aici ii indicam intervalul [1,10]
print(random.choice('abcdef'))  # din str - random un caracter
print(random.choice([1, 20, 3, 40, 25]))  # din list - random un elemet
print(random.choices([1, 20, 3, 40, 25, 100, 4424, 234, 54345], k=3))  # random 3 elemnte din lista,
# obtinem alta lista din 3 elemente
my_list = [1, 20, 3, 40, 25]
random.shuffle(my_list)  # '.shuffle'(ro: amesteca) nu intoarce nimic, dar schimba ordinea in lista a elementelor
print(my_list)
random.shuffle(my_list)
print(my_list)

print(random.choices('0123456789', k=8)) # Obtinem lista din 8 elemente
print(''.join(random.choices('ABCDEF0123456789', k=8))) # astfel obtinem str, un rind