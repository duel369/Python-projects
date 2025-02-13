import pygame, sys
from pygame.locals import *
import random, time
import os

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load(os.path.join("DodgeCars/Assets", "AnimatedStreet.png"))

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Car Surfing")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join("DodgeCars/Assets", "Enemy.png"))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if (self.rect.bottom > SCREEN_HEIGHT):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(30, SCREEN_WIDTH-30), 0)

#    def draw(self, surface):
#        surface.blit(self.image, self.rect)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join("DodgeCars/Assets", "Player.png"))
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH/2-40, SCREEN_HEIGHT-50)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-7, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(7, 0)

#    def draw(self, surface):
#        surface.blit(self.image, self.rect)

P1 = Player()
E1 = Enemy()

enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

#screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#player = pygame.Rect((300, 250, 50, 50))

run = True
while run == True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == INC_SPEED:
            SPEED += 0.5

    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))

    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound(os.path.join("DodgeCars/Assets", 'crash.wav')).play()
        time.sleep(0.5)

        finalScore = font_small.render("Score: " +str(SCORE), True, BLACK)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        DISPLAYSURF.blit(finalScore, (SCREEN_WIDTH/2-40, 380))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(4)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)

pygame.quit()
