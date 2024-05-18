import pygame
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
    def __init__(self, name, image):
        self.name = name
        self.weapon = None
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 250

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
    def __init__(self, name, image):
        self.name = name
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 250

    def defeat(self):
        print(f"{self.name} побежден!")

def battle(fighter: Fighter, monster: Monster):
    fighter.attack()
    monster.defeat()

# Инициализация Pygame
pygame.init()

# Параметры экрана
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Боец против Монстра")

# Загрузка изображений
fighter_image = pygame.image.load('foto/boec.png')  # Замените на путь к вашему изображению бойца
monster_image = pygame.image.load('foto/monstr.png')  # Замените на путь к вашему изображению монстра

# Создание объектов
fighter = Fighter("Боец", fighter_image)
monster = Monster("Монстр", monster_image)

# Основной игровой цикл
running = True
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
attack = False
attack_counter = 0
original_x = fighter.rect.x

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                fighter.changeWeapon(Sword())
                attack = True
                attack_counter = 30  # Продолжительность анимации атаки

    # Обновление экрана
    screen.fill((255, 255, 255))  # Белый фон
    screen.blit(monster.image, monster.rect)  # Рисуем монстра

    if attack:
        fighter.rect.x = min(monster.rect.x - 50, fighter.rect.x + 10)  # Движение бойца к монстру
        attack_counter -= 1
        if attack_counter <= 0:
            attack = False
            battle(fighter, monster)
            fighter.rect.x = original_x  # Возврат бойца на исходную позицию
    else:
        screen.blit(fighter.image, fighter.rect)  # Рисуем бойца

    screen.blit(fighter.image, fighter.rect)  # Рисуем бойца

    # Обновление дисплея
    pygame.display.flip()
    clock.tick(30)

# Завершение Pygame
pygame.quit()

