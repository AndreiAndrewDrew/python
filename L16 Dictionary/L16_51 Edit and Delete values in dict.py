my_motorbyke = {
    'brand': 'Ducati',
    'price': 25000,
    'engine_vol': 1.2
}
other_motorbyke = {
    'price': 25000,
    'engine_vol': 1.2,
    'brand': 'Ducati'
}

print(my_motorbyke['brand'])  # afisharea valorii din dictionara
print(other_motorbyke['price'])

my_motorbyke['price'] = 20000  # modificarea valorii
print(my_motorbyke['price'])
print(my_motorbyke)

my_motorbyke['is_new_key'] = True  # adaugarea kaiei noua
print(my_motorbyke)

del my_motorbyke['is_new_key']  # stergerea cheia 'is_new_key'
print(my_motorbyke)