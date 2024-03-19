try:
    print(10 / 0)  # eroare ZeroDivisionError
except ZeroDivisionError as e:
    print(type(e))
    print(dir(e))
    print(e)

print('Continue...')