"""
Завдання 2. Створити клас Student з атрибутами ім’я, група, середній_бал та методом
show_info(), який виводить повну інформацію про студента. Створити декілька
об’єктів цього класу і вивести інформацію про кожного.
"""

class Student:
    def __init__(self, name, group, average_score):
        self.name = name
        self.group = group
        self.average_score = average_score

    def show_info(self):
        print(f"Name: {self.name}, Group: {self.group}, Average Score: {self.average_score}")


students = [
    Student("Vasya", "A", 7.8),
    Student("Petya", "A", 8.5),
    Student("Bred", "A", 8.1),
    Student("Masha", "A", 7.6)
]

for student in students:
    student.show_info()