import pygame
import math


class Bullet:
    def __init__(self, x, y, state, imageName):
        self.x = x
        self.y = y
        self.image = pygame.image.load(imageName)
        self.bulletYChange = 10
        self.bulletX = 0
        self.state = state  # True = Fire Bullet

    def draw(self, screen):
        if self.state is True:
            screen.blit(self.image, (self.bulletX + 16, self.y + 10))

    def setState(self, state):
        self.state = state

    def setBulletStartLoc(self, x):
        self.bulletX = x

    def getState(self):
        return self.state

    def checkBounds(self):
        if self.y <= 0:
            self.state = False
            self.y = 480

    def fire(self, screen):
        if self.state is True:
            screen.blit(self.image, (self.bulletX, self.y))
            self.y -= self.bulletYChange

    def isColliding(self, enemy):
        distanceBetween = math.sqrt(math.pow(self.x - enemy.x, 2) + math.pow(self.y - enemy.y, 2))

        if distanceBetween < 27:
            return True
        else:
            return False

    def resetBullet(self):
        self.state = False
        self.y = 480
