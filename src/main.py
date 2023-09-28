import os

import pygame
import random

from common import WIDTH, HEIGHT, FPS, BLACK, Direction, WHITE, Orientation, KeyPress, RED, keypress
from map import Map, map
from player import Player
from spritesheet import SpriteSheet


def main():
    # initialize pygame and create window
    pygame.init()
    pygame.mixer.init()  # for sound
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    base_folder = os.path.abspath(os.pardir)

    pygame.display.set_caption("Pacman")
    font = pygame.font.Font(os.path.join(base_folder, "resources", "arcadeclassic.ttf"), 32)

    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()

    img_folder = os.path.join(base_folder, 'images')
    spritesheet = SpriteSheet(os.path.join(img_folder, "pacman-sprites.png"))
    # right: 0 - 3, left: 4 - 7, up: 8 - 11, down: 12 - 15
    player_images = spritesheet.images_at([(4, 1, 13, 13), (20, 1, 13, 13), (36, 1, 13, 13), (20, 1, 13, 13),
                                           (4, 17, 13, 13), (20, 17, 13, 13), (36, 1, 13, 13), (20, 17, 13, 13),
                                           (4, 33, 13, 13), (20, 33, 13, 13), (36, 1, 13, 13), (20, 33, 13, 13),
                                           (4, 49, 13, 13), (20, 49, 13, 13), (36, 1, 13, 13), (20, 49, 13, 13)],
                                          size=(26, 26))

    red_ghost_images = spritesheet.images_at([(4, 65, 13, 13)])
    player = Player(player_images)
    all_sprites.add(player)

    # red_ghost =

    img = pygame.image.load(os.path.join(img_folder, 'pacman_bg_plain.jpg')).convert()
    background = pygame.transform.scale(img, (WIDTH, HEIGHT))
    background_rect = background.get_rect()
    score = 1000
    high_score = 10000

    node_a = map.add_node(50, 100)
    node_b = map.add_node(600, 100)
    node_c = map.add_node(600, 600)
    node_d = map.add_node(50, 600)
    map.add_path(node_a, node_b)
    map.add_path(node_b, node_c)
    map.add_path(node_c, node_d)
    map.add_path(node_d, node_a)

    player.direction = Direction.RIGHT
    player.rect.x = node_a.x
    player.rect.y = node_a.y
    player.image_number = 0

    # Game loop
    running = True
    while running:
        # keep loop running at the right speed
        clock.tick(FPS)
        # Process input (events)
        keypress = KeyPress.NONE
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    keypress = keypress | KeyPress.LEFT
                if event.key == pygame.K_RIGHT:
                    keypress = keypress | KeyPress.RIGHT
                if event.key == pygame.K_UP:
                    keypress = keypress | KeyPress.UP
                if event.key == pygame.K_DOWN:
                    keypress = keypress | KeyPress.DOWN

                #         player.direction = Direction.LEFT
                #         player.image_number = 4
                #     if event.key == pygame.K_RIGHT:
                #         player.direction = Direction.RIGHT
                #         player.image_number = 0
                # else:
                #     if event.key == pygame.K_UP:
                #         player.direction = Direction.UP
                #         player.image_number = 8
                #     if event.key == pygame.K_DOWN:
                #         player.direction = Direction.DOWN
                #         player.image_number = 12

        # Update
        all_sprites.update()
        score_title = font.render('1UP', True, WHITE, BLACK)
        score_title_rect = score_title.get_rect()
        score_title_rect.left = 50
        score_title_rect.top = 1

        high_score_title = font.render('HIGH SCORE', True, WHITE, BLACK)
        high_score_title_rect = high_score_title.get_rect()
        high_score_title_rect.left = 250
        high_score_title_rect.top = 1

        score_text = font.render(str(score), True, WHITE, BLACK)
        score_rect = score_text.get_rect()
        score_rect.left = 50
        score_rect.top = 32

        high_score_text = font.render(str(score), True, WHITE, BLACK)
        high_score_rect = high_score_text.get_rect()
        high_score_rect.left = 250
        high_score_rect.top = 32

        # Draw / render
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        for path in map.paths:
            pygame.draw.line(screen, RED, (path.node1.x, path.node1.y), (path.node2.x, path.node2.y))

        screen.blit(score_title, score_title_rect)
        screen.blit(high_score_title, high_score_title_rect)
        screen.blit(score_text, score_rect)
        screen.blit(high_score_text, high_score_rect)

        all_sprites.draw(screen)
        # *after* drawing everything, flip the display
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
