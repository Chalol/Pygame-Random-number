# This  code is about random a number 
# for subject Software development and practice I
# Code by 6001012630021  Chanakan  Thimkham 

import pygame, sys
from pygame.locals import *
import random
from buttonnum import *

pygame.init()                                    # initialize pygame
#color
colormbred = (208,23,42)
coloryellow = (255,191,23)
colormbblue = (178,232,232)
colormbgreen = (90,224,58)
colorsofty = (255,248,183)
colorwhite = (255,255,255)
colorblack = (0,0,0)

DISP = pygame.display.set_mode((340,580))        #set width and height of display
pygame.display.set_caption('Random')
fontText = pygame.font.SysFont('Arial',30)       #set font and font size that will show on screen
DISP.fill(colorblack)                            #set screen color
width = 80
height = 60
width1 = 100

# set x,y,width,height,color and text on each button
num = []
for i in range(28,0,-1):
    num.append(i)

for x in range(10,270,80):
    for y in range(50,500,65):
        buttonnum(x,y,width,height,colormbred,str(num.pop())).btnum()

ranbut = buttonnum(120,510,width1,height,colormbred,'Random')

def random_loop():
    ty = True
    Num = " "
    while ty:
        ranbut.btrandom()
        
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                ty = False

            if e.type == pygame.MOUSEBUTTONDOWN:          # Mouse click input
                mouse = pygame.mouse.get_pos()            # get mouse position
                if ranbut.finalbut().collidepoint(mouse):
                    num = []
                    for i in range(28,0,-1):
                        num.append(i)
                        random.shuffle(num)

                    for x in range(10,270,80):
                        for y in range(50,500,65):
                            buttonnum(x,y,width,height,colormbred,str(num.pop())).btnum()

        pygame.display.update()            # Update portions of the screen

random_loop()                                 # call function to run programme
pygame.quit()                              # uninitialize all pygame modules
quit()