#CONTROLS
#Arrow keys: Increase the velocity of square in the four directions
#Enter/Return: Resets the postion of the square   

#FEATURES:
#Gravity: The square is influenced by a constant downward acceleration
#Bouncing: The square will have its velocity in the Y direction reversed and reduced if it hits the floor
#Friction: While the square's Y postion is less than or equal to the floor, its X velocity will slow to 0 

import pygame
import random

pygame.init()

X = 100
Y = 100
XV = 0
YV = 0
GRAVITY = 0.05 #Recommended value for gravity is 0.05
SPEED = 1
FRICTION = 0.02
FLOOR = 400
HEIGHT = 500
LENGTH = 1300

screen = pygame.display.set_mode((LENGTH, HEIGHT))
clock = pygame.time.Clock()
square = pygame.Surface((100, 100))
square.fill((227, 131, 118))

while True:
    #draw all elements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        #if a key is pressed
        if event.type == pygame.KEYDOWN:
                #If the down arrow key is pressed
                if event.key == pygame.K_DOWN:
                    print("DOWN")
                    square.fill((random.randint(0, 255) , random.randint(0, 255) , random.randint(0, 255)))
                    YV = YV + SPEED
                #If the up arrow ley is pressed
                if event.key == pygame.K_UP:
                    print("UP")
                    square.fill((random.randint(0, 255) , random.randint(0, 255) , random.randint(0, 255)))
                    YV = YV - SPEED
                #If the left arrow key is pressed
                if event.key == pygame.K_LEFT:
                    print("LEFT")
                    square.fill((random.randint(0, 255) , random.randint(0, 255) , random.randint(0, 255)))
                    XV = XV - SPEED
                #If the right arrow ley is pressed
                if event.key == pygame.K_RIGHT:
                    print("RIGHT")
                    square.fill((random.randint(0, 255) , random.randint(0, 255) , random.randint(0, 255)))
                    XV = XV + SPEED
                #Reset player
                if event.key == pygame.K_RETURN:
                    X = 100
                    Y = 0
                
    #Updating positions based off of X and Y Velocity XV, YV
    X = X + XV
    Y = Y + YV

    #Gravity and Friction
    if Y < FLOOR: 
        YV = YV + GRAVITY
    else:
        Y = 400
        if XV > 0:
            XV = XV - FRICTION
            if XV < .01:
                XV = 0
        else:
            XV = XV + FRICTION
            if XV > -.01:
                XV = 0

    #Bouncing
    if Y == 400:
        if YV > 1:
            YV = ((YV * .5)* -1)

    screen.fill((133, 179, 121))
    screen.blit(square, (X, Y))

    pygame.display.update()
    clock.tick(60)
    print("", X, Y, XV, YV)