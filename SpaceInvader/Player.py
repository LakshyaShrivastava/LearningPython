import pygame


class Player:
    def __init__(self, x, y, imageName):
        self.x = x
        self.y = y
        self.image = pygame.image.load(imageName)

    def move(self, changeInX):
        self.x += changeInX

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def checkBounds(self):
        if self.x <= 0:
            self.x = 0
        elif self.x >= 736:
            self.x = 736
