print("Exemplu 1. Pentru Multsimi")
my_set = {1, 3, 4, 8}

new_set = set()

for val in my_set:
    new_set.add(val * val)  # Cu 'for in' obishnuit

new_set2 = {val * val for val in my_set}  # Cu 'for in' redus

print(my_set)
print(new_set)
print(new_set2)

print("Exemplu 2. Pentru Dictionare")

my_scores = {
    'a': 10,
    'b': 20,
    'c': 30
}

new_scores = {}

for key, value in my_scores.items():  # Cu 'for in' obishnuit
    new_scores[key] = value * 2

new_scores2 = {key: value * 2 for key, value in my_scores.items()}  # Cu 'for in' redus

print(my_scores)
print(new_scores)
print(new_scores2)

