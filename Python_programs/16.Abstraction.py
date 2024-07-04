from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Bike(Vehicle):
    def intro(self):
        print("This is a bike")

    def start(self):
        print("Bike starts")

    def stop(self):
        print("Bike stops")

obj_abs = Vehicle()
obj = Bike()
obj.intro()
obj.start()
obj.stop()