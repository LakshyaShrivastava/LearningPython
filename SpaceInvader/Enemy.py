import pygame
import random


class Enemy:
    def __init__(self, x, y, imageName):
        self.x = x
        self.y = y
        self.image = pygame.image.load(imageName)
        self.X_MOVE_FACTOR = 2
        self.changeInX = self.X_MOVE_FACTOR
        self.changeInY = 40

    def moveHorizontally(self):
        self.x += self.changeInX

    def moveVertically(self):
        self.y += self.changeInY

    def checkBounds(self):
        if self.x <= 0:
            self.changeInX = self.X_MOVE_FACTOR
            self.moveVertically()

        elif self.x >= 736:
            self.changeInX = -self.X_MOVE_FACTOR
            self.moveVertically()


    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def resetEnemy(self):
        self.x = random.randint(0, 736)
        self.y = random.randint(50, 150)

    def removeEnemyFromScreen(self):
        self.y = 2000
