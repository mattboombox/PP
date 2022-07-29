import pygame
import random

#variables
screenLength = 1920
screenHeight = 1080
fps = 15

#Import pygame stuff
pygame.init()
screen = pygame.display.set_mode((screenLength, screenHeight))
clock = pygame.time.Clock()

#Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill(((random.randint(0, 255) , random.randint(0, 255) , random.randint(0, 255))))

    pygame.display.update()
    clock.tick(fps)

