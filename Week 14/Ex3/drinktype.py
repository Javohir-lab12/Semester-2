from enum import Enum
from abc import ABC, abstractmethod

class DrinkType(Enum):
    COFFEE = 1
    TEA = 2
    JUICE = 3

class Drink:
    def __init__(self, size):
        self.size = size
    @abstractmethod
    def prepare():
        pass

class Coffee(Drink):
    def prepare(self):
        print("Brewing {self.size} coffee ☕")

class Tea(Drink):
    def prepare(self):
        print("Steeping {self.size} tea 🍵")

class Juice(Drink):
    def prepare(self):
        print("Squeezing {self.size} juice 🧃")

class DrinkFactory:
    _types = {
        DrinkType.COFFEE: Coffee,
        DrinkType.TEA: Tea,
        DrinkType.JUICE: Juice
    }
    @staticmethod
    def create(kind, size):
        cls = DrinkFactory._types.get(kind)
        if cls is None:
            raise ValueError(f'Unknown drink: {kind}')
        return cls(size)
    
orders = [
    (DrinkType.COFFEE, "large"),
    (DrinkType.TEA, "small"),
    (DrinkType.JUICE, "medium"),
    (DrinkType.COFFEE, "small"),
]

for kind, size in orders:
    drink = DrinkFactory.create(kind, size)
    drink.prepare()