import random
import pygame


class Enemy(pygame.sprite.Sprite):

    def __init__(self, screen_width, screen_height):
        pygame.sprite.Sprite.__init__(self)

        # store screen size to keep enemy on screen
        self.display_width = screen_width
        self.display_height = screen_height

        # set image of enemy
        # create rectangle surface of size x,y
        self.image = pygame.Surface((100, 100))
        # fill new rectangle with a color
        self.image.fill((0, 0, 255))
        # set bounding box rectangle position and dimensions using size of surface
        self.rect = self.image.get_rect()
        # sets the inital position of the enemy

        self.rect.center = (200, 200)
        # start at random position
        self.rect.center = ((random.randint(50, self.display_width - 50), random.randint(-400, -200)))
        # sets the speed of the enemy
        self.x_speed = 0
        self.y_speed = 5
        self.y_speed = random.randint(5, 10)


    def update(self):
        # do noting at first because speeds are 0
        # update position based on speeds
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        if self.rect.top > self.display_height:
            # reset back to the top of the screen
            self.rect.center = ((random.randint(50, self.display_width - 50), random.randint(-400, -200)))


    # def remove(self):
    #     self.kill()






        #
        # # remove sprite when it leaves the bottom of the screen
        # if(self.rect.top > self.display_height):
        #     self.kill()


