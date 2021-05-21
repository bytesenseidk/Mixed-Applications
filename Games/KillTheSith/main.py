import sys
import pygame
import random

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
BACKGROUND = pygame.image.load('background.jpg')
BACKGROUND_RECT = BACKGROUND.get_rect()
JET = pygame.image.load('jet.png')
ENEMY = pygame.image.load('enemy.png')
BULLET = pygame.image.load('laser.png')

FPS = 60

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = ENEMY
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WINDOW_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed = random.randrange(1, 5)
        self.health = 100

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > WINDOW_HEIGHT + 10:
            self.rect.x = random.randrange(WINDOW_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speed = random.randrange(1, 8)
            player.score -= 1

enemies = pygame.sprite.Group()

for i in range(7):
    enemy = Enemy()
    enemies.add(enemy)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = JET
        self.rect = self.image.get_rect()
        self.rect_centerx = 240
        self.rect.bottom = 770
        self.score = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = BULLET
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -15

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

bullets = pygame.sprite.Group()

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load('bgsound.wav')
pygame.mixer.music.play(-1)
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Kill The Sith')
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
all_sprites.add(enemy)

font = pygame.font.SysFont('comicsans', 30, True)
game_over = font.render("GAME OVER!", 1, RED)


run = True
while run:
    clock.tick(FPS)

    hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
    for hit in hits:
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)
        player.score += 1
        bullets.remove(hit)

    hits = pygame.sprite.spritecollide(player, enemies, False)
    if hits:
        screen.blit(game_over, (400, 400))
        run = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and len(bullets) < 10:
        player.shoot()

    if keys[pygame.K_LEFT] and player.rect.x > 0:
        player.rect.x -= 7

    elif keys[pygame.K_RIGHT] and player.rect.x < WINDOW_WIDTH - 50:
        player.rect.x += 7

    if keys[pygame.K_UP] and player.rect.y > 600:
        player.rect.y -= 3

    elif keys[pygame.K_DOWN] and player.rect.y < WINDOW_HEIGHT - 100:
        player.rect.y += 3

    all_sprites.update()

    text = font.render(f'Score: {player.score}', 1, RED)
    screen.blit(BACKGROUND, BACKGROUND_RECT)
    screen.blit(text, (650, 50))
    all_sprites.draw(screen)
    pygame.display.flip()
    screen.fill(BLACK)

pygame.quit()



"""
TODO:
    give enemies more life
    add different enemies
    add highscore
    add upgrades for player
"""
