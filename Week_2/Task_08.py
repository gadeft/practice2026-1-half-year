"""
Завдання 8. Створити абстрактний клас Shape із абстрактним методом area() та
реалізувати класи Circle і Rectangle, що наслідують Shape і визначають власні
обчислення площі.
"""

import math

class Shape:
    def area(self):
        raise NotImplementedError

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * math.pow(self.radius, 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


circle = Circle(5)
rectangle = Rectangle(5, 10)

print(circle.area())
print(rectangle.area())
