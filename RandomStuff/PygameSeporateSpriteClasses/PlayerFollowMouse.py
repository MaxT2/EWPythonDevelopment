import pygame
import random

def random_255():
    return random.randint(100,255)


class PlayerSprite(pygame.sprite.Sprite):
    def __init__(self,screen_width,screen_height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width / 2, screen_height / 2)
        self.x_speed = 0
        self.y_speed = 0

    def update(self):
        self.rect.center = pygame.mouse.get_pos()
        # self.rect.x += self.x_speed
        # self.rect.y += self.y_speed

        # # check to see if sprite left screen and reverse direction
        # if self.rect.right > 1000:
        #     # to make sure you never get stuck
        #     # self.rect.right = 999
        #     # reverse direction
        #     self.x_speed *= -1
        #     self.set_random_color()
        #
        # if self.rect.left < 0:
        #     self.x_speed *= -1
        #     self.set_random_color()
        #
        # if self.rect.bottom > 1000:
        #     self.y_speed *= -1
        #     self.set_random_color()
        #
        # if self.rect.top < 0:
        #     self.y_speed *= -1
        #     self.set_random_color()

    def set_random_color(self):
        self.image.fill((random_255(),random_255(),random_255()))

