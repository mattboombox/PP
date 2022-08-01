import pygame
import random

screen_length = 1000
screen_height = 500

speed = 1

player = pygame.Rect(200, 200, 50, 50)
z1 = pygame.Rect(random.randint(0, 500),  random.randint(0, 500), 50, 50)
z2 = pygame.Rect(random.randint(0, 500),  random.randint(0, 500), 50, 50)
z3 = pygame.Rect(random.randint(0, 500),  random.randint(0, 500), 50, 50)
z4 = pygame.Rect(random.randint(0, 500),  random.randint(0, 500), 50, 50)
z5 = pygame.Rect(random.randint(0, 500),  random.randint(0, 500), 50, 50)
z6 = pygame.Rect(random.randint(0, 500),  random.randint(0, 500), 50, 50)
z7 = pygame.Rect(random.randint(0, 500),  random.randint(0, 500), 50, 50)
z8 = pygame.Rect(random.randint(0, 500),  random.randint(0, 500), 50, 50)
z9 = pygame.Rect(random.randint(0, 500),  random.randint(0, 500), 50, 50)
z10 = pygame.Rect(random.randint(0, 500),  random.randint(0, 500), 50, 50)

pygame.init()

screen = pygame.display.set_mode((screen_length, screen_height))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    #if a key is pressed
    if event.type == pygame.KEYDOWN:
        #If the down arrow key is pressed
        if event.key == pygame.K_DOWN:
            player.move_ip(0, 1)
        #If the up arrow key is pressed
        if event.key == pygame.K_UP:
            player.move_ip(0, -1)
        #If the left arrow key is pressed
        if event.key == pygame.K_LEFT:
            player.move_ip(-1, 0)
        #If the right arrow ley is pressed
        if event.key == pygame.K_RIGHT:
            player.move_ip(1, 0)
        #Reset player
            if event.key == pygame.K_RETURN:
                    player.x = 50
                    player.y = 50

    screen.fill((133, 179, 121))
    pygame.draw.rect(screen, (56,23,0), player)
    pygame.draw.rect(screen, (0,90,0), z1)
    pygame.draw.rect(screen, (0,90,0), z2)
    pygame.draw.rect(screen, (0,90,0), z3)
    pygame.draw.rect(screen, (0,90,0), z4)
    pygame.draw.rect(screen, (0,90,0), z5)
    pygame.draw.rect(screen, (0,90,0), z6)
    pygame.draw.rect(screen, (0,90,0), z7)
    pygame.draw.rect(screen, (0,90,0), z8)
    pygame.draw.rect(screen, (0,90,0), z9)
    pygame.draw.rect(screen, (0,90,0), z10)
    pygame.display.update()
    clock.tick(60)

    print("working")

    
