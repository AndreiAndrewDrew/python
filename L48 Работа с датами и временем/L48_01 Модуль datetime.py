from datetime import date
from datetime import time
from datetime import datetime

my_date = date(2025, 3, 12)
my_time = time(18,23,34)
my_datetime = datetime( 2027,7,24,16,34,54)

print(my_date)
print(my_time)
print(my_datetime)

print(my_date.day)
print(my_date.month)
print(my_date.year)

print(my_time.hour)

print(my_datetime.year)
print(my_datetime.microsecond)

print(my_date.isocalendar())
print(my_time.isoformat())
print(my_datetime.isoformat())
print(my_datetime.now())
print(my_datetime.now().second)

