"""
Завдання 4. Розробити програму для розрахунку дальності польоту снаряда за
заданими початковою швидкістю та кутом вильоту. Вважати умови ідеальними.
Програма має обчислювати та виводити максимальну висоту, а також висоту снаряда
на кожну секунду польоту.
"""

import math



g = 9.8



def calc_flight_time(vel0_y, g):
    return -2 * (vel0_y / (-g))

def calc_height(t, vel0_y, g):
    return (vel0_y * t) + (-g * math.pow(t, 2))/2

def calc_max_height(vel0_y, g):
    mid_time = calc_flight_time(vel0_y, g) / 2 # The time needed for a body to reach the middle of the flight, i.e. time when the body reaches max height
    return calc_height(mid_time, vel0_y, g)

def calc_flight_distance(vel0_x, vel0_y, g):
    full_time = calc_flight_time(vel0_y, g) #The time needed for a body to reach the same height as it started
    return full_time * vel0_x



vel = -1
while vel < 0:
    print("!!!The velocity must be greater than 0 (m/s)")
    vel = float(input("Enter the velocity(float): "))
angle = -1
while angle < 0 or angle > 90:
    print("!!!The angle must vary between 0 and 90 (degrees")
    angle = math.radians(float(input("Enter the angle(float): ")))



vel_x = vel * math.cos(angle)
vel_y = vel * math.sin(angle)
print()
print("The flight distance is (m): " + str(calc_flight_distance(vel_x, vel_y, g)))
print("The max height is (m):" + str(calc_max_height(vel_y, g)))

flight_time = calc_flight_time(vel_y, g)
print("The flight time is (s): " + str(flight_time))

for i in range(1, math.ceil(flight_time)):
    print("Time has passed (s): " + str(i), end="")
    print("; Height (m): " + str(calc_height(i, vel_y, g)))