import pygame
from pygame.locals import *
import sys
import time
import random


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

    if secs < 4:
        pygame.draw.rect(screen, (200, 200, 200), (300, y, 130 - ((secs/4)*130) , 35))
    if 4 < secs < 8:
        pygame.draw.rect(screen, (200, 200, 200), (300, y, 1 , 35))

    if 8 < secs < 13:
        pygame.draw.rect(screen, (200, 200, 200), (300, y,((secs-8)/4) * 130 , 35))

    font = pygame.font.Font('freesansbold.ttf', 15)
    text = font.render(f"{'OPEN' if dir == 0 else 'closed'}", False, (255, 0, 0))
    screen.blit(text, (310, y+10))

    font = pygame.font.Font('freesansbold.ttf', 15)
    text = font.render(f"{secs}", False, (255, 0, 0))
    screen.blit(text, (370, y + 10))


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

def butque(buttons):
    qu =[]
    for counter,each in enumerate(buttons):
        if each[0] == 1:
            qu.append([10-counter,1])
        if each[1] == 1:
            qu.append([10-counter,0])
    return qu


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
        prev = 1
        highercount = 0

        highfloor = 0
        for each in qeue:
            if each[0] > highfloor:
                highfloor = each[0]

        for each in qeue:
            if each[1] == 1 or each[0] == highfloor:
                if hieghts[each[0] - 1]-50 < y:
                    highercount += 1
                if hieghts[each[0]-1]-50 == y:
                    buttonspress[10 - each[0]][1] = 0
                    diroftvl = 0
                    start_ticks = pygame.time.get_ticks()  # starter tick


        if highercount > 0:
            y -= speed

    if diroftvl == 2:
        prev = 2
        lowercount = 0
        for each in qeue:
            if hieghts[each[0] - 1]-50 >  y:
                if each[1] != 1:
                    lowercount += 1
                else:
                    if each[0] == 1:
                        lowercount += 1
            if (hieghts[each[0]-1]-50 == y and each[1] != 1) or (hieghts[each[0]-1]-50 == y and each[0] == 1):

                buttonspress[10 - each[0]][1] = 0
                diroftvl = 0
                start_ticks = pygame.time.get_ticks()  # starter tick
        if lowercount > 0:
            y += speed

        if len(qeue) == 0:
            buttonspress[len(buttonspress)-1][0] = 1

    if diroftvl == 0:
        seconds = (pygame.time.get_ticks() - start_ticks) / 1000  # calculate how many seconds
        if seconds > 12:

            if y == hieghts[0]-50:
                qeue = fl1rem(qeue)
                diroftvl = 1

            highercount = 0
            lowercount = 0

            for each in qeue:

                if hieghts[each[0] - 1] - 50 == y:
                    print(hieghts[each[0]-1]-50,y)

                    buttonspress[10-each[0]][0] = 0
                    buttonspress[10-each[0]][1] = 0
                if hieghts[each[0] - 1] - 50 > y:
                    lowercount += 1
                if hieghts[each[0] - 1] - 50 < y:
                    highercount += 1

            if highercount > 0 and hieghts[0]-50 == y:
                diroftvl = 1

            if highercount > 0 and lowercount == 0:
                diroftvl = 1

            if prev == 1 and highercount > 0:
                print("PReVcheck")
                diroftvl = 1

            if lowercount > 0 and highercount == 0:
                diroftvl = 2

            if prev == 2:
                if hieghts[0]-50 != y:
                    diroftvl = 2

            if highercount == 0:
                if y != hieghts[0] -50:
                    diroftvl = 2
                else:
                    diroftvl = 3
            if y == hieghts[0]-50:
                buttonspress[len(buttonspress)-1][0] = 0
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



            if event.key == pygame.K_DOWN:

                if selected != 1:
                    buttonspress[10 - selected][1] = 1


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


    qeue = butque(buttonspress)
    generalbkg()
    flnums(buttonspress,selected)
    elevator(y, diroftvl,seconds)

    butdir(buttonspress)

    fpsClock.tick(speedtick)
    drawinsidebuttons(insidebuts)
    pygame.display.update()
    print(diroftvl)
    print(qeue)
    print(y)
    print(buttonspress)
pygame.quit()
