# import pygame library so we can use it
import pygame

from PythonCodingClub import pygameColors
from ClassDevEWPygame.RandomStuff.PygameSeporateSpriteClasses import PlayerFollowMouse

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

enemy = PlayerFollowMouse.PlayerSprite(display_width, display_height)

# color definitions

# create a sprite group to keep track of sprites
all_sprites = pygame.sprite.Group()

all_sprites.add(enemy)

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
