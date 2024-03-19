# Exemplu 1
user_data = ['Andrew', 37]


def user_info(name, comments_qty):
    if not comments_qty:
        return f"{name} has no comments"

    return f"{name} has {comments_qty} comments"


my_name, my_comments_qty = user_data  # raspakovka listei in variabile

print(user_info(my_name, my_comments_qty))

print(user_info(*user_data)) # '*' raspakovka listei
