import pygame


def load_image(path, scale=None):
    image = pygame.image.load(path).convert_alpha()

    if scale:
        image = pygame.transform.scale(image, scale)

    return image


def load_assets():
    images = {
        "background": load_image("assets/images/background.png", (3000, 600)),
        "player": load_image("assets/images/maria.png", (40, 60)),
        "mushroom": load_image("assets/images/mushroom.png", (30, 30)),
        "enemy": load_image("assets/images/enemy.png", (40, 40)),
        "platform": load_image("assets/images/platform.png", (100, 20)),
        "castle": load_image("assets/images/castle.png"),
        "flagpole": load_image("assets/images/flagpole.png"),
    }

    sounds = {
        "jump": pygame.mixer.Sound("assets/sounds/jump.wav"),
        "collect": pygame.mixer.Sound("assets/sounds/coin.wav"),
        "hit": pygame.mixer.Sound("assets/sounds/hit.wav"),
        "win": pygame.mixer.Sound("assets/sounds/win.wav"),
    }

    pygame.mixer.music.load("assets/sounds/music.mp3")
    pygame.mixer.music.set_volume(0.5)

    return images, sounds