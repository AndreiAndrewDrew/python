import json

json_str = '{"id":25, "brand": "Nike","qty":85,"status":{"isForSale":true}}'
json_array = '[{"a":1},{"b":2}]'  # lista de dictionare !!! asa des vin datele de pe servere !!!

sneakers = json.loads(json_str)  # cu metoda 'loads' convertam 'json_str' rind in dictionar

print(sneakers)  # Afisham tat dictionarul 'sneakers'
print(type(sneakers))

my_list = json.loads(json_array)

print(my_list)
print(type(my_list))

json_from_dict = json.dumps(sneakers, indent=2)  # Convertam inapoi dict --> json
                                                 # parametru 'indent'- formateaza in format json
print(json_from_dict)
print(type(json_from_dict))  # <class 'str'>
