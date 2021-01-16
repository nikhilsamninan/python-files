from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def service(self):
        pass
class Bike(Vehicle):
    def service(self):
        print("bike servicing")
class Car(Vehicle):
    def service(self):
        print("car servicing")
b1 = Bike()
c1 = Car()
b1.service()
c1.service()