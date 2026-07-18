

class Hero:
    def __init__(self, name, level, health):
        self.name = name
        self.level= level
        self.health = health

    def action(self):
        print(f"{self.name} готов к бою!")

class MageHero(Hero):
    def __init__(self, name, level, health, mp):
        super().__init__(name, level, mp)
        self.mp = mp

    def action(self):
        print(f"Маг {self.name} кастует заклинание! MP: {self.mp}")
        
class WarriorHero(MageHero):
    def __init__(self, name, level, health, mp):
        super().__init__(name, level, health, mp)

    def action(self):
        print(f"Воин {self.name} рубит мечом! Уровень: {self.level}")


class BankAccount:
    bank_name = "Bakaibank"

    def __init__(self, hero, balance, password):
        self.hero = hero
        self._balance = balance
        self.__password = password

    def login(self, password):
        return password == self.__password

    @property
    def full_into(self):
        return f"{self.hero.name} | Баланс: {self._balance} SOM"

    @classmethod
    def get_bank_name(cls):
        return cls.bank_name

    def bonus_for_level(self):
        return self.hero.level * 10

    def __str__(self):
        return f"{self.hero.name} | Баланс: {self._balance} SOM"

    def __add__(self, other):
        if type(self.hero) == type(other.hero):
            return self._balance + other._balance
        return "Ошибка: Нельзя сложить счета героев разных классов!"

    def __eq__(self, other):
        return (
            type(self.hero) == type(other.hero)
            and self.hero.level == other.hero.level
        )

class KGSms:
    def send_otp(self, phone):
        return f"ОТР отправлен на номер {phone}"

mage1 = MageHero("Mario", 57, 88, 100)
mage2 = MageHero("Lion", 5, 45, 77)
warrior = WarriorHero("Lamin Yamal", 5, 33, 250)

mage1.action()
warrior.action()

acc1 = BankAccount("Kaspi", 100000, 6752)
acc2 = BankAccount("Astrobank", 30000, 9851)
acc3 = BankAccount("Novabank", 500000, 4532)

print(acc1)
print(acc2)

print("Банк:", acc1.get_bank_name())
print("Бонус зауровень:", acc1.bonus_for_level(), "SOM")

print("\n=== Проверка __add__ ===")
print("Сумма счетов двух магов:", acc1 + acc2)
print("Сумма мага и воина:", acc1 + acc3)

print("\n=== Проверка __eq__ ===")
print("Mage1 == Mage2 ?", acc1 == acc2)
print("Mage1 == Warrior ?", acc1 == acc3)

sms = KGSms()
print("\n", sms.send_otp("+996707331707"))





