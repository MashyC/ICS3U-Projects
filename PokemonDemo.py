#Issue
#m_outside only runs when character moves
#Loading in police
#Setting police behavi
import pygame
from time import sleep
from random import randint
pygame.init()
pygame.font.init()
display_width = 840
display_height = 840

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
background = (106, 98, 112)
walls = (73, 60, 9)
w_border = (56, 47, 15)
player=(47, 145, 69)
door = (23,0,150)
door2 = (150,0,0)
door3 = (247,150,98)

path = pygame.image.load('PATH.png')
grass = pygame.image.load('GRASS.png')
grass3 = pygame.image.load('GRASS3.png')

DISPLAY = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Pokemans tho')

m_outside = [
             [6,6,6,6,6,6,6,6,1,1,1,1,1,6,6,6,6,6,6,6,6],
             [6,6,6,6,6,6,6,6,1,4,4,4,1,6,6,6,6,6,6,6,6],
             [6,6,6,6,6,6,6,6,6,5,5,5,6,6,6,6,6,6,6,6,6],
             [6,6,6,6,6,6,6,6,6,5,5,5,6,6,6,6,6,6,6,6,6],
             [6,6,6,6,6,6,6,6,6,5,5,5,6,6,6,6,6,6,6,6,6],
             [6,6,6,6,6,6,6,6,6,5,5,5,6,6,6,6,6,6,6,6,6],
             [1,1,1,1,1,6,6,6,6,5,5,5,6,6,6,6,1,1,1,1,1],
             [1,2,2,2,1,6,6,6,6,5,5,5,6,6,6,6,1,4,4,4,1],
             [8,5,5,5,8,6,6,6,6,5,5,5,6,6,6,6,8,5,5,5,8],
             [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
             [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
             [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
             [7,7,7,7,7,7,7,7,7,5,5,5,7,7,7,7,7,7,7,7,7],
             [7,7,7,7,7,7,7,7,7,5,5,5,7,7,7,7,7,7,7,7,7],
             [7,7,7,7,7,7,7,7,7,5,5,5,7,7,7,7,7,7,7,7,7],
             [7,7,7,7,7,7,7,7,7,5,5,5,7,7,7,7,7,7,7,7,7],
             [7,7,7,7,7,7,7,7,7,5,5,5,7,7,7,7,7,7,7,7,7],
             [7,7,7,7,7,7,7,7,7,5,5,5,7,7,7,7,7,7,7,7,7],
             [7,7,7,7,7,7,7,7,7,5,5,5,7,7,7,7,7,7,7,7,7],
             [7,7,7,7,7,7,7,7,7,5,5,5,7,7,7,7,7,7,7,7,7],
             [7,7,7,7,7,7,7,7,7,5,5,5,7,7,7,7,7,7,7,7,7]
             ]

m_shop = [
             [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0],
             [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,1,2,2,2,1,0,0,0,0,0,0,0,0] ]
m_heal = [
             [0,1,1,1,0,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0],
             [0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
             [0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #Last bad
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0],
             [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0],
             [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,1,2,2,2,1,0,0,0,0,0,0,0,0] ]

m_gym = [
             [4,4,4,4,4,4,4,4,4,2,2,2,4,4,4,4,4,4,4,4,4],
             [4,4,4,4,4,4,4,4,0,0,0,0,0,4,4,4,4,4,4,4,4],
             [4,4,4,4,4,4,4,4,0,0,0,0,0,4,4,4,4,4,4,4,4],
             [4,4,4,4,4,4,4,4,0,0,0,0,0,4,4,4,4,4,4,4,4],
             [4,4,4,4,4,4,4,4,0,0,0,0,0,4,4,4,4,4,4,4,4],
             [4,4,4,4,4,4,4,4,0,0,0,0,0,4,4,4,4,4,4,4,4],
             [4,4,4,4,4,4,4,4,0,0,0,0,0,4,4,4,4,4,4,4,4],
             [4,4,4,4,4,4,4,4,0,0,0,0,0,4,4,4,4,4,4,4,4],
             [4,4,4,4,4,4,4,4,0,0,0,0,0,4,4,4,4,4,4,4,4],
             [4,4,4,4,4,4,4,4,0,0,0,0,0,4,4,4,4,4,4,4,4],
             [4,4,4,4,4,4,4,4,0,0,0,0,0,4,4,4,4,4,4,4,4],
             [4,4,4,4,4,4,4,4,0,0,0,0,0,4,4,4,4,4,4,4,4],
             [4,4,4,4,4,4,4,4,0,0,0,0,0,4,4,4,4,4,4,4,4],
             [4,4,4,4,4,4,4,4,0,0,0,0,0,4,4,4,4,4,4,4,4],
             [4,4,4,4,4,4,4,4,0,0,0,0,0,4,4,4,4,4,4,4,4],
             [4,4,4,4,4,4,4,4,0,0,0,0,0,4,4,4,4,4,4,4,4],
             [4,4,4,4,4,4,4,4,0,0,0,0,0,4,4,4,4,4,4,4,4],
             [4,4,4,4,4,4,4,4,0,0,0,0,0,4,4,4,4,4,4,4,4],
             [4,4,4,4,4,4,4,4,0,0,0,0,0,4,4,4,4,4,4,4,4],
             [4,4,4,4,4,4,4,4,0,0,0,0,0,4,4,4,4,4,4,4,4],
             [4,4,4,4,4,4,4,4,4,2,2,2,4,4,4,4,4,4,4,4,4]]

def gym(DISPLAY, x, y, m_outside):
    for i in range(len(m_gym)):
        for n in range(len(m_gym[i])):
            if m_gym[i][n]==0:
                pygame.draw.rect(DISPLAY, background, (n*40,i*40,40,40))
            elif m_gym[i][n] == 1:
                pygame.draw.rect(DISPLAY,walls,(n*40,i*40, 40,40))
                pygame.draw.rect(DISPLAY,w_border,(n*40,i*40, 40,40),3)
            elif m_gym[i][n] == 4:
                pygame.draw.rect(DISPLAY,(0,0,0),(n*40,i*40, 40,40))
            else:
                pygame.draw.rect(DISPLAY, door, (n*40,i*40, 40, 40))
    char = pygame.draw.rect(DISPLAY, player, (x,y,40,40))
    print(x,y)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x>280:
                    if DISPLAY.get_at((int(x-(40)),int(y)))[0] == door[0]:
                        outside(DISPLAY, 400,80,m_outside)
                    elif DISPLAY.get_at((int(x-(40)),int(y)))[0] != w_border[0]:
                        gym(DISPLAY, x-(40),y,m_outside)
                if event.key == pygame.K_RIGHT and x<480:
                    if DISPLAY.get_at((int(x+(40)),int(y)))[0] == door[0]:
                        outside(DISPLAY,400,80, m_outside)
                    elif DISPLAY.get_at((int(x+(40)),int(y)))[0] != w_border[0]:
                        gym(DISPLAY, x+(40),y,m_outside)
                if event.key == pygame.K_UP and y>0:
                    if DISPLAY.get_at((int(x),int(y-(40))))[0]== door[0]:
                        outside(DISPLAY, 400,80, m_outside)
                    elif DISPLAY.get_at((int(x),int(y-(40))))[0] != w_border[0]:
                        gym(DISPLAY, x,y-(40),m_outside)
                if event.key == pygame.K_DOWN and y<display_height-(40):
                    if DISPLAY.get_at((int(x),int(y+(40))))[0] == door[0]:
                        outside(DISPLAY, 400,80,m_outside)
                    elif DISPLAY.get_at((int(x),int(y+(40))))[0] != w_border[0]:
                        gym(DISPLAY, x,y+(40),m_outside)

def heal(DISPLAY, x, y, m_outside):
    for i in range(len(m_heal)):
        for n in range(len(m_heal[i])):
            if m_heal[i][n]==0:
                pygame.draw.rect(DISPLAY, background, (n*40,i*40,40,40))
            elif m_heal[i][n] == 1:
                pygame.draw.rect(DISPLAY,walls,(n*40,i*40, 40,40))
                pygame.draw.rect(DISPLAY,w_border,(n*40,i*40, 40,40),3)
            else:
                pygame.draw.rect(DISPLAY, door, (n*40,i*40, 40, 40))
    char = pygame.draw.rect(DISPLAY, player, (x,y,40,40))
    print(x,y)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x>0:
                    if DISPLAY.get_at((int(x-(40)),int(y)))[0] == door[0]:
                        outside(DISPLAY, 720,320, m_outside)
                    elif DISPLAY.get_at((int(x-(40)),int(y)))[0] != w_border[0]:
                        heal(DISPLAY, x-(40),y,m_outside)
                if event.key == pygame.K_RIGHT and x<display_width-(40):
                    if DISPLAY.get_at((int(x+(40)),int(y)))[0] == door[0]:
                        outside(DISPLAY, 720,320, m_outside)
                    elif DISPLAY.get_at((int(x+(40)),int(y)))[0] != w_border[0]:
                        heal(DISPLAY, x+(40),y,m_outside)
                if event.key == pygame.K_UP and y>0:
                    if DISPLAY.get_at((int(x),int(y-(40))))[0]== door[0]:
                        outside(DISPLAY, 720,320, m_outside)
                    if DISPLAY.get_at((int(x),int(y-(40))))[0] != w_border[0]:
                        heal(DISPLAY, x,y-(40),m_outside)
                if event.key == pygame.K_DOWN and y<display_height-(40):
                    if DISPLAY.get_at((int(x),int(y+(40))))[0] == door[0]:
                        outside(DISPLAY, 720,320, m_outside)
                    if DISPLAY.get_at((int(x),int(y+(40))))[0] != w_border[0]:
                        heal(DISPLAY, x,y+(40),m_outside)

    
def shop(DISPLAY, x, y, m_outside):
    for i in range(len(m_shop)):
        for n in range(len(m_shop[i])):
            if m_shop[i][n]==0:
                pygame.draw.rect(DISPLAY, background, (n*40,i*40,40,40))
            elif m_shop[i][n] == 1:
                pygame.draw.rect(DISPLAY,walls,(n*40,i*40, 40,40))
                pygame.draw.rect(DISPLAY,w_border,(n*40,i*40, 40,40),3)
            else:
                pygame.draw.rect(DISPLAY, door, (n*40,i*40, 40, 40))
    char = pygame.draw.rect(DISPLAY, player, (x,y,40,40))
    print(x,y)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x>0:
                    if DISPLAY.get_at((int(x-(40)),int(y)))[0] == door[0]:
                        outside(DISPLAY, 80,320,m_outside)
                    elif DISPLAY.get_at((int(x-(40)),int(y)))[0] != w_border[0]:
                        shop(DISPLAY, x-(40),y,m_outside)
                if event.key == pygame.K_RIGHT and x<display_width-(40):
                    if DISPLAY.get_at((int(x+(40)),int(y)))[0] == door[0]:
                        outside(DISPLAY, 80,320, m_outside)
                    elif DISPLAY.get_at((int(x+(40)),int(y)))[0] != w_border[0]:
                        shop(DISPLAY, x+(40),y,m_outside)
                if event.key == pygame.K_UP and y>0:
                    if DISPLAY.get_at((int(x),int(y-(40))))[0]== door[0]:
                        outside(DISPLAY, 80,320, m_outside)
                    if DISPLAY.get_at((int(x),int(y-(40))))[0] != w_border[0]:
                        shop(DISPLAY, x,y-(40),m_outside)
                if event.key == pygame.K_DOWN and y<display_height-(40):
                    if DISPLAY.get_at((int(x),int(y+(40))))[0] == door[0]:
                        outside(DISPLAY, 80,320, m_outside)
                    if DISPLAY.get_at((int(x),int(y+(40))))[0] != w_border[0]:
                        shop(DISPLAY, x,y+(40),m_outside)

def outside(DISPLAY, x, y, m_outside):
    for i in range(len(m_outside)):
        for n in range(len(m_outside[i])):
            if m_outside[i][n]==7:
                g=randint(0,1)
                if g==0:
                    DISPLAY.blit(grass, (n*40,i*40))
                    m_outside[i][n]=8
                else:
                    DISPLAY.blit(grass, (n*40,i*40))
                    DISPLAY.blit(grass3, (n*40,i*40))
                    m_outside[i][n]=6
            elif m_outside[i][n] == 1:
                pygame.draw.rect(DISPLAY,walls,(n*40,i*40, 40,40))
                pygame.draw.rect(DISPLAY,w_border,(n*40,i*40, 40,40),3)
            elif m_outside[i][n] == 2:
                pygame.draw.rect(DISPLAY,door2,(n*40,i*40, 40,40))
            elif m_outside[i][n] == 4:
                pygame.draw.rect(DISPLAY,door3,(n*40,i*40, 40,40))
            elif m_outside[i][n] == 5:
                DISPLAY.blit(path,(n*40,i*40))
            elif m_outside[i][n] == 6:
                DISPLAY.blit(grass, (n*40,i*40))
            elif m_outside[i][n] == 8:
                DISPLAY.blit(grass, (n*40,i*40))
                DISPLAY.blit(grass3, (n*40,i*40))
            else:
                pygame.draw.rect(DISPLAY, door, (n*40,i*40, 40, 40))
    char = pygame.draw.rect(DISPLAY, player, (x,y,40,40))
    pygame.display.update()
    outside(DISPLAY, 400,360, m_outside)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x>0:
                    if DISPLAY.get_at((int(x-(40)),int(y)))[0] == door2[0]:
                        shop(DISPLAY, 400,760,m_outside)
                    elif DISPLAY.get_at((int(x-(40)),int(y)))[0] == door[0]:
                        heal(DISPLAY, 400,760,m_outside)
                    elif DISPLAY.get_at((int(x-(40)),int(y)))[0] == door3[0]:
                        gym(DISPLAY, 400,760,m_outside)
                    elif DISPLAY.get_at((int(x-(40)),int(y)))[0] != w_border[0]:
                        outside(DISPLAY, x-(40),y,m_outside)
                if event.key == pygame.K_RIGHT and x<display_width-(40):
                    if DISPLAY.get_at((int(x+(40)),int(y)))[0] == door2[0]:
                        shop(DISPLAY, 400,760, m_outside)
                    elif DISPLAY.get_at((int(x+(40)),int(y)))[0] == door[0]:
                        heal(DISPLAY, 400,760,m_outside)
                    elif DISPLAY.get_at((int(x+(40)),int(y)))[0] == door3[0]:
                        gym(DISPLAY,400,760,m_outside)
                    elif DISPLAY.get_at((int(x+(40)),int(y)))[0] != w_border[0]:
                        outside(DISPLAY, x+(40),y,m_outside)
                if event.key == pygame.K_UP and y>0:
                    if DISPLAY.get_at((int(x),int(y-(40))))[0]== door2[0]:
                        shop(DISPLAY, 400,760, m_outside)
                    elif DISPLAY.get_at((int(x),int(y-(40))))[0] == door[0]:
                        heal(DISPLAY, 400,760,m_outside)
                    elif DISPLAY.get_at((int(x),int(y-(40))))[0] == door3[0]:
                        gym(DISPLAY, 400,760,m_outside)
                    elif DISPLAY.get_at((int(x),int(y-(40))))[0] != w_border[0]:
                        outside(DISPLAY, x,y-(40),m_outside)
                if event.key == pygame.K_DOWN and y<display_height-(40):
                    if DISPLAY.get_at((int(x),int(y+(40))))[0] == door2[0]:
                        shop(DISPLAY, 400,760,m_outside)
                    elif DISPLAY.get_at((int(x),int(y+(40))))[0] == door[0]:
                        heal(DISPLAY, 400,760,m_outside)
                    elif DISPLAY.get_at((int(x),int(y+(40))))[0] == door3[0]:
                        gym(DISPLAY, 400,760,m_outside)
                    elif DISPLAY.get_at((int(x),int(y+(40))))[0] != w_border[0]:
                        outside(DISPLAY, x,y+(40),m_outside)

def game_loop(m_outside):
    gameExit = False
    DISPLAY.fill(background)
    buttonplay = pygame.draw.rect(DISPLAY, (86,224,51), (320, 600, 150, 75))
    pygame.draw.rect(DISPLAY, red, (320, 600, 150, 75), 5)
    myfont = pygame.font.SysFont('Calibri', 60)
    textsurface = myfont.render('PLAY', False, red)
    DISPLAY.blit(textsurface,(337,612))
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if buttonplay.collidepoint(pos):
                    outside(DISPLAY, 400,360, m_outside)
        pygame.display.update()
game_loop(m_outside)