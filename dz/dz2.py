import random
class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength
    def greet(self):
        print(f"Привет!, Я {self.name}, мой уровень{self.level}")
    def attack(self):
        print(f"{self.name} наносит удар!")
    def rest(self):
        self.health += 10
        print(f"{self.name} отдыхает… и восстанавливает здоровье до {self.health}")

class Warrior(Hero):
    def __init__(self, name, level, health, strength, stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina
    def attack(self):
        print("воин атакует мечом!")

class Mage(Hero):
    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.mana = mana
    def attack(self):
        print("маг кастует заклинание!")

class Assassin(Hero):
    def __init__(self, name, level, health, strength, stealth):
        super().__init__(name, level, health, strength)
        self.stealth = stealth
    def attack(self):
        print("Ассасин атакует из-под тишка!")

warrior = Warrior('Warrior', 1, 80, 100, 65)
mage = Mage('Mage', 5, 15, 45, 88)
assassin = Assassin('Assassin', 8, 65, 21, 55)

heroes = [warrior, mage, assassin]

choice = input("Выберите героя (warrior/ mage/ assassin): ").lower()
if choice == "warrior":
    player = warrior
elif choice == "mage":
    player = mage
elif choice == "assassin":
    player = assassin
else:
    print("такого героя нет!")
    exit()

enemy = random.choice(heroes)
while enemy  == player:
    enemy = random.choice(heroes)

print(f"\nвы выбрали: {player.name}")
print(f"противник: {enemy.name}\n")

player.attack()
enemy.attack()

if player.name == "Warrior" and enemy.name == "Assassin":
    print("Warrior победил")
elif player.name == "Assassin" and enemy.name == "Mage":
    print("Assassin победил!")
elif player.name == "Mage" and enemy.name == "Warrior":
    print("Mage победил!")
else:
    print(f"{enemy.name} победил!")