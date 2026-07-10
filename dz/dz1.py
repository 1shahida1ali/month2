class Hero:
    def __init__(self, name, level, health, strength ):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength
    def greet(self):
        print(f'Привет, я {self.name}, мой уровень {self.level}')
    def attack(self):
        print(f'{self.name} наносит удар!')
        self.strength -= 1
    def rest(self):
        print(f'{self.name} отдыхает…')
        self.health += 1

hero1 = Hero('Franklin', 5, 100, 100)
hero2 = Hero('Trevor', 4, 80, 70)
hero1.greet()
hero1.attack()
hero1.rest()
print('здоровье:', hero1.health)
print('cила:', hero1.strength)
print()
hero2.greet()
hero2.attack()
hero2.rest()
print('здоровье:', hero2.health)
print('сила:', hero2.strength)
print()
