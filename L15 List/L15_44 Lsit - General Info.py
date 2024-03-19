empty_list = []
my_fruits = ['apple', 'banana', 'lime']
posts_ids = [123, 3423, 588, 345]
user_inputs = [True, 'Hi!', ':D', 10.5]

other_fruits = ['banana', 'apple', 'lime']

print(my_fruits == other_fruits)  # False

print(len(empty_list))
print(len(my_fruits))
print(len(posts_ids))
print(len(other_fruits))

print(posts_ids[0])
# print(posts_ids[10]) # IndexError: list index out of range
print(my_fruits[1])
print(other_fruits[0])
print(other_fruits[-1])

posts_ids[0] = 1111  # schimbam valoarea primului element din lista
posts_ids[3] = 4444

print(posts_ids)

del other_fruits[0]  # stergem primul element din lista 'other_fruits'
print(other_fruits)
print(len(other_fruits))

users = [  # Lista de Dictionare
    {
        'user_id': 111,
        'user_name': 'Andrew'

    },
    {
        'user_id': 222,
        'user_name': 'Alice'
    }
]

print(len(users))  # 2
print(users[1]['user_id'])  # 222
print(users[0]['user_name'])  # Andrew

my_fruit1 = 'apple'
my_fruit2 = 'orange'
my_fruit3 = 'banana'

all_fruits = [my_fruit1, my_fruit2, my_fruit3]

print(all_fruits)