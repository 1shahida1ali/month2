from abc import ABC, abstractmethod

class Hero(ABC):
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.__health = health
        self.strength = strength
    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def rest(self):
        print(f"{self.name} отдыхает")
        self.__health += 1

    @abstractmethod
    def attack(self):
        pass

class Warrior(Hero):
    def attack(self):
        print(f"{self.name} атакует мечом")

class Mage(Hero):
    def attack(self):
        print(f"{self.name} использует магию")

class Assassin(Hero):
    def attack(self):
        print(f"{self.name} атакует из-под тишка")

Warrior = Warrior("mario", 67, 97, 100)
Mage = Mage("willlow", 11, 59, 100)
Assassin = Assassin("nori", 9, 55, 90)

Warrior.greet()
Warrior.attack()
Warrior.rest()
print()

Mage.greet()
Mage.attack()
Mage.rest()
print()

Assassin.greet()
Assassin.attack()
Assassin.rest()
print()
