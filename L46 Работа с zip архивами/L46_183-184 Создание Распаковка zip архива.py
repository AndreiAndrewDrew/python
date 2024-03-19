from zipfile import ZipFile
from pathlib import Path

if not Path('my-files').exists():  # daca nu exista o creem
    Path('my-files').mkdir()  # creem mapa 'my-files'

with open('my-files/first.txt', 'w') as my_file:  # creem in mapa 'my-files' fisierul 'first.txt'
    my_file.write("This is First file")

with open('my-files/second.txt', 'w') as my_file:  # creem in mapa 'my-files' fisierul 'first.txt'
    my_file.write("This is Second file")

with ZipFile('my-files.zip', 'w') as my_zip_file:  # creem zip fisierul 'my-files.zip'
    print(my_zip_file)
    for file in Path('my-files').iterdir():  # iteratii pe directorie
        print(file)
        my_zip_file.write(file)  # inscriem fisierele in 'my_files.zip'

with ZipFile('my-files.zip') as my_zip_file:  # Extragem totul din 'my-files.zip'
    my_zip_file.extractall('my-files-unzipped') # Se extrage in mapa 'my-files-unzipped'

with ZipFile('my-files.zip') as my_zip_file:
    print(my_zip_file.infolist()) # Info despre fiecare fisier din arhiv