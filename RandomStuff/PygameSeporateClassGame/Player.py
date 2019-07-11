import pygame
import random



def random_255():
    return random.randint(100, 255)


class PlayerSprite(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height, size):
        pygame.sprite.Sprite.__init__(self)
        # setup image for sprite
        self.image = pygame.Surface((size, size))
        self.image.fill((0, 255, 0))
        # setup rectangle "bounding box"
        self.rect = self.image.get_rect()
        # set rect center position (x,y)
        self.rect.center = (screen_width / 2, screen_height - size)
        # speed variables for movement
        self.x_speed = 0
        self.y_speed = 0

    def update(self):
        # update position based on current x and y speed
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        # reset x_speed to 0 after position update
        self.x_speed = 0

        # keep player on screen
        if self.rect.left < 0:
            self.rect.x = 0

        # this should be screen width instead of 10005

    def move_left(self, speed):
        self.x_speed = -1 * speed

    def move_right(self, speed):
        self.x_speed = speed

    def set_random_color(self):
        self.image.fill((random_255(), random_255(), random_255()))

