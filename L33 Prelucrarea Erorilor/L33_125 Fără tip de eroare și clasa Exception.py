# V1
try:
    print(10 / 0)
    # print(10/'a')
except Exception as e:
    print(type(e))
    print(e)

# V2 nu se recomnda de folosit V2
try:
    print(10 / 0)
except:
    print("A aparut oaricare eroare")

print('Continue...')