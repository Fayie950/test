# Base class
class Vehicle:
    def start(self):
        return "Vehicle is starting..."

# Subclass Car
class Car(Vehicle):
    def start(self):
        return "Car is starting with a roar!"

# Subclass Bike
class Bike(Vehicle):
    def start(self):
        return "Bike is starting with a vroom!"

# Testing the classes
car = Car()
bike = Bike()