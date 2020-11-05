import random
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

speed = 2
#speed = 5
speedtick = 10
speedtick = 60

def generalbkg():
    empty_rect = pygame.Rect(20, 10, 100,700)
    pygame.draw.rect(screen, (0, 0, 0), empty_rect, 3)
    empty_rect = pygame.Rect(140, 10, 130,700)
    pygame.draw.rect(screen, (0, 0, 0), empty_rect, 3)
    empty_rect = pygame.Rect(290, 10, 150,700)
    pygame.draw.rect(screen, (0, 0, 0), empty_rect, 3)
    empty_rect = pygame.Rect(460, 10, 200, 700)
    pygame.draw.rect(screen, (0, 0, 0), empty_rect, 3)
diroftvl = 3
def flnums(buttonspress,selected):
    count = 1
    for y in range(700,0,-70):

        pygame.draw.rect(screen,colors[0],(35,720-y,70,35))




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
    pygame.draw.rect(screen,(0,0,0), (300,y,130,35))
    pygame.draw.rect(screen, (200, 200, 200), (300, y, (secs / 12) *130, 35))
    font = pygame.font.Font('freesansbold.ttf', 15)
    text = font.render(f"{'OPEN' if dir == 0 else 'closed'}", False, (255, 0, 0))
    screen.blit(text, (310, y+10))


def checker(que):
    res = []
    for each in que:
        if each not in res:
            res.append(each)

    return res
def fl1rem(que):
    res = []
    for each in que:
        if each != [1,1]:
            res.append(each)

    return res

def butdir(buts):
    for countx,x in enumerate(range(150,211,60)):
        for county,y in enumerate(range(70,701,70)):
            if buts[county][countx] == 1:
                pygame.draw.rect(screen,yellow,(x,y-40,50,20))
            else:
                pygame.draw.rect(screen, (255,255,255), (x, y - 40, 50, 20))
    for county,y in enumerate(range(70,701,70)):
        if buts[county][0] == 1:
            font = pygame.font.Font('freesansbold.ttf', 15)
            text = font.render("UP", False, (0, 255, 255))
            screen.blit(text, (160,y-35))
    for county,y in enumerate(range(70,701,70)):
        if buts[county][1] == 1:
            font = pygame.font.Font('freesansbold.ttf', 15)
            text = font.render("DOWN", False, (0, 255, 255))
            screen.blit(text, (210,y-35))


def quesort(qu):
    lis = qu
    ups = []
    downs = []
    for each in lis:
        if each[1] == 1:
            ups.append(each)

        if each[1] == 0:
            downs.append(each)




insidebuts = []
for x in range(10):
    insidebuts.append(0)

def drawinsidebuttons(buts):
    for count,each in enumerate(buts):

        if each == 0:
            pygame.draw.circle(screen, (0, 0, 0), (540,((count+1)*70)-25),30 )
        if each == 1:
            pygame.draw.circle(screen, yellow, (540,((count+1)*70)-25),30 )

        font = pygame.font.Font('freesansbold.ttf', 25)
        text = font.render(f"{count+1}", False, (0, 255, 255))
        screen.blit(text, (535, ((count+1)*70)-35))

prev = 0
qeue = []
seconds = 0
while True:
    screen.fill((150, 150, 150))
    #y = 720 - hieghts[selected-1]
    xcord, ycord = pygame.mouse.get_pos()

    if diroftvl == 3:
        if len(qeue) > 0:
            diroftvl = 1



    if diroftvl == 1:


    if diroftvl == 2:
        pass

    if diroftvl == 0:
        pass




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


            if event.key == pygame.K_1:

                insidebuts[0] = 1
                qeue.append([1])
            if event.key == pygame.K_2:
                insidebuts[1] = 1
                qeue.append([1])
            if event.key == pygame.K_3:
                insidebuts[2] = 1
                qeue.append([1])

            if event.key == pygame.K_4:
                insidebuts[3] = 1
                qeue.append([1])
            if event.key == pygame.K_5:
                insidebuts[4] = 1
                qeue.append([1])
            if event.key == pygame.K_6:
                insidebuts[5] = 1
                qeue.append([1])
            if event.key == pygame.K_7:
                insidebuts[6] = 1
                qeue.append([1])
            if event.key == pygame.K_8:
                insidebuts[7] = 1
                qeue.append([1])
            if event.key == pygame.K_9:
                insidebuts[8] = 1
                qeue.append([1])
            if event.key == pygame.K_0:
                insidebuts[9] = 1
                qeue.append([1])


        if event.type == pygame.MOUSEBUTTONUP:
            print(xcord,ycord)


    qeue = checker(qeue)
    generalbkg()
    flnums(buttonspress,selected)
    elevator(y, diroftvl,seconds)

    butdir(buttonspress)

    fpsClock.tick(speedtick)
    drawinsidebuttons(insidebuts)
    pygame.display.update()
    print(diroftvl)
pygame.quit()

