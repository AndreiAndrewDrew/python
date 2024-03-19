class Car:
    def move(self):
        print("Car is moving!")

    def stop(self):
        print("Car is stopped!")


my_car = Car()  # Chemam functia constructor, 'my_car' este un exemplear clasei 'Car'
print(my_car)
print(type(my_car))
print("Controlam daca 'my_car' este exemplear din clasa 'Car':")
print(isinstance(my_car, Car))
print("Controlam daca 'my_car' este exemplear din clasa 'object':")
print(isinstance(my_car, object))

print(dir(my_car))  # Conrolom toate atributile moshtenite clasei 'my_car' de la clasa 'Car'

print(my_car.__dict__)  # {} --> dictionar gol, rezulta ca 'my_car' nu are proprii atribute

my_car.move()  # chemam metoda 'move()'
Car.move(my_car)  # o alata forma de chemare a metodei 'move()'
my_car.stop()  # chemam metoda 'stop()'
my_car.stop()
my_car.move()  # Le chemam de cite ori dorim!

my_second_car = Car()

print(my_car == my_second_car)
print(id(my_car), id(my_second_car))
