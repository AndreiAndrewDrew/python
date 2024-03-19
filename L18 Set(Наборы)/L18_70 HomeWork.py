home_set = {10, 20, 30, 40, 50}
print("Multimea 'home_set':", home_set)
home_set.add(35)
print("S-a adugat elementu '35':", home_set)

home_other_set = {10, 20, 33, 44, 55}
print("Multimea 'home_other_set':", home_other_set)
intersection_set = list(home_set.intersection(home_other_set))
print("Intersectia Convertata in Lista:", intersection_set)

