print("Ex.1")
number = 37

if number > 0:
    print(number, "is positive number")

print("Ex.2")
person_info = {
    'name': 'Andrew',
    'age': 20
}

if not person_info.get('name'):
    print("Numele lipseste!")
else:
    print("Numele este", person_info.get('name'))

print("Ex.3")

num_one = 10
num_two = 5

if (num_one > 0 and num_two > 0 and
        isinstance(num_one, int) and isinstance(num_two, int)):
    print("Ambele numere sunt intregi si pozitive")
else:
    print("Erore")
