# import pygame library so we can use it!
import pygame
import random
from pygame.locals import *

# run initialization code on the library
pygame.init()

# setup display dimensions
display_width = 1000
display_height = 1000

game_surface = pygame.display.set_mode((display_width, display_height))
# pygame.display.set_caption('Window Caption!')

# setup game resources
# color definitions
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (235, 235, 235)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (65, 231, 255)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)

# game code that needs to run only once
# rectangle variables
# rectX = 50
# rectY = 50
# rectXSpeed = 1.1
# rectYSpeed = .8

# create sprite groups
all_sprites = pygame.sprite.Group()
# mobs = pygame.sprite.Group()
# bullets = pygame.sprite.Group()



class Block(pygame.sprite.Sprite):
    # import random
    # import pygame
    # x = random.randint(1, 1000)
    # y = random.randint(1, 1000)
    width = 50
    height = 50
    # x = 500
    # y = 500
    xSpeed = 1
    ySpeed = 1
    screen = pygame.display.get_surface()

    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.centerx = 10
        self.rect.x = x
        self.rect.y = y
    def update(self):
        # self.rect.y += 1
        self.rect.x += self.xSpeed
        self.rect.y += self.ySpeed

        if self.rect.x > 1000 or self.rect.x < 1:
            self.xSpeed *= -1
        if self.rect.y > 1000 or self.rect.y < 1:
            self.ySpeed *= -1




blocks = []
# setup squares
for x in range(100):
    block = Block(random.randint(1,1000),random.randint(1,1000))
    all_sprites.add(block)


# fill entire screen with color
game_surface.fill(BLACK)

# main game loop
running = True  # when running is True game loop will run
while running == True:
    # get input events and respond to them
    # if event is .QUIT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # game code that repeats every frame
    # clear display (redraw background)
    # gameSurface.fill(BLACK)

    # update
    # rectX += rectXSpeed
    # rectY += rectYSpeed
    #
    # if rectX > display_width or rectX < 1:
    #     rectXSpeed *= -1
    # if rectY > display_height or rectY < 1:
    #     rectYSpeed *= -1

    game_surface.fill(BLACK)
    # for block in blocks:
    #     block.update()
    # # draw
    # # pygame.draw.rect(gameSurface, WHITE, [rectX, rectY, 50, 50])
    # for block in blocks:
    #     block.draw()
    #
    # for block in blocks:
    #     print(block)

    all_sprites.update()
    all_sprites.draw(game_surface)

    # update and redraw entire screen
    pygame.display.flip()
    # update some of the screen
    # pygame.display.update()



