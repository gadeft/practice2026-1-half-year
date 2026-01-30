"""
Завдання 6. Розробити програму для обчислення факторіала числа з використанням
рекурсивного підходу. Визначити алгоритмічну складність реалізованого методу.
"""

number = -1
while number < 0:
    print("!!!The number must be greater than or equal to 0")
    number = int(input("Enter the number: "))

def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(number))
print("The time complexity is O(n)")
print("The space complexity is O(n)")