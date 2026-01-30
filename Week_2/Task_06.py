"""
Завдання 6. Створити базовий клас Animal із методом sound() і похідні класи Dog,
Cat, Cow, що перевизначають цей метод для відтворення власного звуку.
"""

class Animal:
    def sound(self):
        print("some sound")

class Dog(Animal):
    def sound(self):
        print("woof")

class Cat(Animal):
    def sound(self):
        print("meow")

class Cow(Animal):
    def sound(self):
        print("moo")

dog = Dog()
cat = Cat()
cow = Cow()
dog.sound()
cat.sound()
cow.sound()