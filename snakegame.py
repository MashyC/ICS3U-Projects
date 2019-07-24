import pygame
import math
import random
pygame.font.init()

class cube(object):
    across = 40
    w = 600
    def __init__(self,start,directx=1,directy=0,colour=(247, 165, 226)):
        self.pos = start
        self.directx = 1
        self.directy = 0
        self.colour = colour

        
    def move(self, directx, directy):
        self.directx = directx
        self.directy = directy
        self.pos = (self.pos[0] + self.directx, self.pos[1] + self.directy)

    def build(self, face):
        shape = self.w / self.across
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(face, self.colour, (i*shape+1,j*shape+1, shape-2, shape-2))


class snake(object):
    bod = []
    turn = {}
    def __init__(self, colour, pos):
        self.colour = colour
        self.head = cube(pos)
        self.bod.append(self.head)
        self.directx = 0
        self.directy = 1

    def move(self, timer, timer2):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()
        
            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.directx = -1
                    self.directy = 0
                    self.turn[self.head.pos[:]] = [self.directx, self.directy]

                elif keys[pygame.K_RIGHT]:
                    self.directx = 1
                    self.directy = 0
                    self.turn[self.head.pos[:]] = [self.directx, self.directy]

                elif keys[pygame.K_UP]:
                    self.directx = 0
                    self.directy = -1
                    self.turn[self.head.pos[:]] = [self.directx, self.directy]

                elif keys[pygame.K_DOWN]:
                    self.directx = 0
                    self.directy = 1
                    self.turn[self.head.pos[:]] = [self.directx, self.directy]

        for x, y in enumerate(self.bod):
            n = y.pos[:]
            if n in self.turn:
                turns = self.turn[n]
                y.move(turns[0],turns[1])
                if x == len(self.bod)-1:
                    self.turn.pop(n)
            else:
                if y.directx == -1 and y.pos[0] <= 0:
                    print('Score: ', len(char.bod))
                    char.restart((10,10), timer, timer2)
                elif y.directx == 1 and y.pos[0] >= y.across-1:
                    print('Score: ', len(char.bod))
                    char.restart((10,10), timer, timer2)
                elif y.directy == 1 and y.pos[1] >= y.across-1:
                    print('Score: ', len(char.bod))
                    char.restart((10,10), timer, timer2)
                elif y.directy == -1 and y.pos[1] <= 0:
                    print('Score: ', len(char.bod))
                    char.restart((10,10), timer, timer2)
                else:
                    y.move(y.directx,y.directy)
        

    def restart(self, pos, timer, timer2):
        print("YOU HAVE DIED")
        timer=160
        timer2=160
        self.head = cube(pos)
        self.bod = []
        self.bod.append(self.head)
        self.turn = {}
        self.directx = 0
        self.directy = 1
        print(timer, timer2)


    def add(self):
        tail = self.bod[-1]
        dirx, diry = tail.directx, tail.directy

        if dirx == 1 and diry == 0:
            self.bod.append(cube((tail.pos[0]-1,tail.pos[1])))
        elif dirx == -1 and diry == 0:
            self.bod.append(cube((tail.pos[0]+1,tail.pos[1])))
        elif dirx == 0 and diry == 1:
            self.bod.append(cube((tail.pos[0],tail.pos[1]-1)))
        elif dirx == 0 and diry == -1:
            self.bod.append(cube((tail.pos[0],tail.pos[1]+1)))

        self.bod[-1].directx = dirx
        self.bod[-1].directy = diry
        

    def build(self, face):
        for x, y in enumerate(self.bod):
            y.build(face)
        

def updated(face, timer):
    global across, width, char, food;
    face.fill((0,0,0))
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    timer_text = myfont.render(str(timer), False, (127, 87, 229))
    face.blit(timer_text, (250, 400))
    char.build(face)
    food.build(face)
    pygame.display.update()


def eat(across, item):

    positions = item.bod

    while True:
        x = random.randrange(across)
        y = random.randrange(across)
        if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0:
            continue
        else:
            break
        
    return (x,y)


def main():
    global width, across, char, food
    across = 40
    width = 600
    pygame.display.set_caption("Python")
    window = pygame.display.set_mode((width, width))
    char = snake((247, 165, 226), (10,10))
    food = cube(eat(across, char), colour=(247, 165, 226))



    flag = True

    clock = pygame.time.Clock()
    timer = 160
    timer2 = 160
    while flag:
        timer-=1
        if timer%10==0:
            timer2-=1
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        timer_text = myfont.render('daya bad', False, (127, 87, 229))
        window.blit(timer_text, (250, 400))

        pygame.time.delay(10)
        if timer2 > 100 and timer2 < 160:
            clock.tick(5)
        elif timer2 > 55 and timer2 < 100:
            clock.tick(9)
        elif timer2 > 25 and timer2 < 55:
            clock.tick(15)
        elif timer2 > 10 and timer2 < 25:
            clock.tick(25)
        elif timer2 < 10:
            clock.tick(40)
            
        char.move(timer, timer2)

        if char.bod[0].pos == food.pos:
            char.add()
            food = cube(eat(across, char), colour=(247, 165, 226))

        for x in range(len(char.bod)):
            if char.bod[x].pos in list(map(lambda z:z.pos,char.bod[x+1:])):
                print('Score: ', len(char.bod))
                char.restart((10,10), timer, timer2)
                break
   
        updated(window, timer2) 
main()
