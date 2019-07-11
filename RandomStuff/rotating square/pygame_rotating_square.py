

#36-38




# import pygame library so we can use it!
import pygame
from os import path
import random
# import colors from color.py


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imageOriginal = player_img
        self.image = self.imageOriginal
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        # self.image = pygame.Surface((25, 25))
        # self.image.fill((0, 255, 0))
        # self.rect = self.image.get_rect()
        self.rect.center = (500, 500)
        self.x_speed = 0
        self.y_speed = 0
        self.angle = 0
        # self.rect.clamp_ip(game_surface.get_rect())

    def update(self):
        # pass
        # self.rect.clamp_ip(game_surface.get_rect())
        # self.rect.x += self.x_speed
        # lf.rect.y += self.y_speed
        # self.image.fill(random.randint)
        self.image = pygame.transform.rotate(self.imageOriginal, self.angle)
        self.angle += 1 % 360
        x,y = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


# run initialization code on the library
pygame.init()

# setup display dimensions
display_width = 1200
display_height = 800


# create game surface (the screen we will draw onto)
game_surface = pygame.display.set_mode((display_width, display_height))
# pygame.display.set_caption('Window Caption!')

# setup game resources
#clock
clock = pygame.time.Clock()
FPS = 60

# set up assets folders
game_folder = path.dirname(__file__)
img_folder = path.join(game_folder, "img")
player_img = pygame.image.load(path.join(img_folder, "playerShip1_blue.png")).convert()

# game code that needs to run only once
# fill entire screen with color
game_surface.fill((255, 255, 255))

# sprite group
all_sprites_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()


player_1 = Player()
all_sprites_group.add(player_1)
player_group.add(player_1)


# main game loop
running = True  # when running is True game loop will run
while running == True:
    # get input events and respond to them
    # if event is .QUIT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # game code that repeats every frame

    clock.tick(FPS)
    # update

    all_sprites_group.update()
    # draw
    game_surface.fill((255, 255, 255))
    # all_sprites_group.draw(game_surface)
    game_surface.blit(player_1.image, (500,500))
    # update and redraw entire screen
    pygame.display.flip()


