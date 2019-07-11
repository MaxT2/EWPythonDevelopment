# pygame basic sprite setup - base of all pygame projects

# import pygame library so we can use it!
from os import path
from time import sleep

import pygame
from player import Player
from enemy import Enemy

# game code that needs to run only once

# initialize pygame code
pygame.init()

# setup display size
width = 1200
height = 800

# create game surface (the screen we will draw onto)
game_surface = pygame.display.set_mode((width, height))
# pygame.display.set_caption('Window Caption!')

# setup assets folders
game_folder = path.dirname(__file__)
background = pygame.image.load(path.join(game_folder, "blue_guy.png")).convert()
background = pygame.transform.scale(background, (1200, 800))
background.set_colorkey((0, 0, 0))

# setup framerate
clock = pygame.time.Clock()
FPS = 60

# setup game resources
# define colors - CTR-SHIFT-A --> color picker
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# score
score = 0

# create font to display text
font = pygame.font.Font(None, 36)

#setup sprite groups
all_sprites = pygame.sprite.Group()
all_players = pygame.sprite.Group()
all_enemies = pygame.sprite.Group()

# create player and enemy sprite objects and add them to groups
player_1 = Player(width, height)
# add to all sprites group
all_sprites.add(player_1)
# add to player group
all_players.add(player_1)

for x in range(5):
    # create enemy and add it to groups
    enemy_1 = Enemy(width, height)
    # add to all sprites group
    all_sprites.add(enemy_1)
    # add to enemies group
    all_enemies.add(enemy_1)


# fill entire screen with color
game_surface.fill(WHITE)


# main game loop
running = True
# when running is True game loop will run
while running == True:
    # get input events and respond to them
    # if event is .QUIT
    for event in pygame.event.get():
        # if we close the game window, stop the loop
        if event.type == pygame.QUIT:
            running = False

    # game code that repeats every frame
    # store and print current mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()
    print("X = ", mouse_x, "Y = ", mouse_y)

    # limit the frame rate of your game
    clock.tick(FPS)

    # update stuff
    # update all sprites in group
    all_sprites.update()

    # CHECK FOR COLLISIONS
    # collecting sprites
    # hit_list = pygame.sprite.groupcollide(all_enemies, all_players, True, False)
    # for enemy in hit_list:
    #     print("You Collided!")
    #     # get points for everyone collected

    # avoiding sprites
    hit_list = pygame.sprite.groupcollide(all_enemies, all_players, False, True)
    for enemy in hit_list:
        print("You Collided!")
        # game over!

        #delay
        # font render and display a game over screen
        game_surface.fill((0,0,0))
        text = font.render("GameOver",1,WHITE)
        game_surface.blit(text,(width/2, height/2))
        pygame.display.flip()
        sleep(10000)

        running = False

    # check enemies to see if they left the screen



    # draw stuff
    # draw background before everything else
    game_surface.fill(WHITE)
    game_surface.blit(background,(0,0))
    # draw all sprites in group on game_surface
    all_sprites.draw(game_surface)
    # lastly: update and redraw entire screen

    # draw score  text on screen just before updaing
    #font.render("text",antialias,color,background(optional))
    text = font.render("Score: " + str(score), 1, WHITE)
    # this displays the text on the screen at a location
    # blit(renderedText, (x,y)
    game_surface.blit(text, (50, 50))
    pygame.display.flip()


def increase_score():
    global score
    score += 1

