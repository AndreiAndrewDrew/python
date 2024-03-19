print("Ex.1")
def get_posts_info(**person):  # operator '**' uneste argumentele in dictionar
    print("Afisham Dict:", person)
    print("Tipul",type(person))
    info = (
        f"{person['name']} vorbeste "
        f"{person['posts_qty']} cuvinte"
    )
    return info


info = get_posts_info(name='Andrew', posts_qty=25)
print(info)


print("Ex.2")

def get_posts_info2(**person):  # operator '**' uneste argumentele in dictionar
    print("Afisham Dict:", person)
    info2 = f"{person['name2']} vorbeste {person['posts_qty2']} cuvinte "
    return info2


info2 = get_posts_info2(posts_qty2=30, name2='Andrew', id=1231)
print(info2)
