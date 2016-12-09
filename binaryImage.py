import pygame

width = 800
height = 800
imageDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption("Binary Image")

clock = pygame.time.Clock()
pygame.init()


black = (0,0,0)
white = (255,255,255)
imageDisplay.fill(white)


def mainLoop():
    count = 0 #pixel counter

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    imageDisplay.set_at((count%width, count//height), black)
                    count+=1
                elif event.key == pygame.K_1:
                    imageDisplay.set_at((count%width, count//height), white)
                    count+=1

        pygame.display.update()
        clock.tick(10)



    

mainLoop()
