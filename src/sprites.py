import pygame
import random


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))


class Mushroom(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))

        self.direction = random.choice([-1, 1])
        self.speed = 2

    def update(self):
        self.rect.x += self.speed * self.direction

        if random.randint(0, 100) < 2:
            self.direction *= -1