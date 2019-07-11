# Pygame template - skeleton for a new pygame project
import pygame
import random
from os import path


WIDTH = 400
HEIGHT = 600
FPS = 60

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (100, 100, 200)
YELLOW = (255,255,0)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Astroids")
clock = pygame.time.Clock()

# set up assets folders
game_folder = path.dirname(__file__)
img_folder = path.join(game_folder, "img")


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (50, 38))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.bottom = HEIGHT - 10
        self.speed_x = 0
        self.speed_y = 0

    def update(self):
        self.speed_x = 0
        self.speed_y = 0
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_a]:
            self.speed_x = -5
        if pressed[pygame.K_d]:
            self.speed_x = 5
        if pressed[pygame.K_w]:
            self.speed_y = -5
        if pressed[pygame.K_s]:
            self.speed_y = 5
        # if pressed[pygame.K_LEFT]:
        #     self.image = pygame.transform.rotate(self.image,5)
        # if pressed[pygame.K_RIGHT]:
        #     self.image = pygame.transform.rotate(self.image,-5)
        if self.rect.left < 0:
            self.speed_x = 0
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.speed_x = 0
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.speed_y = 0
            self.rect.top  = 0
        if self.rect.bottom > HEIGHT:
            self.speed_y = 0
            self.rect.bottom = HEIGHT
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x

    def shoot(self):
        # triple shot
        # for i in range(3):
        #     bullet = Bullet(self.rect.left + (20 *i) , self.rect.top)
        #     all_sprites.add(bullet)
        #     bullets.add(bullet)
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = meteor_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(2, 8)
        self.speed_x = random.randrange(-3, 3)
        self.bounce_y = False

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speedy
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.speed_x *= -1
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(2, 5)
        if self.bounce_y:
            if self.rect.top < 0:
                self.rect.top = 0
                self.speedy *= -1
            if self.rect.bottom > HEIGHT:
                self.rect.bottom = HEIGHT
                self.speedy *= -1


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image .get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()




# load all game objects
background = pygame.image.load(path.join(img_folder, "starfield.png")).convert()
background_rect = background.get_rect()
player_img = pygame.image.load(path.join(img_folder, "playerShip1_blue.png")).convert()
meteor_img = pygame.image.load(path.join(img_folder, "meteorBrown_med1.png")).convert()
bullet_img = pygame.image.load(path.join(img_folder, "laserRed02.png")).convert()

# create sprite Groups
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# create player + mobs
player = Player()

# add player to sprite group
all_sprites.add(player)

for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)


pygame.key.set_repeat(1,100)

# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                if player.alive():
                    player.shoot()
            if event.key == pygame.K_l:
                player = Player()
                all_sprites.add(player)



    # Update
    all_sprites.update()

    # check to see if any bullets hit mobs
    hits = pygame.sprite.groupcollide(bullets, mobs, True, True)
    for hit in hits:
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)

    # check to see if any mobs hit player False - should sprite be removed?
    # store in a list
    hits = pygame.sprite.spritecollide(player, mobs, True)
    if hits:
        player.kill()
    #     running = False



    # Draw / render
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
