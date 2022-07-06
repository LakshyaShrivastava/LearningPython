import pygame
import random
from Player import Player
from Enemy import Enemy
from Bullet import Bullet
from pygame import mixer

# Initialize the pygame
pygame.init()

# Constants used in program
MOVEMENT_FACTOR = 5
NUM_OF_ENEMIES = 6

# Create the screen (Make window resizeable later)
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('background.png')

# Sound
mixer.music.load("background.wav")
mixer.music.play(-1)

# Window Title and Icon
pygame.display.set_caption("Space Invaders")
pygame.display.set_icon(pygame.image.load('SpaceShip.png'))

# Player (Change coordinates to scale with screen)
player = Player(370, 480, 'SpaceShip.png')
changeInX = 0

# Enemy
enemyList = []

for i in range(NUM_OF_ENEMIES):
    enemyList.append(Enemy(random.randint(0, 736), random.randint(50, 150), 'alien.png'))


# Bullet
bullet = Bullet(player.x, player.y, False, 'bullet.png')

# score
scoreValue = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10


def drawScreenElements():
    screen.blit(background, (0, 0))
    player.draw(screen)
    for i in range(NUM_OF_ENEMIES):
        enemyList[i].draw(screen)
    bullet.draw(screen)
    score = font.render("Score: " + str(scoreValue), True, (255,255,255))
    screen.blit(score, (textX,textY))


def moveScreenElements():
    player.move(changeInX)
    for i in range(NUM_OF_ENEMIES):
        enemyList[i].moveHorizontally()
    bullet.fire(screen)


def checkBoundsForScreenElements():
    player.checkBounds()
    for i in range(NUM_OF_ENEMIES):
        enemyList[i].checkBounds()
    bullet.checkBounds()



def checkCollisions():
    global scoreValue
    for i in range(NUM_OF_ENEMIES):
        isColliding = bullet.isColliding(enemyList[i])
        if isColliding:
            bullet.resetBullet()
            enemyList[i].resetEnemy()
            scoreValue += 1
            explosion = mixer.Sound("explosion.wav")
            explosion.play()
            break


def isGameOver():
    for i in range(NUM_OF_ENEMIES):
        if enemyList[i].y > 440:
            for enemy in enemyList:
                enemy.removeEnemyFromScreen()
            gameOverText()
            break

def gameOverText():
    gameOverFont = pygame.font.Font('freesansbold.ttf', 64)
    overText = gameOverFont.render("GAME OVER", True, (255,255,255))
    screen.blit(overText, (200,250))

# Infinite Loop which runs the game
running = True

while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                changeInX -= MOVEMENT_FACTOR
            if event.key == pygame.K_RIGHT:
                changeInX += MOVEMENT_FACTOR
            if event.key == pygame.K_SPACE:
                if bullet.getState() is False:
                    bulletSound = mixer.Sound("laser.wav")
                    bulletSound.play()
                    bullet.setState(True)
                    bullet.setBulletStartLoc(player.x)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                changeInX = 0

    moveScreenElements()
    checkBoundsForScreenElements()
    checkCollisions()
    drawScreenElements()
    isGameOver()
    pygame.display.update()
