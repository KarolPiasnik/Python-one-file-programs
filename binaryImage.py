import pygame

width = 1200
height = 1000
imageDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption("Binary Image")

clock = pygame.time.Clock()
pygame.init()

size = 3 # size of units to be drawn
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
magenta = (255,0,255)
cyan = (0,255,255)
colors = [black,white,red,green,blue,yellow,magenta,cyan]

imageDisplay.fill((155,155,155))
content = open('image.txt', 'r').read()


def makeImageWB(): #print image white and black
    count = 0 # needed to calculate where to draw
    for char in content[2:]:
        if char == '1':
            pygame.draw.rect(imageDisplay,white,(count%(width//size)*size, count//(width//size)*size, size, size))
        elif char == '0':
            pygame.draw.rect(imageDisplay,black,(count%(width//size)*size, count//(width//size)*size, size, size))
        count += 1

def makeImage8Color(): #print image in 8 colors
    color = 0
    count = 0 # needed to calculate where to draw
    for char in content[2:]: #this condition is responsible for reading colors from file
        if char == '1':
            color += 2**(count%3)
        count += 1
        if count % 3 == 2:
                pygame.draw.rect(imageDisplay,colors[color],((count//3)%(width//size)*size, (count//3)//(width//size)*size, size, size))
                color = 0
        

def makeImageRGB(): #print image in 8 colors
    rgb = [0,0,0]
    color = 0
    count = 0 # needed to calculate where to draw
    for char in content[2:]: #this condition is responsible for reading colors from file
        if char == '1':
            rgb[(count % 24) // 8] += 2**(count%8) #first eight chars are red, then ble,green
        
        count += 1
        if count % 24 == 23:
                pygame.draw.rect(imageDisplay,(rgb[0],rgb[1],rgb[2]),((count//24)%(width//size)*size, (count//24)//(width//size)*size, size, size))
                rgb = [0,0,0]
 

                
def mainLoop():
    while(True):
        for event in pygame.event.get(): #event handling loop
                if event.type == pygame.QUIT:
                    pygame.quit()
        pygame.display.update()
        clock.tick(10)
        
if content[0] == '0' and content[1] == '0' :                  
    makeImageWB()
elif content[0] == '1' and content[1] == '0':
    makeImage8Color()
elif content[0] == '1' and content[1] == '1':
    makeImageRGB()
else:
    pass

mainLoop()    

