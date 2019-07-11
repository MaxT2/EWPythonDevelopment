# import pygame library so we can use it!
import pygame
import random
from PythonCodingClub import pygameColors

# class definitions
class RainDrop(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        pygame.sprite.Sprite.__init__(self)
        # setup random numbers
        self.x_speed = 0
        # set random drop speed
        self.y_speed = random.randint(12, 16)
        # store screen width
        self.display_width = screen_width
        # pygame image stuff
        # set size based on random drop speed
        self.image = pygame.Surface((5, self.y_speed*1.5))
        self.image.fill((99, 211, 255))
        # set bounding box and position
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, self.display_width), random.randint(-1000, -100))

    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        # check to see if sprite left screen and reverse direction
        if self.rect.top > display_height:
            self.rect.center = (random.randint(0, self.display_width), random.randint(-100, -50))

# game code that needs to run only once

pygame.init()




# setup display dimensions
display_width = 1000
display_height = 1000
gameSurface = pygame.display.set_mode((display_width, display_height))
# pygame.display.set_caption('Window Caption!')

# setup game clock
FPS = 60
clock = pygame.time.Clock()

# setup game resources
# color definitions

# create a sprite group to keep track of sprites
all_sprites = pygame.sprite.Group()

for x in range(100):
    # check if a sprite was "killed" and we need to generate a new raindrop
    all_sprites.add(RainDrop(display_width, display_height))

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

    # UPDATE STUFF
    if (len(all_sprites) < 100):
        all_sprites.add()


    # only update FPS (60) times a second
    clock.tick(FPS)

    # run update on all sprites in all_sprites group
    all_sprites.update()

    # DRAW STUFF
    # clear display every frame(redraw background)
    gameSurface.fill(pygameColors.BLACK)
    # draw all sprites in all_sprites groups
    all_sprites.draw(gameSurface)

    # update and redraw entire screen
    pygame.display.flip()
    # update some of the screen
    # pygame.display.update()
