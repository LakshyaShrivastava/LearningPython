import math
import random
import pygame


def distanceBetweenTwoPoints(first_point, second_point):
    x1 = first_point[0]
    y1 = first_point[1]
    x2 = second_point[0]
    y2 = second_point[1]
    return math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))


class ClickableCircle:
    def __init__(self, center, radius, color=(0, 0, 0)):
        self.center = center
        self.radius = radius
        self.visible = True
        self.color = color

    def isPointInside(self, click_Location):
        distance_Between_Center_And_Click = distanceBetweenTwoPoints(self.center, click_Location)
        retVal = False
        if distance_Between_Center_And_Click <= self.radius:
            retVal = True
        return retVal

    def draw(self, surface):
        if not self.visible:
            self.center[0] = random.random() * pygame.Surface.get_width(surface)
            self.center[1] = random.random() * pygame.Surface.get_height(surface)
            self.setVisible(True)

        pygame.draw.circle(surface, self.color, self.center, self.radius)

    def setVisible(self, state):
        self.visible = state
