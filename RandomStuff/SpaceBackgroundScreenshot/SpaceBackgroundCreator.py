# import pygame library so we can use it!
import pygame
import random
from pathlib import Path
from PythonCodingClub import pygameColors

# class definitions
class Star(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        pygame.sprite.Sprite.__init__(self)
        # setup random numbers
        self.x_speed = 0
        self.y_speed = 0
        #setup pygame image stuff
        self.random_size = random.randint(1, 5)
        self.image = pygame.Surface((self.random_size, self.random_size))
        self.image.fill((255, 255, 255))
        # setup create bounding box and set position
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, screen_width), random.randint(0, screen_height))


    # def update(self):
    #     self.rect.x += self.x_speed
    #     self.rect.y += self.y_speed
    #
    #     # check to see if sprite left screen and reverse direction
    #     if self.rect.top > display_height:
    #         self.kill()
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

# create stars and put them into all_sprites group so we can update and draw them
for x in range(200):
    all_sprites.add(Star(display_width, display_height))

# draw the display sprites once and show them
# fill entire screen with color
gameSurface.fill(pygameColors.BLACK)
all_sprites.draw(gameSurface)
pygame.display.flip()

# save a screenshot of the background
# check if file exists is not working properly so it always takes a screenshot
image_screen_shot = Path("/spaceBackground.jpg")
if image_screen_shot.exists():
    print("screenshot already exists")
else:
    pygame.image.save(gameSurface, "screenshot1.jpg")
    print("screenshot saved")




# main game loop
running = True  # when running is True game loop will run
while running == True:
    # get input events and respond to them
    # if event is .QUIT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # UPDATE STUFF

    # if all_sprites.__sizeof__() < 50:
    #     all_sprites.add(Star(display_width, display_height))
    # only update FPS (60) times a second
    clock.tick(FPS)

    # run update on all sprites in all_sprites group
    # all_sprites.update()

    # DRAW STUFF
    # clear display every frame(redraw background)
    # gameSurface.fill(pygameColors.BLACK)
    # draw all sprites in all_sprites groups
    # all_sprites.draw(gameSurface)

    # update and redraw entire screen
    # pygame.display.flip()
    # update some of the screen
    # pygame.display.update()
