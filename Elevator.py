import pygame
from pygame.locals import *
import sys
import time
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
hieghts = []

for x in range(70,701,70):
    hieghts.append(x)
print(hieghts)
hieghts.reverse()

y= 720-hieghts[9]

speed = 70/40
speed = 5


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
diroftvl = 1
def flnums(buttonspress,selected):
    count = 1
    for y in range(700,0,-70):
        if buttonspress[count-1][0] == 0 and buttonspress[count-1][1] == 0:
            pygame.draw.rect(screen,colors[0],(35,720-y,70,35))

        else:
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

def elevator(y,dir,secs):
    pygame.draw.rect(screen,(0,0,0), (300,y,70,35))
    pygame.draw.rect(screen, (255, 255, 255), (300, y, (secs / 12) * 70, 35))
    font = pygame.font.Font('freesansbold.ttf', 15)
    text = font.render(f"{'OPEN' if dir == 0 else 'closed'}", False, (0, 255, 0))
    screen.blit(text, (310, y+10))

    print(seconds)


def drawarrow(que):
    for each in que:
        font = pygame.font.Font('freesansbold.ttf', 25)
        text = font.render(f"{'up' if each[1] == 1 else 'down'}", False, (0, 255, 0))
        screen.blit(text, (160, hieghts[each[0]-1]-45))

qeue = []
seconds = 0
while True:
    #y = 720 - hieghts[selected-1]
    xcord, ycord = pygame.mouse.get_pos()

    if diroftvl == 1:
        highercount = 0
        lowercount = 0
        for each in qeue:
            if hieghts[each[0] - 1]-50 <  y:
                y -= speed
            if hieghts[each[0]-1]-50 == y:
                try:
                    qeue.remove([each[0],0])
                except:
                    qeue.remove([each[0],1])
                buttonspress[10-each[0]][0] = 0
                buttonspress[10 - each[0]][1] = 0
                diroftvl = 0
                start_ticks = pygame.time.get_ticks()  # starter tick
            if hieghts[each[0]-1]-50 >y:
                lowercount += 1

    if diroftvl == 2:
        for each in qeue:
            if hieghts[each[0] - 1]-50 >  y:
                y += speed
            if hieghts[each[0]-1]-50 == y:
                try:
                    qeue.remove([each[0],0])
                except:
                    qeue.remove([each[0],1])
                buttonspress[10-each[0]][0] = 0
                buttonspress[10 - each[0]][1] = 0
                diroftvl = 0
                start_ticks = pygame.time.get_ticks()  # starter tick

    if diroftvl == 0:
        seconds = (pygame.time.get_ticks() - start_ticks) / 1000  # calculate how many seconds


        if seconds > 12:
            diroftvl = 1
            seconds = 0


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

                if selected != 10:
                    buttonspress[10-selected][0] = 1
                    qeue.append([selected,1])


            if event.key == pygame.K_DOWN:

                if selected != 1:
                    buttonspress[10 - selected][1] = 1
                    qeue.append([selected,0])
        if event.type == pygame.MOUSEBUTTONUP:
            print(xcord,ycord)

    drawarrow(qeue)
    generalbkg()
    flnums(buttonspress,selected)
    elevator(y, diroftvl,seconds)
    drawarrow(qeue)
    pygame.display.update()
    fpsClock.tick(10)
    print(qeue)
    print(buttonspress)
pygame.quit()


