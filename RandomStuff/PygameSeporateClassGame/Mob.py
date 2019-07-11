import pygame
import random
from os import path

class MobSprite(pygame.sprite.Sprite):
    def __init__(self,screen_width, screen_height):
        pygame.sprite.Sprite.__init__(self)
        self.display_width = screen_width
        self.display_height = screen_height

        # set up assets folders
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, "img")

        self.mob_img = pygame.image.load(path.join(img_folder, "meteorBrown_med1.png")).convert()
        self.image = pygame.transform.scale(self.mob_img, (50, 50))
        self.image.set_colorkey((0,0,0))
        # self.image = pygame.Surface((50, 50))
        # self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(screen_width - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(2, 4)
        self.speedx = random.randrange(-3, 3)
        self.bouncey = True

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.left < 0 or self.rect.right > self.display_width:
            self.speedx *= -1
        if self.rect.top > self.display_height + 10:
            self.rect.x = random.randrange(self.display_width - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(2, 5)
        if self.bouncey:
            if self.rect.top < 0:
                self.rect.top = 0
                self.speedy *= -1
            if self.rect.bottom > self.display_height:
                # self.rect.bottom = self.display_height
                # self.speedy *= -1
                self.kill()
