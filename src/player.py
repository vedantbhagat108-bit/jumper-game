import pygame
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, image, platforms, flagpole, jump_sfx):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()

        self.platforms = platforms
        self.flagpole = flagpole
        self.jump_sfx = jump_sfx

        self.vel_y = 0
        self.on_ground = False
        self.jump_count = 0
        self.jump_pressed = False

        self.reset()

    def reset(self):
        self.rect.center = (100, HEIGHT - 150)
        self.vel_y = 0
        self.on_ground = False
        self.jump_count = 0
        self.jump_pressed = False

    def update(self, scroll):
        keys = pygame.key.get_pressed()
        dx = 0

        if keys[pygame.K_LEFT]:
            dx = -PLAYER_SPEED

        if keys[pygame.K_RIGHT]:
            dx = PLAYER_SPEED

        # Jump
        if keys[pygame.K_SPACE]:
            if not self.jump_pressed and self.jump_count < 2:
                self.vel_y = PLAYER_JUMP_POWER
                self.jump_count += 1
                self.jump_sfx.play()
                self.jump_pressed = True
        else:
            self.jump_pressed = False

        # Gravity
        self.vel_y += GRAVITY

        if self.vel_y > MAX_FALL_SPEED:
            self.vel_y = MAX_FALL_SPEED

        # Vertical movement
        self.rect.y += self.vel_y

        # Platform collision
        self.on_ground = False

        for platform in self.platforms:
            if self.rect.colliderect(platform.rect) and self.vel_y >= 0:
                self.rect.bottom = platform.rect.top
                self.vel_y = 0
                self.on_ground = True
                self.jump_count = 0

        # Horizontal movement
        self.rect.x += dx

        # Keep player inside camera view
        if self.rect.left < scroll:
            self.rect.left = scroll

        if self.rect.right > scroll + WIDTH:
            self.rect.right = scroll + WIDTH

        # Player fell down
        if self.rect.top > HEIGHT:
            return scroll, "fell"

        # Player reached flagpole
        if self.rect.colliderect(self.flagpole.rect):
            return scroll, "level_complete"

        # Camera scroll
        scroll = max(0, self.rect.centerx - WIDTH // 2)

        return scroll, None