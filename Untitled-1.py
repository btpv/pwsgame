# Example file showing a basic pygame "game loop"
import pygame
pygame.init()
screen_width, screen_height = 500, 500
win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jour Fun Time")
width = 40
height = 60
vel = 5
x = screen_width // 2 - width // 2
y = screen_height - height
width = 40
height = 60
vel = 5

isjumping = False
jumpcount = 10
left=False
right=False
walkcount=0

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

    if not (isjumping): 
        if keys[pygame.K_SPACE]:
            isjumping = True
    else:
        if jumpcount >= -10:
            if jumpcount < 0:
                y += (jumpcount ** 2) * 0.5
            else:
                y -= (jumpcount ** 2) * 0.5
            jumpcount -= 1
            print (jumpcount)
        else:
            isjumping = False
            jumpcount = 10
    win.fill((63, 63, 255))
    pygame.draw.rect(win, (100, 100, 100), (x, y, width, height))
    pygame.display.update()       
pygame.quit()           