# 'os' vs 'pathlib'
from os import path # functionalnii padhod

print(path.abspath('.'))  # folosim '.' sa gasim calea absoluta spre fisierul dat 'L45 Работа с фаилами'
print(type(path))           

from pathlib import Path # obiect- orientat padhod

print(Path('.').absolute())  # aceeeasi rezultat cu 'pathlib'
print(type(Path))
