import pygame
import random

pygame.init()

FLOOR = 400
HEIGHT = 600
LENGTH = 1000
SPOTX = 400
SPOTY = 400
SPEED1 = 1
SPEED2 = 2

screen = pygame.display.set_mode((LENGTH, HEIGHT))
clock = pygame.time.Clock()

#Things
plant = pygame.Rect(random.randint(0, 500),  random.randint(0, 500), 50, 50)
prey = pygame.Rect(random.randint(0, 500),  random.randint(0, 500), 50, 50)
predator = pygame.Rect(200, 200, 50, 50)

while True:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    #prey movements
    if prey.x > plant.x:
        prey.move_ip(-SPEED2, 0)
    else:
        prey.move_ip(SPEED2, 0)
    
    if prey.y > plant.y:
        prey.move_ip(0, -SPEED2)
    else:
        prey.move_ip(0, SPEED2)

    #predator movements
    if predator.x > prey.x:
        predator.move_ip(-SPEED1, 0)
    else:
        predator.move_ip(SPEED1, 0)

    if predator.y > prey.y:
        predator.move_ip(0, -SPEED1)
    else:
        predator.move_ip(0, SPEED1)

    #plant prey hit detection
    if plant.colliderect(prey) == True:
        plant.x = random.randint(0, LENGTH)
        plant.y = random.randint(0, HEIGHT)

    #Prey predator collision
    if prey.colliderect(predator) == True:
        prey.x = random.randint(0, LENGTH)
        prey.y = random.randint(0, HEIGHT)

    screen.fill((133, 179, 121))
    pygame.draw.rect(screen, (0,90,0), plant)
    pygame.draw.rect(screen, (255,255,255), prey)
    pygame.draw.rect(screen, (204, 110, 43), predator)
    pygame.display.update()
    clock.tick(60)