# Exemplu de convertatie a json rind in dictionar
import json

json_str ='{"id":25, "brand": "Nike","qty":85,"status":{"isForSale":true}}'

sneakers = json.loads(json_str) # cu metoda 'loads' convertam 'json_str' rind in dictionar

print(type(sneakers))

print(sneakers) # Afisham tat dictionarul 'sneakers'
print(sneakers['brand'])
print(sneakers['qty'])
print(sneakers['status']['isForSale'])