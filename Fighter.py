from abc import ABC, abstractmethod

# Шаг 1: Создайте абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Шаг 2: Реализуйте конкретные типы оружия
class Sword(Weapon):
    def attack(self):
        return "удар мечом"

class Bow(Weapon):
    def attack(self):
        return "выстрел из лука"

class Axe(Weapon):
    def attack(self):
        return "удар топором"

# Шаг 3: Модифицируйте класс Fighter
class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def changeWeapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает {self.weapon.attack()}.")

    def attack(self):
        if self.weapon:
            print(f"{self.name} наносит {self.weapon.attack()}.")
        else:
            print(f"{self.name} безоружен.")

# Шаг 4: Реализация боя
class Monster:
    def __init__(self, name):
        self.name = name

    def defeat(self):
        print(f"{self.name} побежден!")

def battle(fighter: Fighter, monster: Monster):
    fighter.attack()
    monster.defeat()

# Пример использования
if __name__ == "__main__":
    fighter = Fighter("Боец")
    monster = Monster("Монстр")

    # Боец выбирает меч
    sword = Sword()
    fighter.changeWeapon(sword)
    battle(fighter, monster)

    # Боец выбирает лук
    bow = Bow()
    fighter.changeWeapon(bow)
    battle(fighter, monster)

    # Боец выбирает топор
    axe = Axe()
    fighter.changeWeapon(axe)
    battle(fighter, monster)
