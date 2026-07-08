import pygame
from settings import BLACK


def draw_text(screen, text, x, y, size=40, center=True):
    font = pygame.font.SysFont("Arial", size)
    surface = font.render(text, True, BLACK)

    if center:
        rect = surface.get_rect(center=(x, y))
    else:
        rect = surface.get_rect(topleft=(x, y))

    screen.blit(surface, rect)