class Product:
    def __init__(self, name, price, quantity):
        self._name = name
        self.price = price
        self.quantity = quantity
    @property
    def name(self):
        return self._name 
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price must be positive")
        self._price = value
    @property
    def quantity(self):
        return self._quantity
    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError("Quantity cannot be negative")
        self._quantity = value
    def restock(self, amount):
        if amount < 0:
            raise ValueError("The amount must be positive")
        self.quantity += amount
    def sell(self, amount):
        if amount < 0:
            raise ValueError("The amount must be positive")
        if amount > self.quantity:
            raise ValueError("The amount cannot exceed the current quantity.")
        self.quantity -= amount
    def total_value(self):
        return self._quantity * self._price
       
p = Product("Laptop", 999.99, 10)
print(p.name)
print(p.price)
print(p.quantity)
print(p.total_value())

p.price = 899.99
p.restock(5)
print(p.quantity)
print(p.total_value())

p.sell(3)
print(p.quantity)

try:
    p.price = -50
except ValueError as e:
    print(e)

try:
    p.sell(100)
except ValueError as e:
    print(e)

try:
    p.name = "Tablet"
except AttributeError:
    print("Cannot change product name")