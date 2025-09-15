# Example file showing a basic pygame "game loop"
import pygame
pygame.init()
screen_width, screen_height = 700, 406
win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jour Fun Time")
width = 128
height = 128

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isjumping = False
        self.jumpcount = 10
        self.left = False
        self.right = True
        self.walkcount = 0
        self.jumpframe = 0
        self.idle = False

x = screen_width // 2 - width // 2
y = screen_height - height - 23
wolf = player(x, y, width, height)

walksheet = pygame.image.load('assets/walk.png')
jumpsheet = pygame.image.load('assets/jump.png')
walkright = [walksheet.subsurface(pygame.Rect(i * 128, 0, 128, 128)) for i in range(11)]
walkleft = [walksheet.subsurface(pygame.Rect(i * 128, 128, 128, 128)) for i in range(11)]
jumpleft = [jumpsheet.subsurface(pygame.Rect(i * 128, 0, 128, 128)) for i in range(11)]
jumpright = [jumpsheet.subsurface(pygame.Rect(i * 128, 128, 128, 128)) for i in range(11)]

Idle_left = pygame.image.load('assets/Idleleft.png')
Idle_right = pygame.image.load('assets/Idleright.png')
bg = pygame.image.load('assets/bg.png')

clock = pygame.time.Clock()

def redrawgamewindow():
    win.blit(bg, (0,0))
    if wolf.isjumping:
        if wolf.jumpframe + 1 >= 33:
            wolf.jumpframe = 0
        if wolf.left:
            win.blit(jumpleft[wolf.jumpframe//3], (wolf.x, wolf.y))
        elif wolf.right:
            win.blit(jumpright[wolf.jumpframe//3], (wolf.x, wolf.y))
        wolf.jumpframe += 1
    elif wolf.idle and wolf.left:
        win.blit(Idle_left, (wolf.x, wolf.y))
    elif wolf.idle and wolf.right:
        win.blit(Idle_right, (wolf.x, wolf.y))
    else:
        if wolf.walkcount + 1 >= 33:
            wolf.walkcount = 0
        if wolf.left:
            win.blit(walkleft[wolf.walkcount//3], (wolf.x, wolf.y))
            wolf.walkcount += 1
        elif wolf.right:
            win.blit(walkright[wolf.walkcount//3], (wolf.x, wolf.y))
            wolf.walkcount += 1
    pygame.display.update()   

run = True
while run:
    wolf.idle = False
    clock.tick(33)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and wolf.x > 0:
        wolf.x -= wolf.vel
        wolf.left = True
        wolf.right = False
    elif keys[pygame.K_RIGHT] and wolf.x < screen_width - wolf.width:
        wolf.x += wolf.vel
        wolf.left = False
        wolf.right = True
    else:
        wolf.walkcount = 0
    if not wolf.isjumping: 
        if keys[pygame.K_SPACE]:
            wolf.isjumping = True
            wolf.walkcount = 0
    else:
        if wolf.jumpcount >= -10:
            if wolf.jumpcount < 0:
                wolf.y += (wolf.jumpcount ** 2) * 0.5
            else:
                wolf.y -= (wolf.jumpcount ** 2) * 0.5
            wolf.jumpcount -= 1
        else:
            wolf.isjumping = False
            wolf.jumpcount = 10
            wolf.jumpframe = 0
    if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not wolf.isjumping:
        wolf.idle = True
        wolf.walkcount = 0
    print(wolf.left, wolf.right, wolf.isjumping, wolf.idle)
    redrawgamewindow()
pygame.quit()