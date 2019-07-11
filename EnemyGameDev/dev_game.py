# init Section
import pygame
from os import path
from EnemyGameDev.enemy import Enemy
from EnemyGameDev.player import Player
from EnemyGameDev.enemy2 import Enemy2
from EnemyGameDev.bullet import Bullet
from EnemyGameDev.enemy_barricade import EnemyBarricade
import time

pygame.init()


def create_player():
    # define player and add to groups.
    # Players are added to the all_sprite and all_players groups
    player = Player(display_width, display_height)
    all_sprites.add(player)
    all_players.add(player)
    return player

def create_enemy():
    enemy1 = Enemy(display_width, display_height)
    global all_sprites
    all_sprites.add(enemy1)
    global all_enemies
    all_enemies.add(enemy1)
    global enemy_count
    enemy_count = enemy_count + 1


# setup game and sound folders
game_folder = path.dirname(__file__)
sound_folder = path.join(game_folder, "sound")
img_folder = path.join(game_folder, "img")

#
# setup sounds
# set music sound
pygame.mixer.music.load(path.join(sound_folder, "lights.wav"))
# store collision sound
collide_sound = pygame.mixer.Sound(path.join(sound_folder, "Blip_Select.wav"))

# setup display
display_width = 1000
display_height = 1000
gameSurface = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Tristen's Game")

# setup background image
background_image = pygame.image.load(path.join(img_folder, "background.png")).convert()
# scale background image to the size of the screen
background_image = pygame.transform.scale(background_image, (1000, 1000))




# setup colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# setup game clock
FPS = 60
clock = pygame.time.Clock()

# define sprite groups
# keep track of all sprites for update and drawing
all_sprites = pygame.sprite.Group()
# keep track of all players
all_players = pygame.sprite.Group()
# keep track of all enemies
all_enemies = pygame.sprite.Group()
# keep track of 2nd type of enemies
all_avoid_enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# variable for storing score as text
score = 0
font_small = pygame.font.Font(None, 36)
font_large = pygame.font.Font(None, 200)

# setup game over text
game_over_text = font_large.render("GAME OVER", 1, (255, 255, 255))

# create player
player1 = create_player()

# enemy player count variable
enemy_count = 0
spawn_number = 1
avoid_spawn_number = 3
# play variable used to "pause game"
play = True

# create first wave of enemies
for x in range(spawn_number):
    # create an enemy
    # enemies are added to the all_sprites and all_enemies groups
    enemy = Enemy(display_width, display_height)
    all_sprites.add(enemy)
    all_enemies.add(enemy)
    enemy_count = enemy_count + 1

# start game music and loop indefinitely (-1)
pygame.mixer.music.play(-1)

# Main Game loop:
running = True
while running == True:

    #testing space


    # every frame......
    # get list of pressed keyboard buttons
    pressed_keys = pygame.key.get_pressed()
    # manage events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # check keys being pressed for player movement
    # if left key pressed move left
    if pressed_keys[pygame.K_LEFT]:
        player1.moveLeft()
    # if right key pressed move right
    elif pressed_keys[pygame.K_RIGHT]:
        player1.moveRight()
    else:
        player1.moveStopX()

    # if up key pressed move up
    if pressed_keys[pygame.K_UP]:
        player1.moveUp()
    # if right key pressed move right
    elif pressed_keys[pygame.K_DOWN]:
        player1.moveDown()
    else:
        player1.moveStopY()

    if pressed_keys[pygame.K_SPACE]:
        bullet = Bullet(display_width, display_height, player1.rect.x, player1.rect.y - 45)
        all_sprites.add(bullet)
        bullets.add(bullet)
    clock.tick(FPS)
    # Run updates on sprites in the all_sprites list
    if play:
        all_sprites.update()

    # check players and enemies for collisions
    hits = pygame.sprite.groupcollide(all_enemies, all_players, True, False)
    for enemy in hits:
        # play collide sound
        pygame.mixer.Sound.play(collide_sound)
        # add 5 to players score
        score = score + 5
        # remove one enemy from enemy_count
        enemy_count = enemy_count - 1

    # check players and enemy2 for collisions
    hits = pygame.sprite.groupcollide(all_avoid_enemies, all_players, False, True)
    if len(hits) > 0:
        play = False

        gameSurface.blit(text, (display_width/2, display_width/2))

        time.sleep(2)
        all_sprites.empty()
        player1 = create_player()
        create_enemy()
        play = True

    # check to see if there are no more ememies and spawn next wave
    if enemy_count == 0:
        # add one more enemie to spawn number
        spawn_number = spawn_number + 1
        for x in range(spawn_number):
            # create an enemy
            new_enemy = Enemy(display_width, display_height)
            all_sprites.add(new_enemy)
            all_enemies.add(new_enemy)

            # add one ememy to our enemy_count
            enemy_count = enemy_count + 1
        for i in range(avoid_spawn_number):
            # also spawn 2nd enemies
            # create an enemy
            new_enemy = Enemy2(display_width, display_height)
            all_sprites.add(new_enemy)
            all_avoid_enemies.add(new_enemy)

    # draw stuff and then update screen
    # gameSurface.fill(BLACK)
    # display the background image we created. Draw it at (0,0)
    gameSurface.blit(background_image, [0, 0])
    # draw all sprites
    all_sprites.draw(gameSurface)

    # print the number of sprites in a group
    # all_sprites_list = len(all_sprites.sprites())
    # print(all_sprites_list)

    # draw score text on screen
    text = font_small.render("Score: " + score.__str__(), 20, (255, 255, 255))
    gameSurface.blit(text, (50, 50))
    if play is False:
        gameSurface.blit(game_over_text, (display_width / 2 - game_over_text.get_rect().width/2, display_width / 2 - game_over_text.get_rect().height/2))
    # update display
    pygame.display.flip()


