# Example file showing a basic pygame "game loop"
import pygame
pygame.init()
screen_width, screen_height = 700, 406
win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jour Fun Time")
width = 128
height = 128
hits = 0
hit = 0
developer_mode = True

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isjumping = False
        self.isatacking = False
        self.attackframe = 0
        self.jumpcount = 10
        self.left = False
        self.right = True
        self.walkcount = 0
        self.jumpframe = 0
        self.idle = False
        self.hitbox = (self.x + 19, self.y + 53, 85, 74)
        self.running = False
        self.runcount = 0
        self.health = 99

    def draw(self, win):
        if self.isatacking:
            if self.attackframe + 1 >= 18:
                self.attackframe = 0
                self.isatacking = False
            if self.left:
                win.blit(attackleft[self.attackframe // 3], (self.x, self.y))
            elif self.right:
                win.blit(attackright[self.attackframe // 3], (self.x, self.y))
            self.attackframe += 1
        elif self.isjumping:
            if self.jumpframe + 1 >= 33:
                self.jumpframe = 0
            if self.left:
                win.blit(jumpleft[self.jumpframe // 3], (self.x, self.y))
            elif self.right:
                win.blit(jumpright[self.jumpframe // 3], (self.x, self.y))
            self.jumpframe += 1
        elif self.running:
            if self.runcount + 1 >= 27:
                self.runcount = 0
            if self.left:
                win.blit(runleft[self.runcount // 3], (self.x, self.y))
            elif self.right:
                win.blit(runright[self.runcount // 3], (self.x, self.y))
            self.runcount += 1
        elif self.idle and self.left:
            win.blit(Idle_left, (self.x, self.y))
        elif self.idle and self.right:
            win.blit(Idle_right, (self.x, self.y))
        else:
            if self.walkcount + 1 >= 33:
                self.walkcount = 0
            if self.left:
                win.blit(walkleft[self.walkcount // 3], (self.x, self.y))
            elif self.right:
                win.blit(walkright[self.walkcount // 3], (self.x, self.y))
            self.walkcount += 1
        self.hitbox = (self.x + 19, self.y + 53, 85, 74)
        if developer_mode:
            pygame.draw.rect(win, (255,0,0), (self.x + 19, self.y + 53, 85 // 2, 74),2)
            pygame.draw.rect(win, (255,0,0), self.hitbox,2)
            # White box around wolf
            white_box = pygame.Rect(self.x, self.y, self.width, self.height)
            pygame.draw.rect(win, (255,255,255), white_box, 2)
        
walksheet_zombie = pygame.image.load('assets/zombies/wild_zombie/Walk.png')

class enemy(object):
    walkright = [walksheet_zombie.subsurface(pygame.Rect(i * 96, 0, 96, 96)) for i in range(14)]
    walkleft = [walksheet_zombie.subsurface(pygame.Rect(i * 96, 96, 96, 96)) for i in range(14)]
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 3
        self.walkcount = 0
        self.hitbox = (self.x + 24, self.y + 50, 50, 45)
        self.health = 10
        self.left = False
        self.right = True
        self.idle = False

    def draw(self, win):
        self.move()
        if self.walkcount + 1 >= 42:
            self.walkcount = 0
        if self.vel > 0:
            win.blit(self.walkright[self.walkcount // 3], (self.x, self.y))
            self.right = True
            self.left = False
            self.idle = False
        elif self.vel < 0:
            win.blit(self.walkleft[self.walkcount // 3], (self.x, self.y))
            self.left = True
            self.right = False
            self.idle = False
        else:
            self.idle = True
            if self.right:
                win.blit(self.walkright[self.walkcount // 3], (self.x, self.y))
            elif self.left:
                win.blit(self.walkleft[self.walkcount // 3], (self.x, self.y))
        self.walkcount += 1
        self.hitbox = (self.x + 24, self.y + 50, 50, 45)
        if developer_mode:
            pygame.draw.rect(win, (255,0,0), self.hitbox,2)
            pygame.draw.rect(win, (255,0,0), (self.x + 24, self.y + 50, 25, 45),2)
            white_box = pygame.Rect(self.x, self.y, self.width, self.height)
            pygame.draw.rect(win, (255,255,255), white_box, 2)
    def move(self):
        if abs (self.hitbox[0] - (wolf.x + (wolf.width // 2))) > 3:
            if self.hitbox[0] < ((wolf.x + (wolf.width // 2)-2)):
                self.vel = 3
                self.x += self.vel
        else:
            self.vel = 0


x = screen_width // 2 - width // 2
y = screen_height - height - 23
wolf = player(x, y, width, height)

walksheet = pygame.image.load('assets/player/walk.png')
jumpsheet = pygame.image.load('assets/player/jump.png')
runsheet = pygame.image.load('assets/player/run.png')
attacksheet = pygame.image.load('assets/player/attack_1.png')
attackright = [attacksheet.subsurface(pygame.Rect(i * 128, 0, 128, 128)) for i in range(6)]
attackleft = [attacksheet.subsurface(pygame.Rect(i * 128, 128, 128, 128)) for i in range(6)]
walkright = [walksheet.subsurface(pygame.Rect(i * 128, 0, 128, 128)) for i in range(11)]
walkleft = [walksheet.subsurface(pygame.Rect(i * 128, 128, 128, 128)) for i in range(11)]
jumpleft = [jumpsheet.subsurface(pygame.Rect(i * 128, 0, 128, 128)) for i in range(11)]
jumpright = [jumpsheet.subsurface(pygame.Rect(i * 128, 128, 128, 128)) for i in range(11)]
runright = [runsheet.subsurface(pygame.Rect(i * 128, 0, 128, 128)) for i in range(9)]
runleft = [pygame.transform.flip(frame, True, False) for frame in runright]

Idle_left = pygame.image.load('assets/player/idleleft.png')
Idle_right = pygame.image.load('assets/player/Idleright.png')
bg = pygame.image.load('assets/bg.png')
bg = pygame.transform.scale(bg, (screen_width, screen_height))

scene = 0

def next_scene():
    global scene, bg
    scene += 1
    if scene == 1:
        bg = pygame.image.load('assets/bg.jpg')
        bg = pygame.transform.scale(bg, (screen_width, screen_height))
    else:
        scene = 0
        bg = pygame.image.load('assets/bg.png')
        bg = pygame.transform.scale(bg, (screen_width, screen_height))

def previous_scene():
    global scene, bg
    scene -= 1
    if scene < 0:
        scene = 1
    if scene == 1:
        bg = pygame.image.load('assets/bg.jpg')
        bg = pygame.transform.scale(bg, (screen_width, screen_height))
    else:
        bg = pygame.image.load('assets/bg.png')
        bg = pygame.transform.scale(bg, (screen_width, screen_height))

clock = pygame.time.Clock()

def redrawgamewindow():
    win.blit(bg, (0,0))
    wolf.draw(win)
    wild_zombie.draw(win)
    pygame.display.update()   

wild_zombie = enemy(100, screen_height - 96 - 23, 96, 96, 600)
run = True
while run:
    wolf.idle = False
    clock.tick(33)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]) and ((keys[pygame.K_LEFT] or keys[pygame.K_a]) or (keys[pygame.K_RIGHT] or keys[pygame.K_d])):
        wolf.running = True
        wolf.vel = 6
    else:
        wolf.running = False
        wolf.vel = 3
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]):
        wolf.x -= wolf.vel
        wolf.left = True
        wolf.right = False
    elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]):
        wolf.x += wolf.vel
        wolf.left = False
        wolf.right = True
    else:
        wolf.walkcount = 0
    if wolf.x + wolf.width/2 >= screen_width:
        next_scene()
        wolf.x = 0 - wolf.width/3
    elif wolf.x <= 0 - wolf.width/2:
        previous_scene()
        wolf.x = screen_width - wolf.width/3*2
    if not wolf.isjumping: 
        if keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]:
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
    if keys[pygame.K_f] and not wolf.isatacking:
        wolf.isatacking = True
    if not (keys[pygame.K_LEFT] or keys[pygame.K_a]) and not (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and not wolf.isjumping and not wolf.isatacking:
        wolf.idle = True
        wolf.walkcount = 0
        wolf.runcount = 0
    if wolf.hitbox[1] < wild_zombie.hitbox[1] + wild_zombie.hitbox[3] and wolf.hitbox[1] + wolf.hitbox[3] > wild_zombie.hitbox[1]:
        if wolf.hitbox[0] + wolf.hitbox[2] > wild_zombie.hitbox[0] and wolf.hitbox[0] < wild_zombie.hitbox[0] + wild_zombie.hitbox[2]:
            if (wild_zombie.walkcount > 36 and  wild_zombie.walkcount < 40) and ((wild_zombie.right and (wolf.x + (wolf.width // 2)) > (wild_zombie.x + (wild_zombie.width // 2))) or (wild_zombie.left and (wolf.x + (wolf.width // 2)) < (wild_zombie.x + (wild_zombie.width // 2)))):
                hits +=1
                wolf.health -= 1
            if wolf.isatacking and (wolf.attackframe > 12 and wolf.attackframe < 16) and ((wolf.right and (wolf.x + (wolf.width // 2)) < (wild_zombie.x + (wild_zombie.width // 2))) or (wolf.left and (wolf.x + (wolf.width // 2)) > (wild_zombie.x + (wild_zombie.width // 2)))):
                hit +=1
                wild_zombie.health -= 1
    if wolf.health <= 0:
        print("You Died")
        run = False
    #print("left:", wolf.left, "jumping:", wolf.isjumping, "idle:", wolf.idle, "atacking:", wolf.isatacking)
    redrawgamewindow()
    print("wolf hitbox:", wolf.hitbox, "zombie hitbox:", wild_zombie.hitbox)
    print()
    #print(wild_zombie.x, wolf.x, wild_zombie.vel, wolf.health, hits, hit)
if run == False:
    diedsheet = pygame.image.load('assets/player/dead.png')
    diedright = [diedsheet.subsurface(pygame.Rect(i * 128, 0, 128, 128)) for i in range(2)]
    diedleft = [diedsheet.subsurface(pygame.Rect(i * 128, 128, 128, 128)) for i in range(2)]
    win.blit(bg, (0,0))
    wild_zombie.draw(win)
    if wolf.left:
        win.blit(diedleft[0], (wolf.x, wolf.y))
    else:
        win.blit(diedright[0], (wolf.x, wolf.y))
    pygame.display.update()
    pygame.time.delay(500)
    win.blit(bg, (0,0))
    wild_zombie.draw(win)
    if wolf.left:
        win.blit(diedleft[1], (wolf.x, wolf.y))
    else:
        win.blit(diedright[1], (wolf.x, wolf.y))
    pygame.display.update()
    pygame.time.delay(2000)
    
pygame.quit()