class ShoppingCart:
    def __init__(self):
        self.cart = []
    def add(self, name, price):
        self.cart.append((name, price))
    def __len__(self):
        return len(self.cart)
    def __getitem__(self, key):
        return f"{self.cart[key][0]}: ${self.cart[key][1]:.2f}"
    def __add__(self, other):
        new_cart = ShoppingCart()
        new_cart.cart = self.cart + other.cart
        return new_cart
    def total_price(self):
        return sum(price[1] for _.price in self.cart)
    def __eq__(self, other):
        return self.total_price() == other.total_price()
    def __str__(self):
        return f"ShoppingCart: {len(self.cart)} items, total ${self.total_price()}"
    def __bool__(self):
        return len(self.cart) != 0
    
cart1 = ShoppingCart()
cart1.add("Apple", 2.50)
cart1.add("Bread", 3.00)

cart2 = ShoppingCart()
cart2.add("Milk", 4.50)
cart2.add("Eggs", 1.00)

print(len(cart1))
print(cart1[0])
print(cart1)

cart3 = cart1 + cart2
print(cart3)
print(len(cart3))

print(cart1 == cart2)

empty = ShoppingCart()
if not empty:
    print("Cart is empty")