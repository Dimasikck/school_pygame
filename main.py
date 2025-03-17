import pygame
import os

# Инициализация Pygame
pygame.init()

# Настройка окна
WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Моя игра")

# Цвета
WHITE = (255, 255, 255)

# Загрузка фона
background = pygame.image.load("assets/images/background.png")  # Укажи путь к файлу фона
background = pygame.transform.scale(background, (WIDTH, HEIGHT))


# Класс для персонажа
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5

        # Загрузка спрайтов
        self.idle_sprites = [pygame.image.load(f"idle_{i}.png") for i in range(4)]  # 4 кадра для состояния покоя
        self.move_right_sprites = [pygame.image.load(f"move_right_{i}.png") for i in
                                   range(4)]  # 4 кадра для движения вправо
        self.move_left_sprites = [pygame.image.load(f"move_left_{i}.png") for i in
                                  range(4)]  # 4 кадра для движения влево

        # Масштабирование спрайтов (если нужно)
        self.idle_sprites = [pygame.transform.scale(sprite, (50, 50)) for sprite in self.idle_sprites]
        self.move_right_sprites = [pygame.transform.scale(sprite, (50, 50)) for sprite in self.move_right_sprites]
        self.move_left_sprites = [pygame.transform.scale(sprite, (50, 50)) for sprite in self.move_left_sprites]

        self.current_sprite = 0
        self.image = self.idle_sprites[self.current_sprite]
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

        self.direction = "idle"  # Текущее состояние: idle, right, left
        self.animation_speed = 0.15  # Скорость смены кадров

    def update(self):
        # Анимация
        self.current_sprite += self.animation_speed
        if self.current_sprite >= len(self.idle_sprites):
            self.current_sprite = 0

        # Выбор спрайтов в зависимости от направления
        if self.direction == "idle":
            self.image = self.idle_sprites[int(self.current_sprite)]
        elif self.direction == "right":
            self.image = self.move_right_sprites[int(self.current_sprite)]
        elif self.direction == "left":
            self.image = self.move_left_sprites[int(self.current_sprite)]

        self.rect.topleft = (self.x, self.y)

    def move(self, keys):
        # Управление движением
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
            self.direction = "left"
        elif keys[pygame.K_RIGHT]:
            self.x += self.speed
            self.direction = "right"
        else:
            self.direction = "idle"

        # Ограничение выхода за пределы экрана
        self.x = max(0, min(self.x, WIDTH - self.rect.width))


# Создание персонажа
player = Player(375, 275)  # Начальная позиция персонажа (по центру)


# Основной игровой цикл
def main():
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(60)  # 60 FPS

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Получение нажатых клавиш
        keys = pygame.key.get_pressed()

        # Обновление персонажа
        player.move(keys)
        player.update()

        # Отрисовка
        WINDOW.blit(background, (0, 0))  # Отрисовка фона
        WINDOW.blit(player.image, player.rect)  # Отрисовка персонажа
        pygame.display.flip()  # Обновление экрана

    pygame.quit()


if __name__ == "__main__":
    main()