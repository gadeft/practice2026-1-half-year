"""
Завдання 2. Розробити програму, яка перетворює числове значення у рядкове
представлення без використання вбудованої функції str().
"""

DIGITS = "0123456789"

number = int(input("Enter a number: "))
output = ""

while number > 0:
    digit = number % 10
    output = DIGITS[digit] + output
    number = number // 10

print(output)