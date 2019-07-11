import random
import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, screen_width, screen_height):
        pygame.sprite.Sprite.__init__(self)

        # set image of enemy
        # create rectangle surface of size x,y
        self.image = pygame.Surface((50, 50))
        # fill new rectangle with a color
        self.image.fill((255, 0, 0))
        # set bounding box rectangle position and dimensions using size of surface
        self.rect = self.image.get_rect()
        # sets the inital position of the enemy
        # self.rect.center = ((random.randint(50, screen_width - 50), random.randint(-400, -100)))
        self.rect.center = (600, 400)
        # sets the speed of the enemy
        self.x_speed = 0
        self.y_speed = 0
        # store screen size to keep enemy on screen
        self.display_width = screen_width
        self.display_height = screen_height

    def update(self):
        # do noting at first because speeds are 0
        # update position based on speeds
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        # move based on mouse position
        self.rect.center = pygame.mouse.get_pos()









        #
        # # remove sprite when it leaves the bottom of the screen
        # if(self.rect.top > self.display_height):
        #     self.kill()


