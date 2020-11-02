import pygame
from pygame.locals import *
import sys

pygame.init()
width, height = 680,720
screen = pygame.display.set_mode((width,height))

yellow = (255,255,102)
grey = (100,100,100)

fpsClock = pygame.time.Clock()

colors = [grey,yellow]

floors = []
for x in range(10):
    floors.append(0)
selected = 1
buttonspress = []
for x in range(10):
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

def flnums(buttonspress,selected):
    count = 1
    for y in range(700,0,-70):
        if buttonspress[count-1][0] == 0 and buttonspress[count-1][1] == 0:
            pygame.draw.rect(screen,colors[0],(35,720-y,70,35))
        if buttonspress[count-1] == 1 or buttonspress[count-1] == 1:
            pygame.draw.rect(screen,colors[1],(35,720-y,70,35))


        font = pygame.font.Font('freesansbold.ttf', 45)
        if count-1 == 10-selected:
            text = font.render(f"{11-count}", False, (0, 255, 0))
        else:
            text = font.render(f"{11-count}", False, (0, 0, 0))

        if 11-count != 10:
            screen.blit(text, (55, 720 - y))
        else:
            screen.blit(text, (40, 720 - y))
        count += 1



#def buttons():
    #for y in range()

while True:
    xcord, ycord = pygame.mouse.get_pos()
    print (selected)


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == ord('w'):
                if selected < 10:
                    selected += 1
            if event.key == ord('s'):
                if selected > 1:
                    selected -= 1
            if event.key == pygame.K_UP:
                buttonspress[10-selected][0] = 1
            if event.key == pygame.K_DOWN:
                buttonspress[10-selected][1] = 1
    generalbkg()
    flnums(buttonspress,selected)

    pygame.display.update()
    fpsClock.tick(10)
    print(buttonspress)
pygame.quit()


