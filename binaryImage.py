import pygame

width = 200
height = 200
imageDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption("Binary Image")

clock = pygame.time.Clock()
pygame.init()

size = 10 # size of units to be drawn
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
some = (255,255,0)
some2 = (255,0,255)
some3 = (0,255,255)
colors = [black,white,red,green,blue,some,some2,some3]
imageDisplay.fill((155,155,155))
content = open('image.txt', 'r').read()


def makeImageWB(): #print image white and black
    count = 0 # needed to calculate where to draw
    for char in content[1:]:
        if char == '1':
            pygame.draw.rect(imageDisplay,white,(count%(width//size)*size, count//(width//size)*size, size, size))
        elif char == '0':
            pygame.draw.rect(imageDisplay,black,(count%(width//size)*size, count//(width//size)*size, size, size))
        count += 1

def makeImage8Color(): #print image white and black
    color = 0
    count = 0 # needed to calculate where to draw
    for char in content[1:]:
        if count % 3 == 2:
                count -= 2
                pygame.draw.rect(imageDisplay,colors[color],(count%(width//size)*size, count//(width//size)*size, size, size))
                color = 0
        else:
            color += 2**(count%3)
            
        count += 1

def introLoop():
    while(True):
        for event in pygame.event.get(): #event handling loop
                if event.type == pygame.QUIT:
                    pygame.quit()
        pygame.display.update()
        clock.tick(10)
if content[0] == '0':                  
    makeImageWB()
else:
    makeImage8Color()
introLoop()    

