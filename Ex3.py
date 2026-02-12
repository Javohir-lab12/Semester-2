class ShoppingCart:
    store_name = "Online Bazaar"
    tax_rate = 0.08
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []

    def add_item(self, item_name, price):
        if price <= 0:
            return("Invalid price. Must be greater than 0")
        dict = {}
        dict[item_name] = price
        self.items.append(dict)
        print(f"Added {item_name} (${price}) to cart")
    
    def remove_item(self, item_name):
        for d in self.items:
            if item_name in d:
                self.items.remove(d)
                
        print(f"Item '{item_name}' not found in cart")
    def get_subtotal(self):
        return sum(price for price in self.items.values())
                
    def display_cart(self):
        print(f"Cart for {self.customer_name} at {ShoppingCart.store_name}:")
        for d in self.items:
            for name, price in d.items():
                print(f" - {name}: ${price}")
        print(f"Subtotal: ${self.get_subtotal}")
