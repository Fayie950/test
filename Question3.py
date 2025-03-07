# Base Shape class
class Shape:
    def __init__(self):
        print("Initializing Shape")

    def calculate_area(self):
        return 0  # Placeholder method


# Derived Rectangle class
class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()  # Calls the parent constructor
        self.width = width
        self.height = height

    def calculate_area(self):
        super().calculate_area()  # Calls base method (though it does nothing here)
        return self.width * self.height


# Testing the class
rect = Rectangle(4, 6)
print(rect.calculate_area())  # Output: 24