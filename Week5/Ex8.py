from abc import ABC, abstractmethod

class Interactable:
    @abstractmethod
    def interact(self, character):
        pass

class FIghtable:
    @abstractmethod
    def take_hit(self, damage):
        pass

class Potion(Interactable):
    def __init__(self, power):
        self.power = power
    def interact(self, character):
        character.health += self.power
        return f"Healed {self.power} HP"

class Sword(Interactable):
    def __init__(self, bonus):
        self.bonus = bonus
    def interact(self, character):
        character.attack += self.bonus
        print(f"Attack +{self.bonus}")

class Mimic:
    def interact(self, character):
        character.health -= 15
        print(f"It's a Mimic! -15 HP")

class Monster(FIghtable):
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        self.items = []
    def take_hit(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        return self.health
class Hero(FIghtable):
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack = 10
    def pick_up(self, item):
        self.items.append(item)
    def take_hit(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        return self.health
    def fight(self, enemy: Monster):
        for item in self.items:
            while self.health and enemy.health:
                self.take_hit(self.attack)
                print(f"{self.name} hits {enemy.name} for {self.attack} damage")
                enemy.take_hits(enemy.attack)
                print(f"{enemy.name} hits {self.name} for {enemy.attack} damage")
            if not self.take_hit:
                print(f"{self.name} has been defeated!")
            if not enemy.take_hit:
                print(f"{enemy.name} has been defeated!")

class Dungeon:
    def __init__(self, name):
        self.name = name
    def place_item(self, item):
        ...