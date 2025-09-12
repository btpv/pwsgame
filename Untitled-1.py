# Example file showing a basic pygame "game loop"
import pygame
pygame.init()
screen_width, screen_height = 500, 500
win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jour Fun Time")
x = screen_width // 2
y = screen_height // 2
width = 40
height = 60
vel = 5

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= vel
    if keys[pygame.K_RIGHT] and x < screen_width - width:
        x += vel
    if keys[pygame.K_UP] and y > 0:
        y -= vel
    if keys[pygame.K_DOWN] and y < screen_height - height:
        y += vel   
    win.fill((63, 63, 255))
    pygame.draw.rect(win, (100, 100, 100), (x, y, width, height))
    pygame.display.update()       
pygame.quit()           