print("Ex.1")


def mult_by_factor(value, multipler=1):  # po default-u multipler are vaoloarea 1
    return value * multipler


print(mult_by_factor(10, 2))  # dam valoare 2
print(mult_by_factor(5))

print("Ex.2")
from datetime import date


def get_weekday():  # Functia intoarce ziua saptaminii
    return date.today().strftime('%A')


def create_new_post(post, weekday=get_weekday()): # 'weekday' o sa aiba valaorea po defaultu, rezultatul functiei 'get_weekday()'
    post_copy = post.copy() # facem copie la argumentul dict post
    post_copy['created_on_weekday'] = weekday # adaugam un cimp nou cu valoare
    return post_copy


initial_post = { # dictionarul initial_post
    'id': 243,
    'author': 'Andrew'
}

post_with_weekday = create_new_post(initial_post)

print("Postul creat cu ziua saptaminii:", post_with_weekday)
print("Postul initsial", initial_post)
