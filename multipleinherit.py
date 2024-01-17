from multipledispatch import dispatch

class Bike:
    def twoWheeler(self):
        print("Bike is two wheeler")

    @dispatch(int)
    def fourWheeler(self, a):
        print("Bike is four wheeler with {} wheels".format(a))

class Car:
    @dispatch(int)
    def fourWheeler(self, a):
        print("Car is the four wheeler with {} wheels".format(a))

class Truck:
    def eightWheeler(self):
        print("Truck is the eight Wheeler")

class Vehicle(Bike, Car, Truck):
    pass

b = Vehicle()

b.twoWheeler()
b.fourWheeler(4)
