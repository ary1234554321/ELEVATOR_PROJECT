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
speedtick = 30

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
diroftvl = 3
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
    pygame.draw.rect(screen,(0,0,0), (300,y,130,35))
    pygame.draw.rect(screen, (255, 255, 255), (300, y, (secs / 12) *130, 35))
    font = pygame.font.Font('freesansbold.ttf', 15)
    text = font.render(f"{'OPEN' if dir == 0 else 'closed'}", False, (0, 255, 0))
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
    if diroftvl == 3:
        if len(qeue) > 0:
            diroftvl = 1



    if diroftvl == 1:
        highercount = 0
        for each in qeue:

            if hieghts[each[0] - 1]-50 <  y:
                highercount += 1
            if hieghts[each[0]-1]-50 == y:
                try:
                    qeue.remove([each[0],0])
                except:
                    qeue.remove([each[0],1])
                buttonspress[10-each[0]][0] = 0
                buttonspress[10 - each[0]][1] = 0
                diroftvl = 0
                start_ticks = pygame.time.get_ticks()  # starter tick
        if highercount > 0:
            y -= speed

    if diroftvl == 2:
        lowercount = 0
        for each in qeue:
            if hieghts[each[0] - 1]-50 >  y:
                lowercount += 1
            if hieghts[each[0]-1]-50 == y:
                try:
                    qeue.remove([each[0],0])
                except:
                    qeue.remove([each[0],1])
                buttonspress[10-each[0]][0] = 0
                buttonspress[10 - each[0]][1] = 0
                diroftvl = 0
                start_ticks = pygame.time.get_ticks()  # starter tick
                highercount = 0
                lowercount = 0
                if hieghts[each[0] - 1] - 50 > y:
                    lowercount += 1
                if hieghts[each[0] - 1] - 50 < y:
                    highercount += 1
        if lowercount > 0:
            y += speed

        if highercount == 0 and lowercount == 0:
            if y != hieghts[0]-50:
                qeue.append([1,1])

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
                    try:
                        qeue.remove([each[0], 0])
                    except:
                        qeue.remove([each[0], 1])
                if hieghts[each[0] - 1] - 50 > y:
                    lowercount += 1
                if hieghts[each[0] - 1] - 50 < y:
                    highercount += 1
            print(y,hieghts[0]-50)
            if highercount > 0:
                diroftvl = 1
            if highercount == 0:
                if y != hieghts[0] -50:
                    diroftvl = 2
                else:
                    diroftvl = 3
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
    qeue = checker(qeue)
    drawarrow(qeue)
    generalbkg()
    flnums(buttonspress,selected)
    elevator(y, diroftvl,seconds)
    drawarrow(qeue)
    pygame.display.update()
    fpsClock.tick(speedtick)
    print(diroftvl)
    print(qeue)
pygame.quit()


