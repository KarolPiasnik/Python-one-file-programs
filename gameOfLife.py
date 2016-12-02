import sys
from copy import deepcopy

rows = 20
columns = 20
world = [ [' ' for column in range(0,columns)] for row in range(0,rows) ]
for row in range(0,rows):
    for column in range(0,columns):
        if(column == 0 or row == 0 or column == columns -1 or row == rows-1):
            world[row][column] = '#'
        elif row % 4 == 0 and column % 2 == 0:
            world[row][column] = ' '
        else:
            world[row][column] = ' '


world[12][15] = '*'
world[12][14] = '*'
world[11][13] = '*'
world[11][15] = '*'
world[10][15] = '*'




world2 = deepcopy(world)

count = 0;
for i in range(20):
    for row in range(1,rows-1):
        for column in range(1,columns-1):
            count = 0
            for row1 in range(-1,2):
                for column1 in range(-1,2):
                    if column+column1<columns-1 and row+row1<rows-1 and column+column1>-0 and row+row1>0:
                        if world[row+row1][column+column1] == '*':
                            count=count+1
                            
            if world[row][column] == '*':
                count-=1
                if count >3 or count < 2:
                    world2[row][column] = ' '
            elif count == 3:
                world2[row][column] = '*'
                
    world = deepcopy(world2)            
                    
                    

    for row in range(0,rows):
        sys.stdout.write('\n')
        for column in range(0,columns):
            sys.stdout.write(world[row][column])

                
