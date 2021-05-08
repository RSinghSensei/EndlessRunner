import pygame

pygame.init()

clock = pygame.time.Clock()
tp = time.time()

screen = pygame.display.set_mode((1920,540))
screen.fill((255,253,208))
fontB = pygame.font.Font("Pixeboy-z8XGD.ttf",128)
fontS = pygame.font.Font("Pixeboy-z8XGD.ttf",64)
text1 = fontB.render("Runner",True,(0,0,0))
text2 = fontB.render("GAME OVER",True,(0,0,0))

#Player Rect
h1 = pygame.Rect(240,470,30,30)
p_score = 0
d = 5
d1 = 10

#Enemy 1
e1 = pygame.Rect(480, 100, 40, 40)
mve1 = e1.x + 50
e2 = pygame.Rect(440, 60, 40,40)
mve2 = e2.x - 50
e3 = pygame.Rect(520,120,40,40)
mve3 = e3.x + 100
enemy_list = [e1,e2,e3]
enemyActive = False

#Boss Fight
boss_e1 = pygame.Rect(2520,135,355,355)
bossFight = False
bossScore = 0

#Player-gun rect
h1_gun = pygame.Rect(h1.x + 15,h1.y + 15,10,10)
gun = False

#Black Platform
bb = pygame.Rect(0,500,1920,50)
bb1 = pygame.Rect(1920,500,1920,50)
bp = pygame.Rect(0,0,1920,50)
bp1 = pygame.Rect(1920,0,1920,50)

#Block Obstacles
h2 = pygame.Rect(1000,450,40,50)
h2_1 = pygame.Rect(1950,450,40,50)
l = [h2,h2_1]

#Bird Obstacle
h3 = pygame.Rect(2100,400,120,50)

#PowerUp
p1 = pygame.Rect(2000,470,30,30)

#Lava Blocks
p2 = pygame.Rect(2200,500,50,50)

#Jump and Back Mechanic
g = False
j = False

#Background image(not currently used)
bg1 = pygame.image.load("bg1.jpg")
bg1_rect = bg1.get_rect()
bg2_rect = bg1.get_rect()
# bg1x = 2

def death(y5):
    enemy_list.remove(y5)

def gun_line():
    global e1, x, y
    x, y = pygame.mouse.get_pos()
    if gun:
        pygame.draw.line(screen,(255,255,255),(h1.x - 20,h1.y),(x,y),2)
        if pygame.MOUSEBUTTONDOWN:
            if e1.collidepoint(x,y) or e1.y > 540:
                pygame.draw.line(screen,(255,0,0),(h1.x-20,h1.y),(x,y),10)
                death(e1)
                e1.x,e1.y = random.randint(350,700),random.randint(50,200)
                enemy_list.append(e1)
            if e2.collidepoint(x,y) or e2.y > 540:
                pygame.draw.line(screen,(255,0,0),(h1.x-20,h1.y),(x,y),10)
                death(e2)
                e2.x,e2.y = random.randint(700,1920),random.randint(50,200)
                enemy_list.append(e2)
            if e3.collidepoint(x,y) or e3.y > 540:
                pygame.draw.line(screen,(255,0,0),(h1.x-20,h1.y),(x,y),10)
                death(e3)
                e3.x,e3.y = random.randint(0,100),random.randint(0,50)
                enemy_list.append(e3)

    # if pygame.MOUSEBUTTONDOWN:
    #     pygame.draw.line(screen,(255,0,0),(h1.x,h1.y),(x,y),2)
    #     print("Pressed")

def enemies():
    if enemyActive:
        for i2 in enemy_list:
            pygame.draw.rect(screen,(248,248,255),i2)
            if i2 == e1:
                if i2.x < random.randint(mve1,mve1 + 200):
                    i2.x+=random.randint(2,5)
                    i2.y+=random.randint(2,5)
                else:
                    pygame.draw.circle(screen,(255,0,0),(e1.left - 7,e1.bottom),5)
            if i2 == e2:
                if i2.x > random.randint(mve2 - 200, mve2 - 50):
                    i2.x-=random.randint(2,5)
                    i2.y+=random.randint(2,5)
                else:
                    pygame.draw.circle(screen,(255,0,0),(e2.right - 15, e2.bottom),5)
            if i2 == e3:
                if i2.x < random.randint(mve3,mve3 + 250):
                    i2.x+=random.randint(2,5)
                    i2.y+=random.randint(2,5)
                else:
                    pygame.draw.circle(screen,(255,0,0),(e3.left - 5,e3.bottom),5)


def timed_event():
    pass


def moving_screen():
    pygame.draw.rect(screen,(0,0,0),bb)
    pygame.draw.rect(screen,(0,0,0),bb1)
    pygame.draw.rect(screen,(0,0,0),bp)
    pygame.draw.rect(screen,(0,0,0),bp1)
    # screen.blit(bg1,bg1_rect)
    # screen.blit(bg1,(bg2_rect.x+1920,0))

def double_jump():
    pass

def check():
    if bb1.x < 0:
        bb1.x = 0
    if bb.x < 0:
        bb.x = 0
    if bp.x < 0:
        bp.x = 0
    if bp1.x < 0:
        bp1.x = 0

def grav():
    global g
    if g:
        h1.y+=25
        if h1.y > 470:
            # pygame.draw.circle(screen, (0, 0, 252), (h1.right, h1.y + 40), 10)
            # pygame.draw.circle(screen, (0, 0, 252), (h1.left, h1.y + 40), 10)
            h1.y = 470
            g = False

def jump():
    global j, g
    if j:
        h1.y-=20
        if h1.y < 200:
            h1.y = 200
            j = False
            g = True

def pallete():
    global enemyActive, bossFight, gun
    if p_score < 500:
        screen.fill( (131, 18, 165))
    if 501 < p_score < 1000:
        screen.fill((114, 11, 152))
        screen.blit(fontS.render("lol still playing yeah?", True, (0, 0, 0)), (0, 300))
    if 1001 < p_score < 1500:
        screen.fill((86, 20, 150))
    if 1501 < p_score < 2000:
        screen.fill((57, 30, 148))
    if 2001 < p_score < 2500:
        screen.fill((29, 39, 145))
    if 2501 < p_score < 3000:
        screen.fill((0, 55, 165))
        screen.blit(fontS.render("Hmph, you're pretty good at this y'know...",True,(0,0,0)),(0,300))
    if 3001 < p_score < 3100:
        screen.fill((0, 55, 165))
        screen.blit(fontS.render("Here, grab this laser.. Kill as many as you can before their laser charges",True,(0,0,0)),(0,300))
        gun = True
    if 3101 < p_score < 3200:
        screen.fill((27, 3, 163))
        enemyActive = True
    if 3201 < p_score < 3500:
        screen.fill((33, 53, 134))
    if 3501 < p_score < 4000:
        screen.fill((39, 104, 106))
    if 4001 < p_score < 4500:
        screen.fill((45, 154, 77))
    if 4501 < p_score < 5000:
        screen.fill((51, 205, 49))
    if 5001 < p_score < 6000:
        screen.fill((57, 255, 20))
        e1.y-=0.5
        e2.y-=.5
        e3.y-=.5
    if 6001 < p_score < 6200:
        screen.fill((57,255,20))
        enemyActive = False
    if 6001 < p_score:
        screen.fill((0,0,0))
        bossFight = True
        bossBattle()

winnerM = fontB.render("WIN",True,(255,255,255))


def bossBattle():
    global x,y,bossScore
    pygame.draw.rect(screen,(255,255,255),boss_e1)
    if boss_e1.x > 1520:
        boss_e1.x-=10
    elif boss_e1.x <= 1520:
        c1 = pygame.draw.circle(screen, (255, 0, 0), (boss_e1.x, random.randint(boss_e1.y, boss_e1.y + 355)), 10)
        if c1.collidepoint(x,y):
            print(bossScore)
            bossScore+=1
    if bossScore >=5:
        screen.blit(winnerM,(900,270))


def obstacles():
    global d, d1, s1, s2, s3, s4, bossFight

    if not bossFight:
        #Block Obstacle Spawner
        for id in l:
            pygame.draw.rect(screen,(255,255,0),id)

        # s2 = pygame.draw.circle(screen, (255, 0, 0), (p2.x - 5, p2.y - 15), 15)
        # s3 = pygame.draw.circle(screen, (255, 0, 0), (p2.x + 10, p2.y - 5), 15)
        # s4 = pygame.draw.circle(screen, (255, 0, 0), (p2.x + 15, p2.y - 10), 15)

        #Bird Spawner
        pygame.draw.rect(screen,(0,0,255),h3)
        pygame.draw.line(screen,(0,0,0),(h3.right + random.randint(5,30),h3.y - 5),(h3.right + random.randint(7,90),h3.y - 5 ),5)
        pygame.draw.line(screen, (0,0,0), (h3.right + random.randint(30,50), h3.y + 25), (h3.right + random.randint(90,120), h3.y + 25),5)
        pygame.draw.line(screen, (0,0,0), (h3.right + random.randint(5,30), h3.y + 55 ), (h3.right + random.randint(7,90), h3.y + 55),5)

        #Powerup Spawner
        pygame.draw.rect(screen, (252, 212, 64), p1)

        #Lava Spawner + Particle System (Working on it)
        pygame.draw.rect(screen, (207, 16, 32), p2)


        #Block Speed
        h2.x -=10
        h2_1.x -=10

        #Bird Speed
        h3.x -=20

        #Power-up speed
        p1.x -=10
        #Lava block speed
        p2.x -=10

        # s1.centerx -= 10

        #Values on passing them
        if h2.right < 0:
            h2.x = random.randint(1925,3000)
        if h2_1.right < 0:
            h2_1.x = random.randint(2500,3500)
        if h3.right < 0:
            h3.x = random.randint(5000,10000)
        if p1.x < 0:
            p1.x = random.randint(5000,10000)
        if p2.x < 0:
            s1.y = p2.y
            s2.y = p2.y
            s3.y = p2.y
            s4.y = p2.y
            d = 0
            d1 = 0
            p2.x = random.randint(2000,4000)
        if 0 <= p2.x < 1920:
            d+=(random.randint(1,5))
            d1+=(random.randint(-5,5))

def lava():
    global s1,s2,s3,s4
    s1 = pygame.draw.circle(screen, (255, 0, 0), (p2.x + d1, p2.y - d),7)
    s2 = pygame.draw.circle(screen, (247, 0, 0), (p2.x + (d1*1.1), p2.y - d), 8)
    s3 = pygame.draw.circle(screen, (255, 0, 0), (p2.x - (d1*0.5), p2.y - d), 7)
    s4 = pygame.draw.circle(screen, (255, 0, 0), (p2.x - d1, p2.y - d), 5)


def collision_check():
    if h1.colliderect(h2) or h1.colliderect(h2_1) or h1.colliderect(h3):
        pause()
    if h1.colliderect(p1):
        p1.x = random.randint(3000,10000)
        powerup()

def powerup():
    global h1
    h1 = pygame.Rect(240,450,100,50)


def pause():
    global pause1, running
    pause1 = True
    while pause1:
        for event1 in pygame.event.get():
            if event1.type == pygame.QUIT:
                pause1 = False
                running = False
            if event1.type == pygame.KEYDOWN:
                if event1.key == pygame.K_r or event1.key == pygame.K_SPACE:
                    pause1 = False
                    running = True
        screen.blit(text2,(750,200))
        pygame.display.update()

running = False
menu = True
pause1 = False

while menu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                menu = False
                running = True
    moving_screen()
    screen.blit(text1,(750,200))
    bg1_rect.x-=1
    bg2_rect.x-=1
    pygame.display.update()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                j = True
    pallete()
    gun_line()
    jump()
    grav()
    moving_screen()
    if not bossFight:
        bb.x-=10
        bb1.x-=10
    check()
    obstacles()
    lava()
    # collision_check()
    pygame.draw.rect(screen,(255,255,255),h1)
    pygame.draw.rect(screen,(0,0,0),h1_gun)
    p_score+=1
    enemies()
    pygame.display.update()
    clock.tick(60)
