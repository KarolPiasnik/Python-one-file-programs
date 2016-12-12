import sys
import pygame
import threading
from time import sleep
import numpy as np
from copy import deepcopy
## s - start loop
## q - quit
## left mouse - live cell
## other mouse - dead cell
## WORKS ONLY AFTER START 
## p - increase speed
## o - decrease speed


width = 800
height = 800
gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption("Conway's Game of Life")
clock = pygame.time.Clock()


black = (0,0,0)
white = (255,255,255)


rows = 100
columns = 100
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
    
def introLoop(world):
    running = True
    while(running):
        for event in pygame.event.get(): #event handling loop
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameQuit()
                    elif event.key == pygame.K_s:
                        running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if event.button == 1:
                        world[(pos[1]//(height//rows))][(pos[0]//(width//columns))] = True
                    else:
                        world[(pos[1]//(height//rows))][(pos[0]//(width//columns))] = False
        pygame.event.clear()
        printLoop(world)
        clock.tick(10)
                    
    
    

def mainLoop(world):
    
    speed = 15 #default framerate
    count = 0;#counter of neighbours
    while(True):
        for event in pygame.event.get(): #event handling loop
            if event.type == pygame.QUIT:
                gameQuit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    gameQuit()
                if event.key == pygame.K_p and speed < 120:
                    speed+=1
                if event.key == pygame.K_o and speed > 1:
                    speed-=1
        pygame.event.clear()
    
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
        clock.tick(speed)            
        


introLoop(world)
mainLoop(world)
