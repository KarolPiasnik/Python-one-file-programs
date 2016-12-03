import pygame
import random
import time
import math

pygame.init()

paused = False
running = True
displayWidth = 800
displayHeight = 600

black = (0,0,0)
white = (255,255,255)

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
brightRed = (255,0,0)
brightGreen = (0,255,0)
gray = (111,111,111)
lightGray = (188,188,188)

gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
clock = pygame.time.Clock()
pygame.display.set_caption('Pong')



def textObjects(text, font, color = black): # textsurface  generator
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def button(msg = 'hello', action = None, x=0, y=0, width = 100, height = 50, activeColor = lightGray, inactiveColor = gray, textColor = black, textSize = 20):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+width > mouse[0] > x and y+height > mouse[1] > y:
        pygame.draw.rect(gameDisplay, activeColor, (x,y,width,height))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, inactiveColor, (x,y,width,height))

    text = pygame.font.Font('freesansbold.ttf',textSize)
    textSurf, textRect = textObjects(msg, text, textColor)
    textRect.center = (x + (width/2), y + (height/2))

    gameDisplay.blit(textSurf, textRect)
    
#################################################### functions that run the game
    
def gameQuit():
    pygame.quit()
    quit()
    
def gameDraw():
    pass

def gameIntro():
    global running
    running = True
    while running:
        
        
        for event in pygame.event.get():
            if event == pygame.QUIT:
                gameQuit()

        gameDisplay.fill(white)
        
        ###################### all the drawing here
        button('Single Player',gameSingle, displayWidth/2 - 75, 200, 150)
        button('Multiplayer',gameMulti, displayWidth/2 - 75, 300, 150)
        button('Options',gameOptions, displayWidth/2 - 75, 400, 150)
        ######################
        
        pygame.display.update()
        clock.tick(60)

def gameOptions():
    global running
    running = True
    while running:
        
        
        for event in pygame.event.get():
            if event == pygame.QUIT:
                gameQuit()

        gameDisplay.fill(white)
        
        ###################### all the drawing here
        button('Single Player', gameSingle, displayWidth/2 - 75, 200, 150)
        button('Multiplayer', gameMulti, displayWidth/2 - 75, 300, 150)
        button('Options', gameOptions, displayWidth/2 - 75, 400, 150)
        ######################
        
        pygame.display.update()
        clock.tick(60)
def gameResume():
    global paused
    paused = False
def gamePause():
    global paused
    paused = True
    while paused:
        
        
        for event in pygame.event.get():
            if event == pygame.QUIT:
                gameQuit()

        gameDisplay.fill(white)
        
        ###################### all the drawing here
        button('Resume', gameResume, displayWidth/2 - 75, 300, 150)
        ######################
        
        pygame.display.update()
        clock.tick(60)
    
def gameSingle():
    global running
    running = True
    
    barWidth = 50 #bar variables and limes
    barHeight = 120
    barSpeed = 7
    x1 = 0
    x2 = displayWidth - barWidth
    y1 = y2 = displayHeight/2 - barHeight/2
    limesWidth = displayWidth/50
    limesHeight = displayHeight/40

    #ball and score variables
    ballSize = 10
    ballX = round(displayWidth/2 - ballSize/2)
    ballY = round(displayHeight/2 - ballSize/2)
    ballSpeed = 13
    ballAlfa = 25
    score1 = score2 = 0
    
    
    while running:
        #######################Handling exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameQuit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    gamePause()
                elif event.key == pygame.K_o:
                    gameOptions()
        ######################Game logic            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and y2-barSpeed >= 0:
            y2 -= barSpeed
        if keys[pygame.K_DOWN] and y2+barSpeed <= displayHeight-barHeight:
            y2 += barSpeed
        #Artificial intelligence
        if ballY > y1+barHeight/2 and y1+barSpeed <= displayHeight-barHeight:
            y1 += barSpeed+3
        elif y1-barSpeed >= 0:
            y1 -= barSpeed+3

        
        #ball movement

        if ballX > displayWidth:
            score1 += 1
            ballX = round(displayWidth/2 - ballSize)
            ballY = round(displayHeight/2 - ballSize)
        elif ballX < 0:
            score2 += 1
            ballX = round(displayWidth/2 - ballSize)
            ballY = round(displayHeight/2 - ballSize)
        elif ballY < ballSize:
            ballY = ballSize
            if 0 < ballAlfa < 90:
                ballAlfa += 270
            else:
                ballAlfa += 90
        elif ballY > displayHeight-ballSize:
            ballY = displayHeight-ballSize
            if 270 < ballAlfa < 360:
                ballAlfa -= 270
            else:
                ballAlfa -= 90
        if y1 - ballSize < ballY < y1 + ballSize + barHeight and 0 - ballSize < ballX < barWidth + ballSize :
            ballX = barWidth + ballSize
            if 180 < ballAlfa < 270:
                ballAlfa += 45+45*math.fabs((((y1+barHeight/2)-ballY)/(barHeight/2)))
            else:
                ballAlfa -= 45+45*math.fabs((((y1+barHeight/2)-ballY)/(barHeight/2)))
        if y2 - ballSize < ballY < y2 + ballSize + barHeight and displayWidth - barWidth - ballSize < ballX < displayWidth:
            ballX = displayWidth - barWidth - ballSize
            if 0 < ballAlfa < 90:
                ballAlfa += 45+45*math.fabs((((y2+barHeight/2)-ballY)/(barHeight/2)))
            else:
                ballAlfa -= 45+45*math.fabs((((y2+barHeight/2)-ballY)/(barHeight/2)))
        
        ballAlfa = ballAlfa % 360
        ballX += (-1)*math.cos(math.radians(ballAlfa))*ballSpeed
        ballY += (-1)*math.sin(math.radians(ballAlfa))*ballSpeed
        
        ###################### all the drawing here
        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay,black,(x1,y1,barWidth,barHeight))
        pygame.draw.rect(gameDisplay,black,(x2,y2,barWidth,barHeight))

        i = 0 # Loop drawing border between sides
        while i < 40:
            if i % 2 == 0:   
                pygame.draw.rect(gameDisplay,black,(displayWidth/2 - limesWidth, limesHeight*i, limesWidth, limesHeight))
            i+=1
        
        
        pygame.draw.circle(gameDisplay, red, (round(ballX),round(ballY)), ballSize)

        text = pygame.font.Font('freesansbold.ttf',round(displayHeight/20))
        textSurf, textRect = textObjects(str(score1), text, green)
        textRect.center = (displayWidth*0.1, displayHeight*0.1)
        gameDisplay.blit(textSurf, textRect)
        text = pygame.font.Font('freesansbold.ttf',round(displayHeight/20))
        textSurf, textRect = textObjects(str(score2), text, green)
        textRect.center = (displayWidth*0.9, displayHeight*0.1)
        gameDisplay.blit(textSurf, textRect)
        ###################### Screen update
        
        pygame.display.update()
        clock.tick(60)
        


def gameMulti():
    global running
    running = True
    
    barWidth = 50 #bar variables and limes
    barHeight = 120
    barSpeed = 5
    x1 = 0
    x2 = displayWidth - barWidth
    y1 = y2 = displayHeight/2 - barHeight/2
    limesWidth = displayWidth/50
    limesHeight = displayHeight/40

    #ball and score variables
    ballSize = 10
    ballX = round(displayWidth/2 - ballSize/2)
    ballY = round(displayHeight/2 - ballSize/2)
    ballSpeed = 10
    ballAlfa = 25
    score1 = score2 = 0
    
    
    while running:
        #######################Handling exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameQuit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    gamePause()
                elif event.key == pygame.K_o:
                    gameOptions()
        ######################Game logic            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and y2-barSpeed >= 0 :
            y2 -= barSpeed
        if keys[pygame.K_DOWN] and y2+barSpeed <= displayHeight-barHeight:
            y2 += barSpeed
        if keys[pygame.K_w] and y1-barSpeed >= 0:
            y1 -= barSpeed
        if keys[pygame.K_s] and y1+barSpeed <= displayHeight-barHeight:
            y1 += barSpeed

        #ball movement

        if ballX > displayWidth:
            score1 += 1
            ballX = round(displayWidth/2 - ballSize)
            ballY = round(displayHeight/2 - ballSize)
        elif ballX < 0:
            score2 += 1
            ballX = round(displayWidth/2 - ballSize)
            ballY = round(displayHeight/2 - ballSize)
        elif ballY < ballSize:
            ballY = ballSize
            if 0 < ballAlfa < 90:
                ballAlfa += 270
            else:
                ballAlfa += 90
        elif ballY > displayHeight-ballSize:
            ballY = displayHeight-ballSize
            if 270 < ballAlfa < 360:
                ballAlfa -= 270
            else:
                ballAlfa -= 90
        if y1 - ballSize < ballY < y1 + ballSize + barHeight and 0 - ballSize < ballX < barWidth + ballSize :
            ballX = barWidth + ballSize
            if 180 < ballAlfa < 270:
                ballAlfa += 45+45*math.fabs((((y1+barHeight/2)-ballY)/(barHeight/2)))
            else:
                ballAlfa -= 45+45*math.fabs((((y1+barHeight/2)-ballY)/(barHeight/2)))
        if y2 - ballSize < ballY < y2 + ballSize + barHeight and displayWidth - barWidth - ballSize < ballX < displayWidth:
            ballX = displayWidth - barWidth - ballSize
            if 0 < ballAlfa < 90:
                ballAlfa += 45+45*math.fabs((((y2+barHeight/2)-ballY)/(barHeight/2)))
            else:
                ballAlfa -= 45+45*math.fabs((((y2+barHeight/2)-ballY)/(barHeight/2)))
        
        ballAlfa = ballAlfa % 360
        ballX += (-1)*math.cos(math.radians(ballAlfa))*ballSpeed
        ballY += (-1)*math.sin(math.radians(ballAlfa))*ballSpeed
        
        ###################### all the drawing here
        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay,black,(x1,y1,barWidth,barHeight))
        pygame.draw.rect(gameDisplay,black,(x2,y2,barWidth,barHeight))

        i = 0 # Loop drawing border between sides
        while i < 40:
            if i % 2 == 0:   
                pygame.draw.rect(gameDisplay,black,(displayWidth/2 - limesWidth, limesHeight*i, limesWidth, limesHeight))
            i+=1
        
        
        pygame.draw.circle(gameDisplay, red, (round(ballX),round(ballY)), ballSize)

        text = pygame.font.Font('freesansbold.ttf',round(displayHeight/20))
        textSurf, textRect = textObjects(str(score1), text, green)
        textRect.center = (displayWidth*0.1, displayHeight*0.1)
        gameDisplay.blit(textSurf, textRect)
        text = pygame.font.Font('freesansbold.ttf',round(displayHeight/20))
        textSurf, textRect = textObjects(str(score2), text, green)
        textRect.center = (displayWidth*0.9, displayHeight*0.1)
        gameDisplay.blit(textSurf, textRect)
        ###################### Screen update
        
        pygame.display.update()
        clock.tick(60)
        


################################################# MAIN

gameIntro()
gameQuit()
        
