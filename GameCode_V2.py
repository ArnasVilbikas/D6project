arena = [['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w'],['w',0,'e1D',0,0,0,0,0,0,0,'m',0,0,0,0,'w',0,'e2D',0,'w'],['w','a',0,0,0,0,0,0,0,0,0,0,0,0,0,'w','a',0,0,'w'],['w','w',0,0,0,0,0,0,'w','w',0,0,0,0,0,'w','w','w',0,'w'],['w','w','w','w','w',0,0,0,0,0,0,0,'w',0,0,0,0,0,'w'],['w',0,0,0,'w','w','w',0,0,0,0,0,0,'w',0,0,0,0,0,'w'],['w',0,0,0,0,0,'w',0,0,0,'w',0,0,0,'m',0,0,0,0,'w'],['w',0,0,0,0,0,0,0,0,0,'w',0,0,0,'w','w','w','w','w','w'],['w','w','w','w',0,0,0,0,0,'a','w','m',0,0,0,0,0,0,0,'w'],['w','a',0,0,0,0,0,'w','w','w','w','w','w','w',0,0,0,0,'a','w'],['w',0,0,0,0,0,0,0,'m','w','a',0,0,0,0,0,0,0,'w'],['w',0,0,'w','w',0,0,0,0,0,'w',0,0,0,0,0,0,0,0,'w'],['w',0,0,0,0,0,0,0,0,0,'w',0,0,0,0,0,'w','w','w','w'],['w',0,0,0,'m',0,0,'w',0,0,0,0,0,0,0,0,0,0,0,'w'],['w',0,0,0,0,0,0,'w',0,0,0,0,0,'w','w',0,0,0,0,'w'],['w','w','w','w','w',0,0,'w',0,0,0,0,0,0,'w',0,0,0,0,'w'],['w','a',0,0,0,0,0,'w',0,0,0,0,0,0,'w',0,0,0,0,'w'],['w',0,0,0,0,0,0,'w',0,0,0,0,0,0,'w',0,0,0,0,'w'],['w',0,'uF',0,0,0,0,'w',0,0,0,0,0,0,'w',0,0,'e3F',0,'w'],['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w']] 

import pygame
pygame.init()

# Loads the sprites as surface objects in Python
AItankd = pygame.image.load('AItankd.bmp')
AItankf = pygame.image.load('AItankf.bmp')
AItankl = pygame.image.load('AItankl.bmp')
AItankr = pygame.image.load('AItankr.bmp')
ammo = pygame.image.load('ammo.bmp')
bg = pygame.image.load('bg.bmp')
bullet = pygame.image.load('bullet.bmp')
explosion = pygame.image.load('explosion.bmp')
mine = pygame.image.load('mine.bmp')
tankd = pygame.image.load('tankd.bmp')
tankf = pygame.image.load('tankf.bmp')
tankl = pygame.image.load('tankl.bmp')
tankr = pygame.image.load('tankr.bmp')
wall = pygame.image.load('wall.bmp')

# Creates the screen and sets the caption
size = (1000,1000)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tanks")

running = True  # Used for the main game loop to indicate whether a user is finished

print(arena)

while running:
    # Checks if user is done, for example if the user presses the 'x' button on the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#
            running == False

    

    pygame.display.flip()  # Updates screen with what we've drawn

pygame.quit() # Quits the game





