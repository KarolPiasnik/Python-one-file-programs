import pygame

width = 800
height = 800
imageDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption("Binary Image")

clock = pygame.time.Clock()
pygame.init()

size = 10 # size of units to be drawn
black = (0,0,0)
white = (255,255,255)
imageDisplay.fill((155,155,155))

content = open('image.txt', 'r').read()
count = 0 # needed to calculate where to draw
for char in content:
    if char == '1':
        pygame.draw.rect(gameDisplay,black,(column*(width/columns), row*(height/rows), (width/columns), height/rows))
    elif char == '0':
        pygame.draw.rect(gameDisplay,black,(column*(width/columns), row*(height/rows), (width/columns), height/rows))
    count += 1

def introLoop():
    while(True):
        for event in pygame.event.get(): #event handling loop
                if event.type == pygame.QUIT:
                    pygame.quit()
                
        clock.tick(10)
                    

introLoop()    

