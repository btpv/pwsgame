# Example file showing a basic pygame "game loop"
import pygame
pygame.init()
screen_width, screen_height = 1400, 771
win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jour Fun Time")
width = 128
height = 128
vel = 5
x = screen_width // 2 - width // 2
y = screen_height - height
vel = 5


walksheet = pygame.image.load('walk.png')
jumpsheet = pygame.image.load('jump.png')
walkright = [walksheet.subsurface(pygame.Rect(i * 128, 0, 128, 128)) for i in range(11)]
walkleft = [walksheet.subsurface(pygame.Rect(i * 128, 128, 128, 128)) for i in range(11)]
jumpleft = [jumpsheet.subsurface(pygame.Rect(i * 128, 0, 128, 128)) for i in range(11)]
jumpright = [jumpsheet.subsurface(pygame.Rect(i * 128, 128, 128, 128)) for i in range(11)]

Idle_left = pygame.image.load('Idleleft.png')
Idle_right = pygame.image.load('Idleright.png')
char = Idle_right
bg = pygame.image.load('bg.jpg')

clock = pygame.time.Clock()

isjumping = False
jumpcount = 10
left=False
right=True
walkcount=0
jumpframe = 0
idle=False

def redrawgamewindow():
    global walkcount
    global jumpframe
    win.blit(bg, (0,0))
    if isjumping:
        if jumpframe + 1 >= 33:
            jumpframe = 0
        if left:
            win.blit(jumpleft[jumpframe//3], (x, y))
            jumpframe += 1
        elif right:
            win.blit(jumpright[jumpframe//3], (x, y))
            jumpframe += 1
    elif idle and left:
        win.blit(Idle_left, (x, y))
    elif idle and right:
        win.blit(Idle_right, (x, y))
    else:
        if walkcount + 1 >= 33:
            walkcount = 0
        if left:
            win.blit(walkleft[walkcount//3], (x, y))
            walkcount += 1
        elif right:
            win.blit(walkright[walkcount//3], (x, y))
            walkcount += 1
    pygame.display.update()   

run = True
while run:
    idle=False
    clock.tick(33)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= vel
        left=True
        right=False
    elif keys[pygame.K_RIGHT] and x < screen_width - width:
        x += vel
        left=False
        right=True
    else:
        walkcount=0
    if not (isjumping): 
        if keys[pygame.K_SPACE]:
            isjumping = True
            walkcount=0
    else:
        if jumpcount >= -10:
            if jumpcount < 0:
                y += (jumpcount ** 2) * 0.5
            else:
                y -= (jumpcount ** 2) * 0.5
            jumpcount -= 1
        else:
            isjumping = False
            jumpcount = 10
            jumpframe = 0
    if keys[pygame.K_LEFT] == False and keys[pygame.K_RIGHT] == False and not(isjumping):
        idle=True
        walkcount=0
    print(left, right, isjumping, idle)
    redrawgamewindow()
pygame.quit()           