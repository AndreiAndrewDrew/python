from datetime import datetime, timedelta

my_datetime = datetime(2027, 7, 24, 16, 34, 54)

print(timedelta)
print(my_datetime)
print(my_datetime + timedelta())
print(my_datetime + timedelta(days=100)) # +100 de zile
print(my_datetime + timedelta(days=100, minutes=400)) # +100 de zile + 400 minute

