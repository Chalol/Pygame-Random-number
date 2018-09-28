import pygame, sys
from pygame.locals import *

pygame.init()                                    # initialize pygame
#color
colormbred = (208,23,42)
coloryellow = (255,191,23)
colormbblue = (178,232,232)
colormbgreen = (90,224,58)
colorsofty = (255,248,183)
colorwhite = (255,255,255)
colorblack = (0,0,0)

DISP = pygame.display.set_mode((350,580))        #set width and height of display
pygame.display.set_caption('Random')
fontText = pygame.font.SysFont('Arial',30)       #set font and font size that will show on screen
DISP.fill(colorblack)                            #set screen color
width = 80
height = 60
width1 = 100

class buttonnum():
    
    def __init__(self,x,y,width,height,color,text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        
    def btnum(self):                             
        pygame.draw.rect(DISP,colormbred,(self.x,self.y,self.width,self.height))
        DISP.blit(fontText.render(self.text,True,colorwhite),(self.x+30,self.y+10))

    def btrandom(self):
        pygame.draw.rect(DISP,colormbred,(self.x,self.y,self.width,self.height))
        DISP.blit(fontText.render(self.text,True,colorwhite),(self.x,self.y+10)) 
               
    def finalbut(self):                        #function that will using for check x,y aka mouse position
        return pygame.draw.rect(DISP,colormbred,(self.x,self.y,self.width,self.height))
