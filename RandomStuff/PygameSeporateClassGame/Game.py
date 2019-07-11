
# import pygame library so we can use it
import pygame
from PythonCodingClub import pygameColors
from RandomStuff.PygameSeporateClassGame.Player import PlayerSprite
from RandomStuff.PygameSeporateClassGame.Mob import MobSprite
from os import path

# game code that needs to run only once

pygame.init()

# setup display dimensions
display_width = 800
display_height = 800
gameSurface = pygame.display.set_mode((display_width, display_height))
# pygame.display.set_caption('Window Caption!')

# setup game clock
FPS = 60
clock = pygame.time.Clock()

# setup game resources
score = 0
# text stuff
font = pygame.font.Font(None, 36)
text = font.render(score.__str__(), 1, (255, 255, 255))

# setup sounds and sound folder
game_folder = path.dirname(__file__)
img_folder = path.join(game_folder, "sound")



#define player 1
player1 = PlayerSprite(display_width, display_height, 50)

# color definitions

# create sprite groups to keep track of sprites
all_sprites = pygame.sprite.Group()
all_players = pygame.sprite.Group()
all_mobs = pygame.sprite.Group()

# add player 1 to sprite groups
all_sprites.add(player1)
all_players.add(player1)

# create mobs
# mob1 = MobSprite(display_width, display_height)
# all_sprites.add(mob1)
# all_mobs.add(mob1)

for x in range(5):
        mob = MobSprite(display_width, display_height)
        all_sprites.add(mob)
        all_mobs.add(mob)

# mob2 = MobSprite(display_width, display_height)
# all_sprites.add(mob2)
# all_mobs.add(mob2)

# fill entire screen with color
gameSurface.fill(pygameColors.BLACK)

# main game loop
running = True  # when running is True game loop will run
while running == True:
    # get list of pressed buttons
    pressed = pygame.key.get_pressed()

    # get input events and respond to them
    # if event is .QUIT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if pressed[pygame.K_LEFT]:
        player1.move_left(20)
    if pressed[pygame.K_RIGHT]:
        player1.move_right(20)
    # if pressed[pygame.K_UP]:
    #     player1.move_left(20)
    # if pressed[pygame.K_DOWN]:
    #     player1.move_right(20)

    # UPDATE STUFF
    # only update FPS (60) times a second
    clock.tick(FPS)


    # spawn new stuff if needed
    # if len(all_mobs) < 5:
    #     mob = MobSprite(display_width, display_height)
    #     all_sprites.add(mob)
    #     all_mobs.add(mob)

    # run update on all sprites in all_sprites group
    all_sprites.update()

    # check for collisions before we draw stuff
    # check to see if any bullets hit mobs
    # something to look up - what is a "hit"
    hits = pygame.sprite.groupcollide(all_players, all_mobs, False, True)
    for hit in hits:
        score += 1
        m = MobSprite(display_width, display_height)
        all_sprites.add(m)
        all_mobs.add(m)



    # DRAW STUFF
    # clear display every frame(redraw background)
    gameSurface.fill(pygameColors.BLACK)
    # draw all sprites in all_sprites groups
    all_sprites.draw(gameSurface)

    # draw score
    text = font.render("Score: " + score.__str__(), 1, (255, 255, 255))
    gameSurface.blit(text, (50, 50))

    # update and redraw entire screen
    # pygame.display.flip()
    # update some of the screen
    pygame.display.update()
