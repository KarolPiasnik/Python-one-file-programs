import sys
import pygame
import threading
from time import sleep
import numpy as np
from copy import deepcopy

width = 800
height = 800
gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption("Conway's Game of Life")
clock = pygame.time.Clock()


black = (0,0,0)
white = (255,255,255)


rows = 40
columns = 40
world = np.ndarray((rows,columns))


world = [ [' ' for column in range(0,columns)] for row in range(0,rows) ]
for row in range(0,rows):
    for column in range(0,columns):
            world[row][column] = False
        

world[12][15] = True
world[12][14] = True
world[11][13] = True
world[11][15] = True
world[10][15] = True



world2 = deepcopy(world)

def gameQuit():
    pygame.quit()
    quit()
    
def printLoop(world):
    gameDisplay.fill(white)

    for row in range(0,rows):
        for column in range(0,columns): 
            if world[row][column]:
                pygame.draw.rect(gameDisplay,black,(column*(width/columns), row*(height/rows), (width/columns), height/rows))
    
    pygame.display.update()
    
        
def mainLoop(world):
     for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameQuit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    gameQuit()
                #elif event.key == pygame.K_o:
                    #gameOptions()
                    
    count = 0;
    while(True):
        for row in range(0,rows):
            for column in range(0,columns):
                count = 0
                for row1 in range(-1,2):
                    for column1 in range(-1,2):
                        if column+column1<columns-1 and row+row1<rows-1 and column+column1>-0 and row+row1>0:
                            if world[row+row1][column+column1] == True:
                                count=count+1
                                
                if world[row][column] == True:
                    count-=1
                    if count >3 or count < 2:
                        world2[row][column] = False
                elif count == 3:
                    world2[row][column] = True
                    
        world = deepcopy(world2)

        
    
        printLoop(world)          
        clock.tick(15)            
        


mainLoop(world)
