import math


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * math.pow(self.radius, 2)

rect = Rectangle(10, 2)
circ = Circle(1)
print(rect.area())
print(circ.area())