import math


# Base Shape class
class Shape:
    def area(self):
        pass  # Placeholder method


# Circle class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


# Rectangle class
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Function to calculate total area
def total_area(shapes):
    return sum(shape.area() for shape in shapes)


# Testing the function
shapes = [Circle(5), Rectangle(4, 6)]
print(total_area(shapes))  # Output: Sum of areas