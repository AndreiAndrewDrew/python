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
print(my_motorbyke)
print(other_motorbyke)
print("Dictionarile sunt echivalente?-", my_motorbyke == other_motorbyke)  # True - Dictionarel sunt echivalente
print("Id-rile sunt egale?-", id(my_motorbyke) == id(other_motorbyke))  # False - Dar au id-uri diferite
