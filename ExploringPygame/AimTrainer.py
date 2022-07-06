import pygame
from ClickableCircle import ClickableCircle

pygame.init()
screen = pygame.display.set_mode((0, 0))
pygame.display.set_caption("Cyde117's Aim Trainer")
pygame.mouse.set_visible(False)
background = pygame.image.load('Images/Background.png')
hits = 0
total = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

target_color = (0, 197, 144)

targets = []
targets.append(
    ClickableCircle([pygame.Surface.get_width(screen) / 2, pygame.Surface.get_height(screen) / 2], 40, target_color))
targets.append(ClickableCircle([pygame.Surface.get_width(screen) / 2 + 100, pygame.Surface.get_height(screen) / 2], 40,
                               target_color))
targets.append(ClickableCircle([pygame.Surface.get_width(screen) / 2 - 100, pygame.Surface.get_height(screen) / 2], 40,
                               target_color))
targets.append(ClickableCircle([pygame.Surface.get_width(screen) / 2, pygame.Surface.get_height(screen) / 2 + 100], 40,
                               target_color))
targets.append(ClickableCircle([pygame.Surface.get_width(screen) / 2, pygame.Surface.get_height(screen) / 2 - 100], 40,
                               target_color))


def draw_stats(surface):
    percent = 0
    if total != 0:
        percent = hits / total * 100
    stats = font.render('Hits: ' + str(hits) + ' Total Shots: ' + str(total) + ' Accuracy: ' + str(percent) + '%', True, (255, 255, 0))
    screen.blit(stats, (textX, textY))


def draw_crosshair(surface, color):
    # Horizontal Link
    pygame.draw.line(surface, color, (pygame.mouse.get_pos()[0] - 10, pygame.mouse.get_pos()[1]),
                     (pygame.mouse.get_pos()[0] + 10, pygame.mouse.get_pos()[1]), width=4)
    # Vertical Link
    pygame.draw.line(surface, color, (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1] - 10),
                     (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1] + 10), width=4)


def draw_screen_elements():
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    for t in targets:
        t.draw(screen)
    draw_crosshair(screen, (0, 0, 0))
    draw_stats(screen)


is_running = True

while is_running:
    draw_screen_elements()
    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            total = total + 1
            for target in targets:
                if target.isPointInside(pygame.mouse.get_pos()):
                    target.setVisible(False)
                    hits = hits + 1
        elif event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            is_running = False
    pygame.display.flip()
