arena = [['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w', 0],['w',0,'e1D',0,0,0,0,0,0,0,'m',0,0,0,0,'w',0,'e2D',0,'w',0],['w','a',0,0,0,0,0,0,0,0,0,0,0,0,0,'w','a',0,0,'w',0],['w','w',0,0,0,0,0,0,'w','w',0,0,0,0,0,'w','w','w',0,'w',0],['w','w','w','w','w',0,0,0,0,0,0,0,0,'w',0,0,0,0,0,'w'],['w',0,0,0,'w','w','w',0,0,0,0,0,0,'w',0,0,0,0,0,'w',0],['w',0,0,0,0,0,'w',0,0,0,'w',0,0,0,'m',0,0,0,0,'w',0],['w',0,0,0,0,0,0,0,0,0,'w',0,0,0,'w','w','w','w','w','w',0],['w','w','w','w',0,0,0,0,0,'a','w','m',0,0,0,0,0,0,0,'w',0],['w','a',0,0,0,0,0,'w','w','w','w','w','w','w',0,0,0,0,'a','w',0],['w',0,0,0,0,0,0,0,0,'m','w','a',0,0,0,0,0,0,0,'w'],['w',0,0,'w','w',0,0,0,0,0,'w',0,0,0,0,0,0,0,0,'w',0],['w',0,0,0,0,0,0,0,0,0,'w',0,0,0,0,0,'w','w','w','w',0],['w',0,0,0,'m',0,0,'w',0,0,0,0,0,0,0,0,0,0,0,'w',0],['w',0,0,0,0,0,0,'w',0,0,0,0,0,'w','w',0,0,0,0,'w',0],['w','w','w','w','w',0,0,'w',0,0,0,0,0,0,'w',0,0,0,0,'w',0],['w','a',0,0,0,0,0,'w',0,0,0,0,0,0,'w',0,0,0,0,'w',0],['w',0,0,0,0,0,0,'w',0,0,0,0,0,0,'w',0,0,0,0,'w',0],['w',0,'uF',0,0,0,0,'w',0,0,0,0,0,0,'w',0,0,'e3F',0,'w',0],['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w',0]]

import pygame
import random
import math
from random import randint
pygame.init()

AItankd = pygame.image.load('AItankd.bmp')
AItankf = pygame.image.load('AItankf.bmp')
AItankl = pygame.image.load('AItankl.bmp')
AItankr = pygame.image.load('AItankr.bmp')
ammo = pygame.image.load('ammo.bmp')
bg = pygame.image.load('bg.bmp')
bullet = pygame.image.load('bullet.bmp')
e = pygame.image.load('explosion.bmp')
mine = pygame.image.load('mine.bmp')
tankd = pygame.image.load('tankd.bmp')
tankf = pygame.image.load('tankf.bmp')
tankl = pygame.image.load('tankl.bmp')
tankr = pygame.image.load('tankr.bmp')
wall = pygame.image.load('wall.bmp')

size = (500,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tanks")

userPosition = [3, 19]
e1Position = [2, 3]
e2Position = [2, 18]
e3Position = [19, 18]
green= (0,255,0)
yellow= (255,255,0)
red= (255,0,0)
usrp=userPosition

def nextPosition(direction):
    usrp=[0,0]
    dead=0
    ammo=0
    if direction == 'f':
        tentativePosition = [userPosition[0], userPosition[1] - 1]
        usrp=usrp[1]+1
    elif direction == 'd':
        tentativePosition = [userPosition[0], userPosition[1] + 1]
        usrp=usrp[1]-1
    elif direction == 'l':
        tentativePosition = [userPosition[0] - 1, userPosition[1]]
        usrp=usrp[0]+1
    elif direction == 'r':
        tentativePosition = [userPosition[0] + 1, userPosition[1]]
        usrp=usrp[0]-1
    if tentativePosition[0] > 20 or tentativePosition[1] > 20 or arena[tentativePosition[1] - 1][tentativePosition[0] - 1] == 'w':
        return None
    elif tentativePosition[0]==5 and tentativePosition[1]==14:
        screen.blit(e,pixelPosition(5,14))
        screen.blit(bg,pixelPosition(userPosition[0],userPosition[1]))
        return None
    elif tentativePosition[0]==11 and tentativePosition[1]==2:
        screen.blit(e,pixelPosition(11,2))
        screen.blit(bg,pixelPosition(userPosition[0],userPosition[1]))
        tentativePosition=[11,2]
        return None
    elif tentativePosition[0]==15 and tentativePosition[1]==7:
        screen.blit(e,pixelPosition(15,7))
        screen.blit(bg,pixelPosition(userPosition[0],userPosition[1]))
        return None
    elif tentativePosition[0]==5 and tentativePosition[1]==14:
        screen.blit(e,pixelPosition(5,14))
        screen.blit(bg,pixelPosition(userPosition[0],userPosition[1]))
        return None
    elif tentativePosition[0]==12 and tentativePosition[1]==9:
        screen.blit(e,pixelPosition(12,9))
        screen.blit(bg,pixelPosition(userPosition[0],userPosition[1]))
        return None
    elif tentativePosition[0]==10 and tentativePosition[1]==11:
        screen.blit(e,pixelPosition(10,11))
        screen.blit(bg,pixelPosition(userPosition[0],userPosition[1]))
        return None
    #ammo, but for some reason it doesnt add up
    if tentativePosition[0]==2 and tentativePosition[1]==3:
        ammo=ammo+1
        screen.blit(bg,pixelPosition(tentativePosition[0],tentativePosition[1]))
        print("ammo +",ammo)
    if tentativePosition[0]==17 and tentativePosition[1]==3:
        ammo=ammo+1
        screen.blit(bg,pixelPosition(tentativePosition[0],tentativePosition[1]))
        print("ammo +",ammo)
    if tentativePosition[0]==10 and tentativePosition[1]==9:
        ammo=ammo+1
        screen.blit(bg,pixelPosition(tentativePosition[0],tentativePosition[1]))
        print("ammo +",ammo)
    if tentativePosition[0]==2 and tentativePosition[1]==10:
        ammo=ammo+1
        screen.blit(bg,pixelPosition(tentativePosition[0],tentativePosition[1]))
        print("ammo +",ammo)
    if tentativePosition[0]==12 and tentativePosition[1]==11:
        ammo=ammo+1
        screen.blit(bg,pixelPosition(tentativePosition[0],tentativePosition[1]))
        print("ammo +",ammo)
    if tentativePosition[0]==2 and tentativePosition[1]==3:
        ammo=ammo+1
        screen.blit(bg,pixelPosition(tentativePosition[0],tentativePosition[1]))
        print("ammo +",ammo)
    if tentativePosition[0]==19 and tentativePosition[1]==10:
        ammo=ammo+1
        screen.blit(bg,pixelPosition(tentativePosition[0],tentativePosition[1]))
        print("ammo +",ammo)
    if tentativePosition[0]==2 and tentativePosition[1]==17:
        ammo=ammo+1
        screen.blit(bg,pixelPosition(tentativePosition[0],tentativePosition[1]))
        print("ammo +",ammo)
    if tentativePosition[0]==19 and tentativePosition[1]==18:
        ammo=ammo+1
        screen.blit(bg,pixelPosition(tentativePosition[0],tentativePosition[1]))        
        print("ammo +",ammo)
    else:
        return tentativePosition
    return[usrp]
    

def health_bars(usH,e1H,e2H,e3H):
    if usH > 75:
        user_health_color = green
    elif usH >50:
        user_health_color = yellow
    else:
        user_health_color = red
    if e1H > 75:
        e1_health_color = green
    elif e1H>50:
        e1_health_color=yellow
    else:
        e1_health_color=red
    if e2H > 75:
        e2_health_color = green
    elif e2H>50:
        e2_health_color=yellow
    else:
        e2_health_color=red
    if e3H > 75:
        e3_health_color = green
    elif e3H>50:
        e3_health_color=yellow
    else:
        e3_health_color=red
    pygame.draw.rect(screen,user_health_color,(30,485,usH,10))
    pygame.draw.rect(screen,e1_health_color,(30,10,e1H,10))
    pygame.draw.rect(screen,e2_health_color,(375,10,e2H,10))
    pygame.draw.rect(screen,e3_health_color,(375,485,e3H,10))
def pixelPosition(x, y):
    xPixel = (x - 1)*25
    yPixel = (y - 1)*25
    return [xPixel, yPixel]
distanceu=0
xCoord = 0
yCoord = 0
x = 0
y = 0
while x <= 19:
        while y <= 19:
            if arena[x][y] == 'e1D' or arena[x][y] == 'e2D' or arena[x][y] == 'e3D':
                screen.blit(AItankd,(xCoord, yCoord))
            elif arena[x][y] == 'e1F' or arena[x][y] == 'e2F' or arena[x][y] == 'e3F':
                screen.blit(AItankf,(xCoord, yCoord))
            elif arena[x][y] == 'e1L' or arena[x][y] == 'e2L' or arena[x][y] == 'e3L':
                screen.blit(AItankl,(xCoord, yCoord))
            elif arena[x][y] == 'e1R' or arena[x][y] == 'e2R' or arena[x][y] == 'e3R':
                screen.blit(AItankr,(xCoord, yCoord))
            elif arena[x][y] == 'a':
                screen.blit(ammo,(xCoord, yCoord))
            elif arena[x][y] == 0:
                screen.blit(bg,(xCoord, yCoord))
            elif arena[x][y] == 'b':
                screen.blit(bullet,(xCoord, yCoord))
            elif arena[x][y] == 'e':
                screen.blit(e,(xCoord, yCoord))
            elif arena[x][y] == 'm':
                screen.blit(mine,(xCoord, yCoord))
            elif arena[x][y] == 'uD':
                screen.blit(tankd,(xCoord, yCoord))
            elif arena[x][y] == 'uF':
                screen.blit(tankf,(xCoord, yCoord))
            elif arena[x][y] == 'uL':
                screen.blit(tankl,(xCoord, yCoord))
            elif arena[x][y] == 'uR':
                screen.blit(tankr,(xCoord, yCoord))
            elif arena[x][y] == 'w':
                screen.blit(wall,(xCoord, yCoord))
            xCoord = xCoord + 25
            if xCoord == 1000:
                xCoord = 0
            y = y + 1
            if y == 20:
                break
        xCoord = 0
        x = x + 1
        yCoord = yCoord + 25
        y = 0

running = True 
clock = pygame.time.Clock()
loop = 0


while running:
    usH=100
    e1H=100
    e2H=100
    e3H=100
    health_bars(usH,e1H,e2H,e3H)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            distanceu=distanceu+1
            if event.key == pygame.K_w:
                if nextPosition('f') == None :
                    pass
                else:
                    screen.blit(bg,(pixelPosition(userPosition[0], userPosition[1])[0], pixelPosition(userPosition[0], userPosition[1])[1]))
                    userPosition = nextPosition('f')
                    screen.blit(tankf,(pixelPosition(userPosition[0], userPosition[1])[0], pixelPosition(userPosition[0], userPosition[1])[1]))
            elif event.key == pygame.K_d:
                if nextPosition('r') == None:
                    pass
                else:
                    screen.blit(bg,(pixelPosition(userPosition[0], userPosition[1])[0], pixelPosition(userPosition[0], userPosition[1])[1]))
                    userPosition = nextPosition('r')
                    screen.blit(tankr,(pixelPosition(userPosition[0], userPosition[1])[0], pixelPosition(userPosition[0], userPosition[1])[1]))
            elif event.key == pygame.K_s:
                if nextPosition('d') == None:
                    pass
                else:
                    screen.blit(bg,(pixelPosition(userPosition[0], userPosition[1])[0], pixelPosition(userPosition[0], userPosition[1])[1]))
                    userPosition = nextPosition('d')
                    screen.blit(tankd,(pixelPosition(userPosition[0], userPosition[1])[0], pixelPosition(userPosition[0], userPosition[1])[1]))
            elif event.key == pygame.K_a:
                if nextPosition('l') == None:
                    pass
                else:
                    screen.blit(bg,(pixelPosition(userPosition[0], userPosition[1])[0], pixelPosition(userPosition[0], userPosition[1])[1]))
                    userPosition = nextPosition('l')
                    screen.blit(tankl,(pixelPosition(userPosition[0], userPosition[1])[0], pixelPosition(userPosition[0], userPosition[1])[1]))
    def move(robot):
        if robot == 'e1':
            position = e1Position
        elif robot == 'e2':
            position = e2Position
        elif robot == 'e3':
            position = e3Position
        else:
            screen.blit(bg,(pixelPosition(position[0],position[1])[0],pixelPosition(position[0],position[1])[1]))
            position=nextPosition('f')
            screen.blit(e1,(pixelPosition(position[0],position[1])[0],pixelPosition(position[0],position[1])[1]))
        
    



    pygame.display.flip()
    clock.tick(60)
print("distance travelled is",distanceu,"units")
dist=math.sqrt((userPosition[0]-usrp[0])**2+(userPosition[1]-usrp[1])**2)
print("distance from start to end is:",dist,"units")
pygame.quit()





