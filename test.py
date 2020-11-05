import pygame
from pygame.locals import *
import sys
pygame.init()
width, height = 680,720
screen = pygame.display.set_mode((width,height))
while True:
    screen.fill((150, 150, 150))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.draw.polygon(screen, (0, 0, 0),((0, 100), (0, 200), (200, 200), (200, 300), (300, 150), (200, 0), (200, 100)))

    pygame.display.update()

pygame.quit()