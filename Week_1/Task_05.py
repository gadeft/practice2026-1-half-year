"""
Завдання 5. Написати програму, що здійснює сортування масиву методом
«бульбашкового сортування». Дані для масиву користувач вводить самостійно;
початкова довжина масиву не фіксована.
"""

array = input("Enter an array of integers (divide them with a space): ").split()

sorted_elements = 1
for i in range(len(array)):
    num_of_exchanges = 0
    for j in range(len(array) - sorted_elements):
        if array[j] > array[j + 1]:
            temp = array[j]
            array[j] = array[j + 1]
            array[j + 1] = temp
            num_of_exchanges += 1
    if num_of_exchanges == 0:
        break

print(array)