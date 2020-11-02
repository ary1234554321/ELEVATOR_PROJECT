import pygame
from pygame.locals import *
import sys

pygame.init()
width, height = 680,720
screen = pygame.display.set_mode((width,height))

yellow = (255,255,102)
grey = (100,100,100)


colors = [grey,yellow]

buttonspress = []
for x in range(18):
    buttonspress.append([0,0])

def generalbkg():
    screen.fill((150,150,150))
    empty_rect = pygame.Rect(20, 10, 100,700)
    pygame.draw.rect(screen, (0, 0, 0), empty_rect, 3)
    empty_rect = pygame.Rect(140, 10, 130,700)
    pygame.draw.rect(screen, (0, 0, 0), empty_rect, 3)
    empty_rect = pygame.Rect(290, 10, 150,700)
    pygame.draw.rect(screen, (0, 0, 0), empty_rect, 3)
    empty_rect = pygame.Rect(460, 10, 200, 700)
    pygame.draw.rect(screen, (0, 0, 0), empty_rect, 3)

def flnums(buttonspress):
    count = 1
    for y in range(700,0,-70):
        if buttonspress[count-1][0] == 0 and buttonspress[count-1][1] == 0:
            pygame.draw.rect(screen,colors[0],(35,720-y,70,35))
        if buttonspress[count-1] == 1 or buttonspress[count-1] == 1:
            pygame.draw.rect(screen,colors[1],(35,720-y,70,35))

        font = pygame.font.Font('freesansbold.ttf', 45)
        text = font.render(f"{count}", False, (0, 0, 0))
        if count != 10:
            screen.blit(text, (55, 720 - y))
        else:
            screen.blit(text, (40, 720 - y))



        count += 1

#def buttons():
    #for y in range()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    generalbkg()
    flnums(buttonspress)

    pygame.display.update()