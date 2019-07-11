import pygame
import random

def random_255():
    return random.randint(100,255)

class EnemySpriteRandom(pygame.sprite.Sprite):
    def __init__(self,screen_width,screen_height):
        self.image = pygame.Surface((10, 10))
        self.color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, screen_width), random.randint(0, screen_width))
        self.x_speed = random.randint(-3, 3)
        if self.x_speed == 0:
            self.x_speed += 1
        self.y_speed = random.randint(-3, 3)
        if self.y_speed == 0:
            self.y_speed += 1

    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        # check to see if sprite left screen and reverse direction
        if self.rect.right > 1000:
            # to make sure you never get stuck
            # self.rect.right = 999
            # reverse direction
            self.x_speed *= -1
            self.set_random_color()

        if self.rect.left < 0:
            self.x_speed *= -1
            self.set_random_color()

        if self.rect.bottom > 1000:
            self.y_speed *= -1
            self.set_random_color()

        if self.rect.top < 0:
            self.y_speed *= -1
            self.set_random_color()

    def set_random_color(self):
        self.image.fill((random_255(),random_255(),random_255()))

