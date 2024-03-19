import json

my_dict = {
    'str': 'Andrew',
    'a': 23,
    'c': 2.45,
    'd': True,
    2: 2,
    'bool': False
}

my_json = json.dumps(my_dict, indent=2)

print(my_json)
print(type(my_json))
