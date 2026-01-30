import math


def calc_rectangle_area(width, height):
    return width * height

def calc_circle_area(radius):
    return math.pi * math.pow(radius, 2)

print(calc_rectangle_area(10, 2))
print(calc_circle_area(1))