class Car:
    def move(self):
        print("Car is moving!")

    def stop(self):
        print("Car is stopped!")


my_car = Car()  # Chemam functia constructor, 'my_car' este un exemplear clasei 'Car'
print(type(my_car))
print(isinstance(my_car, Car))
my_car.move()
my_car.stop()
