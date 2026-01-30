"""
Завдання 7. Створити структуру даних, що зберігає інформацію про групу студентів.
Для кожного студента передбачити поля: ім’я, прізвище, оцінки з п’яти навчальних
дисциплін. Реалізувати програму, яка виводить таблицю із середнім балом кожного
студента та обчислює середній бал групи з кожної дисципліни.
"""

NUM_OF_DISCIPLINES = 5

class Student:
    def __init__(self, name, surname, *marks):
        if len(marks) != NUM_OF_DISCIPLINES:
            raise ValueError(f"!!!The number of marks must be {NUM_OF_DISCIPLINES}")

        self._name = name
        self._surname = surname
        self._marks = marks

    def get_name(self):
        return self._name
    def get_surname(self):
        return self._surname
    def get_marks(self):
        return self._marks

    def average_mark(self):
        return sum(self._marks) / len(self._marks)


class Group:
    def __init__(self, *students):
        self._students = list(students)

    def get_students(self):
        return self._students
    def add_student(self, student):
        self._students.append(student)
    def remove_student(self, student):
        self._students.remove(student)

    def average_mark_student(self):
        output = list()
        for student in self._students:
            output.append(student.average_mark())

        return output

    def average_mark_group(self):
        every_student_marks = list()
        for student in self._students:
            every_student_marks.append(student.get_marks())

        number_of_students = len(every_student_marks)
        average_marks = list()
        for i in range(NUM_OF_DISCIPLINES):
            temp_sum = 0
            for student in every_student_marks:
                temp_sum += student[i]
            average_marks.append(temp_sum / number_of_students)

        return average_marks


# petya = Student("Petya", "Petrov", 4, 3, 4, 5, 4)
# vanya = Student("Vanya", "Ivanov", 4, 3, 2, 3, 3)
# bred = Student("Bred", "Pitt", 3, 3, 2, 2, 5)
#
# group = Group(petya, vanya, bred)
#
# print(group.average_mark_student())
# print(group.average_mark_group())f