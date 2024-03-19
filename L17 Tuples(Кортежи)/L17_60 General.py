my_fruits = ('banana', 'apple', 'orange')  # exemplu de tuple
# tilpe cum se creeaza asa si ramine nu se poate de modificat, de sters
# de adugata elemente...tuple ramine neschimbat
print(my_fruits)
print(type(my_fruits))

users = (  # creeam 3 dictionare in interiorul Kortedjilui Tuple
    {
        'user_id': 123,
        'user_name': 'Andrew'
    },
    {
        'user_id': 834,
        'user_name': 'Vasile'
    }
)

print(users[1]['user_id'])  # afisham valaore 'user_id' din dictionarul 2
users[1]['user_id'] = 100  # modificam valoarea user_id din dictionar 2
print(users[1]['user_id'])

one_ids = (102, 83, 34)
two_ids = (67, 89)
all_ids = one_ids + two_ids  # unirea a 2 tuples
print(all_ids)
