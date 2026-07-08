import pygame
import sys

from settings import *
from ui import draw_text
from player import Player
from assets import load_assets
from level import create_world


# Initialize
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maria's Mushroom Run")
clock = pygame.time.Clock()

# Load assets
images, sounds = load_assets()

bg_img = images["background"]
player_img = images["player"]
mushroom_img = images["mushroom"]
enemy_img = images["enemy"]
platform_img = images["platform"]
castle_img = images["castle"]
flagpole_img = images["flagpole"]

jump_sfx = sounds["jump"]
collect_sfx = sounds["collect"]
hit_sfx = sounds["hit"]
win_sfx = sounds["win"]

pygame.mixer.music.play(-1)

# Groups
player_group = pygame.sprite.Group()
platforms = pygame.sprite.Group()
mushrooms = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# Game variables
score = 0
lives = STARTING_LIVES
game_state = "menu"
scroll = 0
flag_raising = False

# Castle
castle = pygame.sprite.Sprite()
castle.image = castle_img
castle.rect = castle.image.get_rect()
castle.rect.bottomleft = (LEVEL_LENGTH, HEIGHT - 100)

# Flagpole
flagpole = pygame.sprite.Sprite()
flagpole.image = flagpole_img
flagpole.rect = flagpole.image.get_rect()
flagpole.rect.bottomleft = (LEVEL_LENGTH - 120, HEIGHT - 40)

# Create player
player = Player(player_img, platforms, flagpole, jump_sfx)
player_group.add(player)


def reset_game():
    global score, lives, game_state, scroll, flag_raising

    score = 0
    lives = STARTING_LIVES
    scroll = 0
    flag_raising = False

    player.reset()

    flagpole.rect.bottomleft = (LEVEL_LENGTH - 120, HEIGHT - 40)

    create_world(platforms, mushrooms, enemies, platform_img, mushroom_img, enemy_img)

    game_state = "playing"


# Create world first time
create_world(platforms, mushrooms, enemies, platform_img, mushroom_img, enemy_img)


# Game loop
running = True

while running:
    clock.tick(FPS)
    screen.fill(WHITE)

    # Draw background
    screen.blit(bg_img, (-int(scroll * 0.5), 0))

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if game_state == "menu":
                game_state = "playing"

            elif game_state == "playing":
                if event.key == pygame.K_ESCAPE:
                    game_state = "paused"

            elif game_state == "paused":
                if event.key == pygame.K_ESCAPE:
                    game_state = "playing"

                elif event.key == pygame.K_r:
                    reset_game()

                elif event.key == pygame.K_q:
                    running = False

            elif game_state == "gameover":
                reset_game()

    # Menu
    if game_state == "menu":
        draw_text(screen, "Maria's Mushroom Run", WIDTH // 2, HEIGHT // 2 - 50)
        draw_text(screen, "Press any key to start", WIDTH // 2, HEIGHT // 2 + 10)

    # Playing
    elif game_state == "playing":
        scroll, player_status = player.update(scroll)

        if player_status == "fell":
            hit_sfx.play()
            lives -= 1

            if lives <= 0:
                game_state = "gameover"
            else:
                player.reset()
                scroll = 0

        elif player_status == "level_complete":
            game_state = "level_complete"
            win_sfx.play()
            flag_raising = True

        enemies.update()

        # Collect mushrooms
        hit_mushrooms = pygame.sprite.spritecollide(player, mushrooms, True)

        if hit_mushrooms:
            collect_sfx.play()
            score += len(hit_mushrooms)

        # Enemy collision
        hit_enemies = pygame.sprite.spritecollide(player, enemies, False)

        for enemy in hit_enemies:
            if player.vel_y > 0:
                enemies.remove(enemy)
                player.vel_y = -10
            else:
                hit_sfx.play()
                lives -= 1

                if lives <= 0:
                    game_state = "gameover"
                else:
                    player.reset()
                    scroll = 0

        # Draw platforms, mushrooms, enemies
        for group in [platforms, mushrooms, enemies]:
            for sprite in group:
                screen.blit(sprite.image, (sprite.rect.x - scroll, sprite.rect.y))

        # Draw player
        screen.blit(player.image, (player.rect.x - scroll, player.rect.y))

        # Draw UI
        draw_text(screen, f"Score: {score}", 10, 10, size=28, center=False)
        draw_text(screen, f"Lives: {lives}", WIDTH - 120, 10, size=28, center=False)

    # Paused
    elif game_state == "paused":
        draw_text(screen, "Paused", WIDTH // 2, HEIGHT // 2 - 80, size=64)
        draw_text(screen, "Press ESC to Resume", WIDTH // 2, HEIGHT // 2)
        draw_text(screen, "Press R to Restart", WIDTH // 2, HEIGHT // 2 + 50)
        draw_text(screen, "Press Q to Quit", WIDTH // 2, HEIGHT // 2 + 100)

    # Level complete
    elif game_state == "level_complete":
        if flag_raising and flagpole.rect.y > HEIGHT - 300:
            flagpole.rect.y -= 3
        else:
            draw_text(screen, "Level Complete!", WIDTH // 2, HEIGHT // 2 - 50, size=64)
            draw_text(screen, "Press close button to exit", WIDTH // 2, HEIGHT // 2 + 30, size=28)

    # Game over
    elif game_state == "gameover":
        draw_text(screen, "Game Over", WIDTH // 2, HEIGHT // 2 - 50, size=64)
        draw_text(screen, "Press any key to restart", WIDTH // 2, HEIGHT // 2 + 30, size=28)

    # Draw castle and flagpole
    screen.blit(castle.image, (castle.rect.x - scroll, castle.rect.y))
    screen.blit(flagpole.image, (flagpole.rect.x - scroll, flagpole.rect.y))

    pygame.display.flip()


pygame.quit()
sys.exit()