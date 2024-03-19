my_motorbyke = {
    'brand': 'Ducati',
    'price': 25000,
    'engine_vol': 1.2
}

# print(my_motorbyke['model']) # eraore- si python opresete eexecutisa
print(my_motorbyke.get('model'))  # metoda .get nu opreste executia
print(my_motorbyke.get('price'))
