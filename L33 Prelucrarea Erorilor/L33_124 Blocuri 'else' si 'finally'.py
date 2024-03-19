try:
    print(10 / 2)
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print("There was no error!!!")
finally:
    print('Continue...')
