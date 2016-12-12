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

content = open('image.txt', 'r').read()




    

