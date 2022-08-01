import pygame
import random

screen_length = 1500
screen_height = 700
fps = 60

size = 10

speed = 1
player_speed = 2
player_XV = 0
player_YV = 0

player = pygame.Rect(200, 200, size, size)
z1 = pygame.Rect(random.randint(0, 500),  random.randint(0, 500), size, size)
z2 = pygame.Rect(random.randint(0, 500),  random.randint(0, 500), size, size)
z3 = pygame.Rect(random.randint(0, 500),  random.randint(0, 500), size, size)
z4 = pygame.Rect(random.randint(0, 500),  random.randint(0, 500), size, size)
z5 = pygame.Rect(random.randint(0, 500),  random.randint(0, 500), size, size)
z6 = pygame.Rect(random.randint(0, 500),  random.randint(0, 500), size, size)
z7 = pygame.Rect(random.randint(0, 500),  random.randint(0, 500), size, size)
z8 = pygame.Rect(random.randint(0, 500),  random.randint(0, 500), size, size)
z9 = pygame.Rect(random.randint(0, 500),  random.randint(0, 500), size, size)
z10 = pygame.Rect(random.randint(0, 500),  random.randint(0, 500), size, size)

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
            player_YV = player_speed
        #If the up arrow key is pressed
        if event.key == pygame.K_UP:
            player_YV = -player_speed
        #If the left arrow key is pressed
        if event.key == pygame.K_LEFT:
            player_XV = -player_speed
        #If the right arrow ley is pressed
        if event.key == pygame.K_RIGHT:
            player_XV = player_speed
        #Reset player
        if event.key == pygame.K_RETURN:
            player.x = 0
            player.y = 0
            player_XV = 0
            player_YV = 0

    #Z movements
    if z1.x > player.x:
        z1.move_ip(-speed, 0)
    else:
        z1.move_ip(speed, 0)

    if z1.y > player.y:
        z1.move_ip(0, -speed)
    else:
        z1.move_ip(0, speed)

    if z2.x > player.x:
        z2.move_ip(-speed, 0)
    else:
        z2.move_ip(speed, 0)

    if z2.y > player.y:
        z2.move_ip(0, -speed)
    else:
        z2.move_ip(0, speed)

    if z3.x > player.x:
        z3.move_ip(-speed, 0)
    else:
        z3.move_ip(speed, 0)

    if z3.y > player.y:
        z3.move_ip(0, -speed)
    else:
        z3.move_ip(0, speed)

    if z4.x > player.x:
        z4.move_ip(-speed, 0)
    else:
        z4.move_ip(speed, 0)

    if z4.y > player.y:
        z4.move_ip(0, -speed)
    else:
        z4.move_ip(0, speed)

    if z5.x > player.x:
        z5.move_ip(-speed, 0)
    else:
        z5.move_ip(speed, 0)

    if z5.y > player.y:
        z5.move_ip(0, -speed)
    else:
        z5.move_ip(0, speed)

    if z6.x > player.x:
        z6.move_ip(-speed, 0)
    else:
        z6.move_ip(speed, 0)

    if z6.y > player.y:
        z6.move_ip(0, -speed)
    else:
        z6.move_ip(0, speed)

    if z7.x > player.x:
        z7.move_ip(-speed, 0)
    else:
        z7.move_ip(speed, 0)

    if z7.y > player.y:
        z7.move_ip(0, -speed)
    else:
        z7.move_ip(0, speed)

    if z8.x > player.x:
        z8.move_ip(-speed, 0)
    else:
        z8.move_ip(speed, 0)

    if z8.y > player.y:
        z8.move_ip(0, -speed)
    else:
        z8.move_ip(0, speed)

    if z9.x > player.x:
        z9.move_ip(-speed, 0)
    else:
        z9.move_ip(speed, 0)

    if z9.y > player.y:
        z9.move_ip(0, -speed)
    else:
        z9.move_ip(0, speed)

    if z10.x > player.x:
        z10.move_ip(-speed, 0)
    else:
        z10.move_ip(speed, 0)

    if z10.y > player.y:
        z10.move_ip(0, -speed)
    else:
        z10.move_ip(0, speed)

    player.move_ip(player_XV, player_YV)

    print("", player_XV, player_YV, player.x, player.y)

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
    clock.tick(fps)
