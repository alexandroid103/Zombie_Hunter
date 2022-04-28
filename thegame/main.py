import pygame
import sys
import random
import time
import math

pygame.init()
speed = 5
food = 0
x = 600
y = 400
pos_x=random.randint(0,5000)
pos_y=random.randint(0,5000)
zombie_x = random.randint(0, 1200)
zombie_y = random.randint(0, 800)
healz = 3
expireance = 0
lvl = 1
hint_tree = pygame.image.load("hint_tree.png")
loot_box = pygame.image.load("lootbox.png")
aim = pygame.image.load("aim.png")
hints = ["собака была правее", "собака расположена выше", "собака левее", "собака ушла немного ниже",
         "новый лутбокс правее", "новый лутбокс левее", "новый лутбокс выше", "новый лутбокс ниже"]
screen = pygame.display.set_mode((1200, 800))
player = [pygame.image.load("player_right (2).png"), pygame.image.load("player_down (2).png"),
          pygame.image.load("player_up (2).png"), pygame.image.load("player_left (2).png"),
          pygame.image.load("player_left (2).png"), pygame.image.load("player_right_shoot.png"),
          pygame.image.load("player_down_shoot.png"), pygame.image.load("player_left_shoot.png"),
          pygame.image.load("player_up_shoot.png")]
grass = [pygame.image.load("grass1.png"), pygame.image.load("grass2.png"), pygame.image.load("grass3.png"), ]
menu = "game0"
win_screen=pygame.image.load("win_screen.png")
grass_set = [random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), ]
language = "русский"
menu_sprites = [pygame.image.load("settings.png"), pygame.image.load("start.png"), pygame.image.load("exit.png")]
object_x = [random.randint(0, 1200), random.randint(0, 1200), random.randint(0, 1200), random.randint(0, 1200),
            random.randint(0, 1200), random.randint(0, 1200), ]
object_y = [random.randint(0, 800), random.randint(0, 800), random.randint(0, 800), random.randint(0, 800),
            random.randint(0, 800), random.randint(0, 800), ]
tablet_sprites = [pygame.image.load("player_tablet_sprite.png")]
zombies_sprites = [pygame.image.load("zombie_right.png"), pygame.image.load("zombie_left.png"),
                   pygame.image.load("zombie_up.png"), pygame.image.load("zombie_down.png"), ]
r = pygame.Rect(50, 500, 800, 700)
font = pygame.font.SysFont('couriernew', 40)
doge = pygame.image.load("doge.png")
health = 100
food_level = 100
catridges = 100
dialoge = True
interface = pygame.image.load("interface.png")
time = [0, 0, 0]
screen_color = (0, 0, 0)
doge_x = 1
doge_y = 1
loot = True
map_end=pygame.image.load("map_end.png")


def dialoges(tablet_text, sprite):
    if dialoge == True:
        pygame.draw.rect(screen, (0, 0, 0), r, 0)
        tablet = font.render(tablet_text, True, (255, 255, 255))
        screen.blit(tablet, (200, 600))
        screen.blit(sprite, (0, 300))


while True:
    pygame.time.delay(10)
    time[1] += 1
    food_level -= 0.001
    if time[1] >= 60:
        time[1] = 0
        time[0] += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if menu == "game0":
            while doge_x % 5 != 0:
                doge_x = random.randint(0, 1200)
            while doge_y % 5 != 0:
                doge_y = random.randint(0, 800)
            screen.blit(menu_sprites[1], (500, 300))
            screen.blit(menu_sprites[2], (850, 300))
            screen.blit(menu_sprites[0], (200, 300))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] in range(500, 700) and event.pos[1] in range(300, 500):
                    menu = "game1"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] in range(850, 1050) and event.pos[1] in range(300, 500):
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] in range(200, 400) and event.pos[1] in range(300, 500):
                    menu = "settings"
                    screen.fill((0, 0, 0))
        if menu == "settings":
            if event.type == pygame.K_SPACE and language == "русский":
                language = "english"
            if event.type == pygame.K_SPACE and language == "english":
                language = "русский"
            screen.fill((0, 0, 0))
            text = font.render(language, True, (255, 255, 255))
            screen.blit(text, (600, 400))
        if menu == "game1":
            screen.fill((60, 179, 113))
            if time[0] in range(12, 14):
                screen_color = (60, 179, 113)
            elif time[0] in range(14, 16):
                screen_color = (46, 139, 87)
            elif time[0] in range(16, 18):
                screen_color = (34, 139, 34)
            elif time[0] in range(18, 20):
                screen_color = (0, 100, 0)
            elif time[0] in range(20, 22):
                screen_color = (75, 0, 130)
            elif time[0] in range(22, 24):
                screen_color = (106, 90, 205)
            else:
                screen_color = (60, 179, 113)

        if event.type == pygame.KEYDOWN:
            dialoge = False

        dialoges("черт,этот растяпа убежал.", tablet_sprites[0])
    if healz > 0:
        if x > zombie_x:
            screen.fill(screen_color)
            screen.blit(zombies_sprites[0], (zombie_x, zombie_y))
            zombie_x += 1
            if zombie_x == x:
                health -= 1
                zombie_x -= 50
        if x < zombie_x:
            screen.fill(screen_color)
            screen.blit(zombies_sprites[1], (zombie_x, zombie_y))
            zombie_x -= 1
            if zombie_x == x:
                health -= 1
                zombie_x += 50
        if y < zombie_y:
            screen.fill(screen_color)
            screen.blit(zombies_sprites[2], (zombie_x, zombie_y))
            zombie_y -= 1
            if zombie_y == y:
                health -= 1
                zombie_y += 50
        if y > zombie_y:
            screen.fill(screen_color)
            screen.blit(zombies_sprites[3], (zombie_x, zombie_y))
            zombie_y += 1
            if zombie_y == y:
                health -= 1
                zombie_y -= 50
    else:
        zombie_x = random.randint(0, 1200)
        zombie_y = random.randint(0, 800)
        healz = 3
        expireance += 10

    if expireance >= 40:
        expireance = 0
        lvl += 1
    if event.type == pygame.MOUSEMOTION:
        screen.blit(aim, (event.pos[0], event.pos[1]))
        if event.pos[1] >= y and event.pos[1] > y + 100:
            screen.blit(player[1], (x, y))
        elif event.pos[1] <= y and event.pos[1] < y - 100:
            screen.blit(player[2], (x, y))
        elif event.pos[0] >= x:
            screen.blit(player[0], (x, y))
        elif event.pos[0] <= x:
            screen.blit(player[4], (x, y))
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
        if event.pos[0] in range(object_x[2] - 50, object_x[2] + 50) and event.pos[1] in range(object_y[2] - 50,
                                                                                               object_y[2] + 50):
            if doge_x  > x:
                hint = font.render(hints[0], True, (255, 255, 255))
            elif doge_x  < x:
                hint = font.render(hints[2], True, (255, 255, 255))
            elif doge_y  > y:
                hint = font.render(hints[3], True, (255, 255, 255))
            elif doge_y  < y:
                hint = font.render(hints[1], True, (255, 255, 255))
            screen.blit(hint, (600, 400))
        if event.pos[1] >= y and event.pos[0] in range(x - 75, x + 75):
            screen.blit(player[1], (x, y))
            object_y[0] -= speed
            doge_y -= speed
            object_y[2] -= speed
            object_y[3] -= speed
            object_y[4] -= speed
            object_y[5] -= speed
            zombie_y -= speed
            object_y[1] -= speed
            pos_y -= speed
        elif event.pos[1] <= y and event.pos[0] in range(x - 75, x + 75):
            screen.blit(player[2], (x, y))
            object_y[0] += speed
            doge_y += speed
            object_y[2] += speed
            object_y[3] += speed
            object_y[4] += speed
            object_y[5] += speed
            zombie_y += speed
            object_y[1] += speed
            pos_y +=speed
        elif event.pos[0] >= x and event.pos[1] in range(y - 75, y + 75):
            screen.blit(player[0], (x, y))
            object_x[0] -= speed
            doge_x -= speed
            object_x[2] -= speed
            object_x[3] -= speed
            object_x[4] -= speed
            object_x[5] -= speed
            zombie_x += speed
            object_x[1] -= speed
            pos_x-=speed
        elif event.pos[0] <= x and event.pos[1] in range(y - 75, y + 75):
            screen.blit(player[4], (x, y))
            object_x[0] += speed
            doge_x += speed
            object_x[2] += speed
            object_x[3] += speed
            object_x[4] += speed
            object_x[5] += speed
            zombie_x += speed
            object_x[1] += speed
            pos_x += speed
    if x in range(object_x[1] - 200, object_x[1] + 200) and y in range(object_y[1] - 200, object_y[1] + 200) and loot == True:
        food += 1
        loot = False
    screen.blit(interface, (1000, 500))
    pygame.draw.circle(screen, (255, 255, 0), (1093, 601), expireance, 0)
    health_text = font.render(str(math.trunc(health)), True, (255, 255, 255))
    food_text = font.render(str(food_level), True, (255, 255, 255))
    food_level_text = font.render(str(food), True, (255, 255, 255))
    screen.blit(health_text, (970, 640))
    screen.blit(food_text, (970, 670))
    health_bar = pygame.Rect(1040, 650, health, 20)
    pygame.draw.rect(screen, (255, 0, 0), health_bar, 0)
    screen.blit(doge, (doge_x, doge_y))
    screen.blit(loot_box, (object_x[1], object_y[1]))
    screen.blit(hint_tree, (object_x[2], object_y[2]))
    screen.blit(grass[grass_set[1]], (object_x[3], object_y[3]))
    screen.blit(food_level_text, (1070, 520))
    catridges_text = font.render(str(catridges), True, (255, 255, 255))
    screen.blit(catridges_text, (1030, 540))
    dialoges("черт,этот растяпа убежал.", tablet_sprites[0])
    if event.type == pygame.K_SPACE and food > 0:
        food -= 1
        food_level += 5
    if menu == "game0":
        screen.blit(menu_sprites[1], (500, 300))
        screen.blit(menu_sprites[2], (850, 300))
        screen.blit(menu_sprites[0], (200, 300))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[0] in range(500, 600) and event.pos[1] in range(300, 400):
                menu = "game1"
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[0] in range(850, 950) and event.pos[1] in range(300, 400):
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[0] in range(200, 300) and event.pos[1] in range(300, 400):
                menu = "settings"
                screen.fill((0, 0, 0))


    if object_x[0] > 1200:
        object_x[0] = -100
        object_y[0] = random.randint(0, 800)
    elif object_x[1] > 1200:
        object_x[1] = -100
        object_y[1] = random.randint(0, 800)
    elif object_x[2] > 1200:
        object_x[2] = -100
        object_y[2] = random.randint(0, 800)
    elif object_x[3] > 1200:
        object_x[3] = -100
        object_y[3] = random.randint(0, 800)
    elif object_x[4] > 1200:
        object_x[4] = -100
        object_y[4] = random.randint(0, 800)
    elif object_x[5] > 1200:
        object_x[5] = -100
        object_y[5] = random.randint(0, 800)
    if object_x[0] < 0:
        object_x[0] = -100
        object_y[0] = random.randint(0, 800)
    elif object_x[1] < 0:
        object_x[1] = 1300
        object_y[1] = random.randint(0, 800)
    elif object_x[2] < 0:
        object_x[2] = 1300
        object_y[2] = random.randint(0, 800)
    elif object_x[3] < 0:
        object_x[3] = 1300
        object_y[3] = random.randint(0, 800)
    elif object_x[4] < 0:
        object_x[4] = -100
        object_y[4] = random.randint(0, 800)
    elif object_x[5] < 0:
        object_x[5] = 1300
        object_y[5] = random.randint(0, 800)
    if object_y[0] > 800:
        object_y[0] = -100
        object_x[0] = random.randint(0, 1200)
    elif object_y[1] > 1200:
        object_y[2] = -100
        object_x[2] = random.randint(0, 1200)
    elif object_y[2] > 1200:
        object_y[2] = -100
        object_x[2] = random.randint(0, 1200)
    elif object_y[3] > 1200:
        object_y[3] = -100
        object_x[3] = random.randint(0, 1200)
    elif object_y[4] > 1200:
        object_y[4] = -100
        object_x[4] = random.randint(0, 1200)
    elif object_y[5] > 1200:
        object_y[5] = -100
        object_x[5] = random.randint(0, 1200)
    if object_y[0] < 0:
        object_y[0] = 900
        object_x[0] = random.randint(0, 1200)
    elif object_x[1] < 0:
        object_y[1] = 900
        object_x[1] = random.randint(0, 1200)
    elif object_x[2] < 0:
        object_y[2] = 900
        object_x[2] = random.randint(0, 1200)
    elif object_x[3] < 0:
        object_y[3] = 900
        object_x[3] = random.randint(0, 1200)
    elif object_x[4] < 0:
        object_y[4] = 900
        object_x[4] = random.randint(0, 1200)
    elif object_x[5] < 0:
        object_y[5] = 900
        object_x[5] = random.randint(0, 1200)
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if catridges > 0:
            if event.pos[0] + 50 in range(zombie_x, zombie_x + 85) and event.pos[1] + 50 in range(zombie_y,
                                                                                                  zombie_y + 85):
                healz -= 1
                catridges -= 1
        if event.pos[1] >= y and event.pos[1] > y + 100:
            screen.blit(player[6], (x, y))
        elif event.pos[1] <= y and event.pos[1] < y - 100:
            screen.blit(player[8], (x, y))
        elif event.pos[0] >= x:
            screen.blit(player[5], (x, y))
        elif event.pos[0] <= x:
            screen.blit(player[7], (x, y))
    if food_level <= 0:
        health -= 1
    if pos_y>=4200:
        screen.blit(map_end,(0,0))
    map=pygame.Rect(100,300,50,50)
    pygame.draw.rect(screen,(0,0,0),map,0)
    map_player = pygame.Rect(pos_x/5, pos_y/5, 3, 3)
    pygame.draw.rect(screen, (255, 255, 255), map_player, 0)
    map_doge = pygame.Rect(doge_x / 5, doge_y / 5, 3, 3)
    pygame.draw.rect(screen, (255, 0, 0), map_doge, 0)
    if x in range(doge_x-100,doge_x+100)  and y in range(doge_y-100,doge_y+100):
        menu="win_screen"
        screen.fill((0,0,0))
        screen.blit(win_screen,(300,100))
    pygame.display.flip()
