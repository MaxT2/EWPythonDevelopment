


# import pygame library so we can use it!
import pygame

# define player sprite
class Enemy(pygame.sprite.Sprite):
    def __init__(self,screen_width,screen_height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width / 2, screen_height / 2)
        self.x_speed = 15
        self.y_speed = 20

    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        # check to see if sprite left screen and reverse direction
        if self.rect.right > 1000:
            # to make sure you never get stuck
            # self.rect.right = 999
            # reverse direction
            self.x_speed *= -1

        if self.rect.left < 0:
            self.x_speed *= -1

        if self.rect.bottom > 1000:
            self.y_speed *= -1

        if self.rect.top < 0:
            self.y_speed *= -1


# game code that needs to run only once
pygame.init()

# setup display dimensions
display_width = 1000
display_height = 1000
gameSurface = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Window Caption!')

# setup game clock
FPS = 60
clock = pygame.time.Clock()

# setup game resources

# create a sprite group to keep track of sprites
all_sprites = pygame.sprite.Group()
enemy1 = Enemy(display_width, display_height)
all_sprites.add(enemy1)

# fill entire screen with black
gameSurface.fill(0)

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
    gameSurface.fill(0)
    # draw all sprites in all_sprites group
    all_sprites.draw(gameSurface)

    # update and redraw entire screen
    pygame.display.flip()
    # update some of the screen
    # pygame.display.update()
