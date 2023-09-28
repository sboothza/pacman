import pygame

from common import GREEN, WIDTH, HEIGHT, Direction, SPEED, keypress
from map import Map, map, Point


class Player(pygame.sprite.Sprite):
    def __init__(self, image_list):
        pygame.sprite.Sprite.__init__(self)
        self.images = image_list
        self.image = image_list[0] #pygame.Surface((50, 50))
        # self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.direction = Direction.DOWN
        self.image_number = 0

    def update(self):
        self.image = self.images[self.image_number]
        # self.image_number += 1

        result = map.move(Point(self.rect.x, self.rect.y), keypress)
        self.rect.x = result.x
        self.rect.y = result.y

        # if self.direction == Direction.RIGHT:
        #     self.rect.x += SPEED
        #     if self.rect.left > WIDTH:
        #         self.rect.x = 0
        #     if self.image_number > 3:
        #         self.image_number = 0
        # elif self.direction == Direction.LEFT:
        #     self.rect.x -= SPEED
        #     if self.rect.right < 0:
        #         self.rect.x = WIDTH
        #     if self.image_number > 7:
        #         self.image_number = 4
        # elif self.direction == Direction.UP:
        #     self.rect.y -= SPEED
        #     if self.rect.bottom < 0:
        #         self.rect.y = HEIGHT
        #     if self.image_number > 11:
        #         self.image_number = 8
        # elif self.direction == Direction.DOWN:
        #     self.rect.y += SPEED
        #     if self.rect.top > HEIGHT:
        #         self.rect.y = 0
        #     if self.image_number > 15:
        #         self.image_number = 12


        # self.image_number += 1
        # if self.image_number >= len(self.images):
        #     self.image_number = 0


        # self.rect.x += self.horiz_direction
        # if self.rect.right > WIDTH:
        #     self.horiz_direction = -5
        #     self.image_number = 4
        # elif self.rect.left < 0:
        #     self.horiz_direction = 5
        #     self.image_number = 0

        # self.rect.y += self.vert_direction
        # if self.rect.bottom > HEIGHT:
        #     self.vert_direction = -5
        # elif self.rect.top < 0:
        #     self.vert_direction = 5