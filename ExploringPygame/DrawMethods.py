import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))


def drawRect(surface, color, rectangle):
    pygame.draw.rect(surface, color, rectangle)


def drawCircle(surface, color, center, radius):
    pygame.draw.circle(surface, color, center, radius)


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    drawRect(screen, (0, 0, 0), pygame.Rect(30, 30, 60, 60))
    drawCircle(screen, (0, 255, 0), (500, 500), 50)

    pygame.display.flip()
