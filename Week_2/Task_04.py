"""
Завдання 4. Створити клас Car з атрибутами марка, рік_випуску, пробіг і методами
drive(km) для збільшення пробігу та info() для виведення опису авто. Додати
конструктор init() і метод str() для зручного текстового відображення об’єкта.
"""

class Car:
    def __init__(self, mark, year, mileage):
        self.mark = mark
        self.year = year
        self.mileage = mileage

    def drive(self, km):
        self.mileage += km

    def info(self):
        return {"mark": self.mark, "year": self.year, "mileage": self.mileage}

    def __str__(self):
        sep = "\n--------------------------\n"
        return sep + f"Mark: {self.mark} \nYear fo manufacture: {self.year} \nMileage: {self.mileage}" + sep


car = Car("Audi", "2016", 20000)
print(car.info())
car.drive(100)
print(car.info())
print(car)