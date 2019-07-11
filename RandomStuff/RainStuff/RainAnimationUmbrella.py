# NOT WORKING, something is wrong with the "umbrella"



# import pygame library so we can use it!
import pygame
import random
from PythonCodingClub import pygameColors

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
# class definitions
class RainDrop(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        pygame.sprite.Sprite.__init__(self)
        # setup random numbers
        self.x_speed = 0
        # set random drop speed
        self.y_speed = random.randint(12, 30)
        # pygame image stuff
        # set size based on random drop speed
        self.image = pygame.Surface((5, self.y_speed*1.5))
        self.image.fill((99, 211, 255))
        # set bounding box and position
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, screen_width), random.randint(-100,-50))

    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        # check to see if sprite left screen and reverse direction
        if self.rect.top > display_height:
            self.kill()
# game code that needs to run only once


class Umbrella(pygame.sprite.Sprite):
    # class variables shared by all instances of this class
    image = pygame.Surface((100, 100))  # created on the fly
    image.set_colorkey((0, 0, 0))  # black transparent
    pygame.draw.circle(image, (255, 0, 0), (50, 50), 50, 2)  # red circle
    image = image.convert_alpha()
    # code for each individual class instance

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.groups)  # THE most important line !
        self.image = Umbrella.image  # make class-variable an instance variable
        self.rect = self.image.get_rect()
        self.radius = 50  # for collide check

    def update(self, seconds):
        # no need for seconds but the other sprites need it
        self.rect.center = pygame.mouse.get_pos()


# color definitions

# ------------ SPRITES ------------
# create a sprite group to keep track of sprites
all_sprites = pygame.sprite.Group()

# add player to sprite group first
all_sprites.add(Umbrella())

# ------------ Display ------------
# fill entire screen with color
gameSurface.fill(pygameColors.BLACK)

# ------------ MAIN GAME LOOP ------------
running = True  # when running is True game loop will run
while running == True:
    # get input events and respond to them
    # if event is .QUIT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ------------ UPDATE STUFF ------------
    # check if a sprite was "killed" and we need to generate a new raindrop
    if all_sprites.__sizeof__() < 50:
        all_sprites.add(RainDrop(display_width, display_height))
    # only update FPS (60) times a second
    clock.tick(FPS)

    # run update on all sprites in all_sprites group
    all_sprites.update()

    # ------------ DRAW STUFF ------------
    # clear display every frame(redraw background)
    gameSurface.fill(pygameColors.BLACK)
    # draw all sprites in all_sprites groups
    all_sprites.draw(gameSurface)
    # update and redraw entire screen
    pygame.display.flip()
    # update some of the screen
    # pygame.display.update()
