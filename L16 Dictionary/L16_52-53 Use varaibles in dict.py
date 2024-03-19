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

key_name = 'brand'
my_motorbyke[key_name] = 'BMW'  # se modifica valoarea cu ajutorul variabilei
print(my_motorbyke)

my_motorbyke2 = {  # ex de dictonar care inculde alt dictionar
    'brand': 'Ducati',
    'engine_vol': 1.2,
    'price_info': {
        'price': 20000,
        'is_avaible': True
    }
}
print(my_motorbyke2['price_info']['price'])
print(my_motorbyke2['price_info']['is_avaible'])

# Crearea dictocarului cu ajutorul variabilor
brand = 'Ducati'
engine_vol = 1.2
bike_price = 30000

my_motorbyke3 = {
    'brand': brand,
    'price': bike_price,
    'engine_volume': engine_vol
}
print(my_motorbyke3)

# L16_53: Lenght of the dict
print(len(my_motorbyke3)) # 3
