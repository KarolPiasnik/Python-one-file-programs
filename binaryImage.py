import pygame

width = 800
height = 800
gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption("Binary Image")
clock = pygame.time.Clock()


black = (0,0,0)
white = (255,255,255)

def mainLoop():
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        clock.tick(10)



    
imgIn = input("Enter your bitmap image")
imgOut = ""
count = 0
for char in imgIn:
    if count % 6 == 0:
        imgOut += '\n'
    count+=1

    if char == '1':
        imgOut += '*'
    else:
        imgOut+= ' '
        
    
print(imgOut)
mainLoop()
