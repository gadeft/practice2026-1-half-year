"""
Завдання 10. Додати до одного чи кількох створених класів властивості (@property)
для контролю коректності зміни атрибутів, зокрема заборонити встановлення
від’ємних значень там, де це нелогічно (наприклад, баланс або пробіг).
"""

class Product:
    def __init__(self, name, price: float, description: str = "", characteristics: dict = None):
        if characteristics is None:
            characteristics = dict()
        self.name = name
        self.price = price
        self.description = description
        self.characteristics = characteristics

    @property
    def name(self) -> str:
        return self._name
    @property
    def price(self) -> float:
        return self._price
    @property
    def description(self) -> str:
        return self._description
    @property
    def characteristics(self) -> dict:
        return self._characteristics


    @name.setter
    def name(self, name: str):
        if type(name) != str:
            raise TypeError("name must be a string")
        if len(name) > 100:
            raise ValueError("name must be less than 100 characters")

        self._name = name

    @price.setter
    def price(self, price: float):
        try:
            self._price = float(price)
        except ValueError:
            raise TypeError("price must be a float")

    @description.setter
    def description(self, description: str):
        if type(description) != str:
            raise TypeError("description must be a string")
        if len(description) > 1000:
            raise ValueError("description must be less than 1000 characters")

        self._description = description

    @characteristics.setter
    def characteristics(self, characteristics: dict):
        if type(characteristics) != dict:
            raise TypeError("characteristics must be a dict")
        if len(characteristics) > 100:
            raise ValueError("characteristics must be less than 100 parameters")

        self._characteristics = characteristics


product = Product("aasdf", 4, description="")
print(product.name)
print(product.price)
print(product.description)
print(product.characteristics)