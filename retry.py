import pygame
from pygame.locals import *
import sys
import time
import random
import json
import datetime
pygame.init()
width, length = 680,720
screen = pygame.display.set_mode((width,length))

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

floornums = []
for x in range(10):
    floornums.append(x)


for x in range(70,701,70):
    hieghts.append(x)

hieghts.reverse()

hieghts2 = []

for x in range(70,771,70):
    hieghts2.append(x)

hieghts2.reverse()

log = []


y= 720-hieghts[9]

speed = 5
#speed = 5
speedtick = 10
speedtick = 60
pygame.init()
def generalbkg():
    empty_rect = pygame.Rect(20, 10, 100,700)
    pygame.draw.rect(screen, (0, 0, 0), empty_rect, 3)
    empty_rect = pygame.Rect(140, 10, 130,700)
    pygame.draw.rect(screen, (0, 0, 0), empty_rect, 3)
    empty_rect = pygame.Rect(290, 10, 150,700)
    pygame.draw.rect(screen, (0, 0, 0), empty_rect, 3)
    empty_rect = pygame.Rect(460, 10, 200, 700)
    pygame.draw.rect(screen, (0, 0, 0), empty_rect, 3)
    empty_rect = pygame.Rect(600, 400, 40, 240)
    pygame.draw.rect(screen, (0, 0, 0), empty_rect, 3)
diroftvl = 3

def getfloor(lst,K):
    K = K-50
    x= lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]
    return lst.index(x)



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
    pygame.draw.rect(screen, (0, 0, 0), (300, y, 130, 35))

    if secs < 4:
        pygame.draw.rect(screen, (200, 200, 200), (300, y, 130 - ((secs / 4) * 130), 35))
        if 1.1 <secs < 1.3:
            timdate = datetime.datetime.now()
            log.append(f"Door opening at: {timdate}")
    if 4 < secs < 8:
        pygame.draw.rect(screen, (200, 200, 200), (300, y, 1, 35))

    if 8 < secs < 13:
        pygame.draw.rect(screen, (200, 200, 200), (300, y, ((secs - 8) / 4) * 130, 35))
        if 8.1 < secs < 8.3:
            timdate = datetime.datetime.now()
            log.append(f"Door closing at: {timdate}")

    font = pygame.font.Font('freesansbold.ttf', 15)
    text = font.render(f"{'OPEN' if dir == 0 else 'closed'}", False, (255, 0, 0))
    screen.blit(text, (310, y + 10))

    font = pygame.font.Font('freesansbold.ttf', 15)
    text = font.render(f"{secs}", False, (255, 0, 0))
    screen.blit(text, (370, y + 10))



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

prev = 1
qeue = []
seconds = 0


def butque(buttons,inbut):
    qu =[]
    for counter,each in enumerate(buttons):
        if each[0] == 1:
            qu.append([10-counter,1])
        if each[1] == 1:
            qu.append([10-counter,0])
    for counter,each in enumerate(inbut):
        if each == 1:
            qu.append([counter+1,3])
    return qu

def drawcurentfloor(floor,direction):
    font = pygame.font.Font('freesansbold.ttf', 35)
    text = font.render(f"{floor}", False, (255, 0, 0))
    screen.blit(text, (610, 500))

    if direction == 1:
        pygame.draw.polygon(screen, (0, 255, 0),((610, 500), (630, 500), (630,450), (640, 450), (620,410 ), (600, 450), (610, 450)))
    if direction == 2:
        pygame.draw.polygon(screen, (255, 0, 0),((610, 550), (630, 550), (630, 600), (640, 600), (620, 640), (600,600), (610, 600)))


start_ticks2 = pygame.time.get_ticks()

while True:
    screen.fill((150, 150, 150))
    #y = 720 - hieghts[selected-1]
    xcord, ycord = pygame.mouse.get_pos()



    if diroftvl == 3:
        seconds2 = (pygame.time.get_ticks() - start_ticks2) / 1000
        print(seconds2)
        if seconds2 >60:
            if y != hieghts[0]-50:
                buttonspress[len(buttonspress)-1][0] = 1

        counthigher = 0
        countlower = 0
        for each in qeue:
            if hieghts[each[0]-1]-50 > y or (buttonspress[len(buttonspress)-1][0] == 1 and y < hieghts[0]):
                countlower += 1
            if hieghts[each[0]-1]-50 < y:
                counthigher += 1

        if prev == 2 and countlower > 0:
            diroftvl = 2
        if prev == 1 and counthigher > 0:
            diroftvl = 1
        if prev == 2 and countlower == 0 and counthigher > 0:
            diroftvl = 1
        if prev == 1 and counthigher == 0 and countlower > 0:
            diroftvl = 2




    if diroftvl == 0:
        seconds = (pygame.time.get_ticks() - start_ticks) / 1000
        #print("FLOOR:",getfloor(hieghts2,y)-1)

        insidebuts[getfloor(hieghts2,y)-2] = 0
        if seconds > 12:

            if y == hieghts[0] - 50:
                diroftvl = 3
                start_ticks2 = pygame.time.get_ticks()

            if prev == 2:

                countlower = 0
                for each in qeue:
                    if len(each) != 1:
                        if hieghts[each[0]-1]-50 > y and (each[1] == 0 or each[1] == 3):
                            countlower += 1

                if countlower > 0:

                    diroftvl = 2

            if prev == 1:

                counthigher = 0
                for each in qeue:
                    if len(each) != 1:
                        if hieghts[each[0]-1] < y:
                            counthigher += 1

                if counthigher > 0:
                    diroftvl = 1
                if counthigher == 0:
                    diroftvl = 2

            if len(qeue) == 0:

                diroftvl = 3
                start_ticks2 = pygame.time.get_ticks()

            seconds = 0


    if diroftvl == 1:
        prev = 1

        counthigher = 0
        for each in qeue:
            if len(each) != 1:
                if (hieghts[each[0]-1] - 50 < y and each[1] == 1) or (hieghts[each[0]-1] - 50 < y and each[1] == 0) or (hieghts[each[0]-1]-50 < y and each[1] == 3):
                    counthigher += 1
        for each in qeue:
            if len(each) != 1:
                if (hieghts[each[0]-1] - 50 == y):
                    if each[1] == 1:
                        buttonspress[10-(each[0])][0] = 0
                        start_ticks = pygame.time.get_ticks()
                        diroftvl = 0
                        #print("RANDOM FLOOR UP!")
                        current = getfloor(hieghts2, y)-1
                        ran = random.randint(current, 9)
                        insidebuts[ran] = 1

                if hieghts[each[0]-1] - 50 == y and each[1] == 3:
                    insidebuts[each[0]-1] = 0
                    start_ticks = pygame.time.get_ticks()
                    diroftvl = 0


        highest = [0,0]
        for each in qeue:
            if len(each) != 1:
                if each[1] == 0:
                    if each[0] > highest[0]:
                        highest = each
        newhigh = [0,0]
        for each in qeue:
            if len(each) != 1:
                if each[1] == 1:
                    if each[0] > newhigh[0]:
                        newhigh = each

        if newhigh[0] > highest[0]:
            highest = newhigh
        newerhigh = [0,0]
        for each in qeue:
            if len(each) != 1:
                if each[1] == 3:
                    if each[0] > newerhigh[0]:
                        newerhigh = each

        if newerhigh[0] > highest[0]:
            highest = newerhigh


        if (hieghts[highest[0]-1] - 50 == y):
            if highest[1] == 0 or highest[1] == 1:
                #print(highest)
                buttonspress[10-(highest[0])][1] = 0
                ran1 = random.randint(0, 9)
                if highest[1] == 0:
                    if ran1 != 0:
                        insidebuts[0] = 1
                    if ran1 == 0:
                        current = getfloor(hieghts2, y)-1
                        ran = random.randint(0, current)

                        insidebuts[ran] = 1
                diroftvl = 0

                start_ticks = pygame.time.get_ticks()
            if highest[1] == 3:
                insidebuts[highest[0]-1] = 0
                diroftvl = 0
                start_ticks = pygame.time.get_ticks()

        if counthigher > 0:
            y -= speed




    if diroftvl == 2:
        prev = 2
        countlower = 0
        for each in qeue:
            if len(each) != 1:
                if (hieghts[each[0]-1]-50 > y and (each[1] == 0 or each[1] == 3)) or (hieghts[0] -50 > y and buttonspress[len(buttonspress)-1][0]== 1):
                    countlower += 1

                if hieghts[each[0]-1]-50 == y and (each[1] == 0 or each[1]==3):

                    buttonspress[10 - (each[0])][1] = 0
                    start_ticks = pygame.time.get_ticks()
                    diroftvl = 0
                    if each[1] == 0:

                        ran1 = random.randint(0,9)
                        if ran1 != 0:
                            insidebuts[0] = 1
                        if ran1 == 0:
                            current = getfloor(hieghts2,y)-1
                            ran = random.randint(0,current)

                            insidebuts[ran] = 1


                if hieghts[0] -50 == y and buttonspress[len(buttonspress) - 1][0] == 1:
                    buttonspress[len(buttonspress) - 1][0] = 0
                    diroftvl = 0
                    start_ticks = pygame.time.get_ticks()
        #for count,each in enumerate(insidebuts):
            #print('count:',count)
        if countlower > 0:
            y += speed


    for event in pygame.event.get():
        if event.type == QUIT:
            print("MAKING LOG!")
            total = {}
            total['log'] = log
            with open(f"Log.json", "w") as out:
                json.dump(total, out)
            pygame.quit()
            exit()

        keys = pygame.key.get_pressed()
        if keys[K_h]:
            timdate = datetime.datetime.now()
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

                    timdate = datetime.datetime.now()
                    log.append(f"Up button, floor {10-selected} pressed: {timdate}")


            if event.key == pygame.K_DOWN:

                if selected != 1:
                    buttonspress[10 - selected][1] = 1
                    timdate = datetime.datetime.now()
                    log.append(f"Down button, floor {10 - selected} pressed: {timdate}")

            if event.key == pygame.K_1:

                insidebuts[0] = 1
                timdate = datetime.datetime.now()
                log.append(f"Button floor 1 pressed: {timdate}")

            if event.key == pygame.K_2:
                insidebuts[1] = 1
                timdate = datetime.datetime.now()
                log.append(f"Button floor 2 pressed: {timdate}")
            if event.key == pygame.K_3:
                insidebuts[2] = 1
                timdate = datetime.datetime.now()
                log.append(f"Button floor 3 pressed: {timdate}")
            if event.key == pygame.K_4:
                insidebuts[3] = 1
                timdate = datetime.datetime.now()
                log.append(f"Button floor 4 pressed: {timdate}")
            if event.key == pygame.K_5:
                insidebuts[4] = 1
                timdate = datetime.datetime.now()
                log.append(f"Button floor 5 pressed: {timdate}")
            if event.key == pygame.K_6:
                insidebuts[5] = 1
                timdate = datetime.datetime.now()
                log.append(f"Button floor 6 pressed: {timdate}")
            if event.key == pygame.K_7:
                insidebuts[6] = 1
                timdate = datetime.datetime.now()
                log.append(f"Button floor 7 pressed: {timdate}")
            if event.key == pygame.K_8:
                insidebuts[6] = 1
                timdate = datetime.datetime.now()
                log.append(f"Button floor 8 pressed: {timdate}")
            if event.key == pygame.K_9:
                insidebuts[8] = 1
                timdate = datetime.datetime.now()
                log.append(f"Button floor 9 pressed: {timdate}")
            if event.key == pygame.K_0:
                insidebuts[9] = 1
                timdate = datetime.datetime.now()
                log.append(f"Button floor 10 pressed: {timdate}")
        if event.type == pygame.MOUSEBUTTONUP:
            print(xcord,ycord)
    qeue = butque(buttonspress,insidebuts)
    generalbkg()
    flnums(buttonspress,selected)
    elevator(y, diroftvl,seconds)
    butdir(buttonspress)
    fpsClock.tick(speedtick)
    drawinsidebuttons(insidebuts)
    drawcurentfloor(getfloor(hieghts2,y)-1,diroftvl)
    pygame.display.update()


    #print(diroftvl)
    #print(qeue)
    #print(buttonspress)



pygame.quit()
print("MAKING LOG!")
total['log'] = log
with open(f"Log.json", "w") as out:
    json.dump(total, out)
