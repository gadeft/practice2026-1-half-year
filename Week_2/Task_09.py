"""
Завдання 9. Змоделювати предметну область на вибір (наприклад, «Бібліотека—
Книга—Читач» або «Зоопарк—Тварина—Доглядальник») так, щоб у рішенні були
присутні ієрархія класів, абстракція, інкапсуляція, наслідування та поліморфізм;
продемонструвати типові взаємодії об’єктів.

Обрана предметна область: "Інтернет-магазин".
"""

from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    @abstractmethod
    def get_role(self) -> str:
        pass

class Admin(User):
    def get_role(self) -> str:
        return "admin"

class Customer(User):
    def get_role(self) -> str:
        return "customer"

# payment classes
class Payment(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass

class CashPayment(Payment):
    def pay(self, amount: float):
        return f"Payment by cash. Total of: {amount:.2f}"

class CardPayment(Payment):
    def pay(self, amount: float):
        return f"Payment by card. Total of: {amount:.2f}"


class Product:
    def __init__(self, name, price: float, description: str = "", characteristics: dict = None):
        if characteristics is None:
            characteristics = dict()
        self.__name = name
        self.__price = price
        self.__description = description
        self.__characteristics = characteristics

    def get_name(self) -> str:
        return self.__name
    def get_price(self) -> float:
        return self.__price
    def get_description(self) -> str:
        return self.__description
    def get_characteristics(self) -> dict:
        return self.__characteristics

    def set_name(self, name: str):
        self.__name = name
    def set_price(self, price: float):
        self.__price = price
    def set_description(self, description: str):
        self.__description = description
    def set_characteristics(self, characteristics: dict):
        self.__characteristics = characteristics


class Order:
    def __init__(self, customer: Customer, *products: Product):
        self.__customer = customer
        self.__products = list(products)

    def add_products(self, *products: Product):
        self.__products.extend(products)
    def remove_products(self, *products: Product):
        for prod in products:
            self.__products.remove(prod)

    def get_total_price(self):
        total = 0
        for prod in self.__products:
            total += prod.get_price()
        return total

    def show_order(self):
        print(f"Customer name: {self.__customer.get_name()}")
        print("Products:")
        for prod in self.__products:
            print(f"{prod.get_name()} ({prod.get_price():.2f})")
        print(f"Total price: {self.get_total_price():.2f}")


the_customer = Customer("Vasya")

phone = Product("Phone", 30000)
book = Product("Book", 500)
mousepad = Product("Mousepad", 200.5)

order = Order(the_customer, phone, book)
order.remove_products(phone)
order.add_products(phone)
order.add_products(mousepad)
order.show_order()

payment = CashPayment()
print(payment.pay(order.get_total_price()))
