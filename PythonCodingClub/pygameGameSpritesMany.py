# import pygame library so we can use it!
import pygame
import random
from PythonCodingClub import pygameColors

# run initialization code on the library

pygame.init()

# setup display dimensions
display_width = 1000
display_height = 1000
FPS = 30

gameSurface = pygame.display.set_mode((display_width, display_height))
# pygame.display.set_caption('Window Caption!')


# game code that needs to run only once

# create game clock
clock = pygame.time.Clock()

# create a sprite group to keep track of sprites
all_sprites = pygame.sprite.Group()


class EnemyRandom(pygame.sprite.Sprite):
    import random

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.color = (random.randint(100,255),random.randint(100,255),random.randint(100,255))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0,display_width), random.randint(0,display_width))
        self.x_speed = random.randint(-3,3)
        if self.x_speed == 0:
            self.x_speed += 1
        self.y_speed = random.randint(-3,3)
        if self.y_speed == 0:
            self.y_speed += 1

    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        x,y = self.rect.center
        if x > 1000 or x < 0:
            self.x_speed *= -1
            self.color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
            self.image.fill(self.color)
        if y > 1000 or y < 0:
            self.y_speed *= -1
            self.color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
            self.image.fill(self.color)

for x in range(100):
    player = EnemyRandom()
    all_sprites.add(player)



# fill entire screen with color
gameSurface.fill(pygameColors.BLACK)


# main game loop
running = True  # when running is True game loop will run
while running == True:
    # get input events and respond to them
    # if event is .QUIT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(FPS)

    # game code that repeats every frame
    # clear display (redraw background)
    # gameSurface.fill(pygameColors.BLACK)


    # update
    all_sprites.update()

    # draw
    # draw a background each frame
    # gameSurface.fill(BLACK)
    # draw all sprites
    all_sprites.draw(gameSurface)




    # pygame.draw.rect(gameSurface, r_color, [rectX, rectY, 25, 25])
    # pygame.draw.circle(gameSurface,r_color,(int(rectX),int(rectY)),25)
    # gameSurface.blit(image1, [rectX, rectY])


    # update and redraw entire screen
    pygame.display.flip()
    # update some of the screen
    # pygame.display.update()




class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(pygameColors.GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (display_width / 2, display_height / 2)
