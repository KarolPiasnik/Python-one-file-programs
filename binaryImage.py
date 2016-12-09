import pygame

width = 800
height = 800
gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption("Binary Image")
clock = pygame.time.Clock()


black = (0,0,0)
white = (255,255,255)
count = 0

def mainLoop():
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        clock.tick(10)



    

mainLoop()
