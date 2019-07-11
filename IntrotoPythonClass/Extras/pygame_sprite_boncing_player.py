

#36-38




# import pygame library so we can use it!
import pygame
import random
# import colors from color.py

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (500, 500)
        self.x_speed = 15
        self.y_speed = 20
        self.rect.clamp_ip(game_surface.get_rect())

    def update(self):
        # self.rect.clamp_ip(game_surface.get_rect())
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        self.image.fill(random.randint)

# run initialization code on the library
pygame.init()

# setup display dimensions
display_width = 1200
display_height = 800

# create game surface (the screen we will draw onto)
game_surface = pygame.display.set_mode((display_width, display_height))
# pygame.display.set_caption('Window Caption!')

# setup game resources


# game code that needs to run only once
# fill entire screen with color
game_surface.fill((0, 0, 0))


# main game loop
running = True  # when running is True game loop will run
while running == True:
    # get input events and respond to them
    # if event is .QUIT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # game code that repeats every frame

    # update

    # draw

    # update and redraw entire screen
    pygame.display.flip()


