class Inventory:
    def __init__(self, name):
        self.name = name
        self.items = []
    def add(self, name, value):
        self.items.append((name, value))
    def __len__(self):
        return len(self.items)
    def __getitem__(self, key):
        return f"{self.items[0]} ({self.items[1]} gold)"
    def __str__(self):
        return f"Inventory {f}"