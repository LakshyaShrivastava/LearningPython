import sys
import time
from GameElements import *

pygame.init()
vec = pygame.math.Vector2  # Two Dimensional

HEIGHT = 450
WIDTH = 400
ACC = 0.5
FRIC = -0.12
FPS = 144

FramePerSec = pygame.time.Clock()
displaySurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DoodleJump")

background = pygame.image.load("background.png")

PT1 = Platform(WIDTH)
PT1.surf = pygame.Surface((WIDTH, 20))
# PT1.surf.fill((255, 0, 0))
PT1.rect = PT1.surf.get_rect(center=(WIDTH / 2, HEIGHT - 10))
PT1.moving = False
PT1.point = False

P1 = Player()

all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()
coins = pygame.sprite.Group()

all_sprites.add(PT1)
all_sprites.add(P1)
platforms.add(PT1)


def plat_gen():
    while len(platforms) < 6:
        width = random.randrange(50, 100)
        p = Platform()
        C = True

        while C:
            p = Platform()
            p.rect.center = (random.randrange(0, WIDTH - width), random.randrange(-50, 0))
            C = check_plat_gen(p, platforms)
        p.generateCoin(coins, P1)
        platforms.add(p)
        all_sprites.add(p)


def check_plat_gen(platform, groups):
    if pygame.sprite.spritecollideany(platform, groups):
        return True
    else:
        for entity in groups:
            if entity == platform:
                continue
            if (abs(platform.rect.top - entity.rect.bottom) < 40) and (
                    abs(platform.rect.bottom - entity.rect.top) < 40):
                return True
        C = False


for x in range(random.randint(6,7)):
    C = True
    pl = Platform()
    while C:
        pl = Platform()
        C = check_plat_gen(pl, platforms)
    pl.generateCoin(coins, P1)
    platforms.add(pl)
    all_sprites.add(pl)


while True:
    P1.update(platforms)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                P1.jump(platforms)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                P1.cancel_jump()

    if P1.rect.top > HEIGHT:
        for entity in all_sprites:
            entity.kill()
            time.sleep(1)
            displaySurface.fill((255, 0, 0))
            f = pygame.font.SysFont("Verdana", 20)
            g = f.render(str(P1.score), True, (123, 255, 0))
            displaySurface.blit(g, (WIDTH/2, 10))
            pygame.display.update()
            time.sleep(1)
            pygame.quit()
            sys.exit()

    if P1.rect.top <= HEIGHT / 3:
        P1.pos.y += abs(P1.vel.y)
        for plat in platforms:
            plat.rect.y += abs(P1.vel.y)
            if plat.rect.top >= HEIGHT:
                plat.kill()

    for coin in coins:
        coin.rect.y += abs(P1.vel.y)
        if coin.rect.top >= HEIGHT:
            coin.kill()

    plat_gen()
    displaySurface.blit(background, (0, 0
                                     ))
    f = pygame.font.SysFont("Verdana", 20)
    g = f.render(str(P1.score), True, (123, 255, 0))
    displaySurface.blit(g, (WIDTH/2, 10))

    for entity in all_sprites:
        displaySurface.blit(entity.surf, entity.rect)
        if type(entity) == Platform:
            entity.move(P1)
        elif type(entity) == Player:
            entity.move()

    for coin in coins:
        displaySurface.blit(coin.image, coin.rect)
        coin.update(P1)

    pygame.display.update()
    FramePerSec.tick(FPS)
