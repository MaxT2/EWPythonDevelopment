import pygame

from ClassDevEWPygame.ShooterGame.shooterGameMultiClass import player_img, BLACK, WIDTH, HEIGHT, Bullet, all_sprites, bullets


class PlayerSprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (50, 38))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center.x = WIDTH/2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_a]:
            self.speedx = -5
        if pressed[pygame.K_d]:
            self.speedx = 5
        if pressed[pygame.K_w]:
            self.speedy = -5
        if pressed[pygame.K_s]:
            self.speedy = 5
        if pressed[pygame.K_LEFT]:
            self.image = pygame.transform.rotate(self.image, 5)
        if pressed[pygame.K_RIGHT]:
            self.image = pygame.transform.rotate(self.image, -5)
        if self.rect.left < 0:
            self.speedx = 0
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.speedx = 0
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.speedy = 0
            self.rect.top  = 0
        if self.rect.bottom > HEIGHT:
            self.speedy = 0
            self.rect.bottom = HEIGHT
        self.rect.y += self.speedy
        self.rect.x += self.speedx



    def shoot(self):
        ## tripple shot
        # for i in range(3):
        #     bullet = Bullet(self.rect.left + (20 *i) , self.rect.top)
        #     all_sprites.add(bullet)
        #     bullets.add(bullet)
        bullet = Bullet(self.rect.centerx , self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)