import random

from settings import HEIGHT, LEVEL_LENGTH
from sprites import Platform, Mushroom, Enemy


LEVEL_LAYOUT = [
    (0, HEIGHT - 40),
    (300, 500),
    (600, 450),
    (900, 400),
    (1200, 350),
    (1500, 300),
    (1800, 500),
    (2100, 450),
    (2400, 400),
    (2700, 350),
]


def create_world(platforms, mushrooms, enemies, platform_img, mushroom_img, enemy_img):
    platforms.empty()
    mushrooms.empty()
    enemies.empty()

    # Create platforms
    for x, y in LEVEL_LAYOUT:
        platforms.add(Platform(x, y, platform_img))

    # Create mushrooms
    for _ in range(8):
        x = random.randint(300, LEVEL_LENGTH - 200)
        y = random.randint(100, 500)
        mushrooms.add(Mushroom(x, y, mushroom_img))

    # Create enemies
    for _ in range(8):
        x = random.randint(500, LEVEL_LENGTH - 200)
        y = random.randint(100, 500)
        enemies.add(Enemy(x, y, enemy_img))