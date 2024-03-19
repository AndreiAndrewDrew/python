from pathlib import Path

# cwd = Path('.')
print(Path('.').cwd())  # Calea spre directoriei

print(Path('.'))  # '.'
print(isinstance(Path('.'), Path))  # True, 'cwd' este exemplear clasei 'Path'
print(type(Path('.')))  # <class 'pathlib.WindowsPath'>
print(Path.__subclasses__())

print(Path('.').absolute())  # calea absoluta a directoriei

print(Path('D:/').joinpath('1.Andrew Work').joinpath('3.Python').joinpath('1.PhytonProjects (2023)[Udemy]')
      .joinpath('python').joinpath('L45 Работа с фаилами'))
print(Path('D:/') / '1.Andrew Work' / '3.Python' / '1.PhytonProjects (2023)[Udemy]' / 'python' / 'L45 Работа с фаилами')

my_dir = (Path('D:/') / '1.Andrew Work' / '3.Python' / '1.PhytonProjects (2023)[Udemy]'
          / 'python' / 'L45 Работа с фаилами' / 'test mapa')

print("Controlam daca exista mapa 'test mapa':", my_dir.exists())

if not my_dir.exists():  # daca nu exista o creem
    print(my_dir.mkdir())  # creem mapa

if my_dir.exists():  # daca exista
    print(my_dir.rmdir())  # stergem mapa
