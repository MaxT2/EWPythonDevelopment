import random

import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen_width, screen_height, x, y):
        pygame.sprite.Sprite.__init__(self)
        # set image of enemy
        self.image = pygame.Surface((screen_width/45, screen_height/40))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        # sets the inital position of the enemy
        self.rect.center = (x,y)
        # sets the speed of the enemy
        self.xspeed = 0
        self.yspeed = -2
        # store screen size to keep enemy on screen
        self.display_width = screen_width
        self.display_height = screen_height

    def update(self):
        self.rect.x += self.xspeed
        self.rect.y += self.yspeed

        # remove sprite when it leaves the bottom of the screen
        if self.rect.top > self.display_height:
            self.kill()


