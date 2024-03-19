print("Ex.1")


def sum_nums(*args):
    print("Afisham argumentele:", args)
    print("Tipul argumentelor:", type(args))
    print("Afisham primul argument:", args[0])
    return sum(args)  # 'sum' - functie integrata in Python


print("Afisham Suma:",sum_nums(2, 3, 7, 9))

print("Ex.2")


def get_post_info(name, posts_qty):
    info = f"{name} vorbeste {posts_qty} de cuvinte!"  # f"" - f rinduri
    return info


info = get_post_info('Andrew', 45)
print(info)
