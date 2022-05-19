import pygame
import sys
import random
import time

pygame.init()
x = 600
y = 400
zombie_x = random.randint(0, 1200)
zombie_y = random.randint(0, 800)
hint_tree = pygame.image.load("hint_tree.png")
hints = ["собака была правее", "собака расположена выше", "собака левее", "собака ушла немного ниже",
         "новый лутбокс правее", "новый лутбокс левее", "новый лутбокс выше", "новый лутбокс ниже"]
a = 0
screen = pygame.display.set_mode((1200, 800))
player = [pygame.image.load("player_right (2).png"), pygame.image.load("player_down (2).png"),
          pygame.image.load("player_up (2).png"), pygame.image.load("player_left (2).png"),
          pygame.image.load("player_left (2).png"), pygame.image.load("player_right_shoot.png"),
          pygame.image.load("player_down_shoot.png"), pygame.image.load("player_left_shoot.png"),
          pygame.image.load("player_up_shoot.png")]
grass = [pygame.image.load("grass1.png"), pygame.image.load("grass2.png"), pygame.image.load("grass3.png"), ]
menu = "game0"
grass_set = [random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), ]
language = "русский"
menu_sprites = [pygame.image.load("start.png")]
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
health_bar = pygame.Rect(0, 0, health, 50)
dialoge = True
doge_x = 1
doge_y = 1


def dialoges(text, sprite):
    if event.type != pygame.KEYDOWN and dialoge == True:
        pygame.draw.rect(screen, (0, 0, 0), r, 0)
        tablet = font.render(text, True, (255, 255, 255))
        screen.blit(tablet, (200, 600))
        screen.blit(sprite, (0, 300))


while True:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if menu == "game0":
            screen.blit(menu_sprites[0], (500, 300))
            screen.blit(menu_sprites[0], (850, 300))
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
            health_text = font.render(str(health), True, (255, 255, 255))
            screen.blit(health_text, (0, 100))
            pygame.draw.rect(screen, (255, 0, 0), health_bar, 0)
            while doge_x % 10 != 0:
                doge_x = random.randint(0, 1200)
            while doge_y % 10 != 0:
                doge_y = random.randint(0, 800)
            if event.type == pygame.MOUSEMOTION:
                screen.fill((60, 179, 113))
                if event.pos[1] >= y and event.pos[1] > y + 100:
                    screen.blit(player[1], (x, y))
                elif event.pos[1] <= y and event.pos[1] < y - 100:
                    screen.blit(player[2], (x, y))
                elif event.pos[0] >= x:
                    screen.blit(player[0], (x, y))
                elif event.pos[0] <= x:
                    screen.blit(player[4], (x, y))
                if event.type == pygame.K_SPACE:
                    screen.fill((60, 179, 113))
                    if event.pos[1] >= y and event.pos[0] in range(x - 75, x + 75):
                        screen.blit(player[6], (x, y))
                        object_y[0] -= 10
                    elif event.pos[1] <= y and event.pos[0] in range(x - 75, x + 75):
                        screen.blit(player[8], (x, y))
                        object_y[0] += 10
                    elif event.pos[0] >= x and event.pos[1] in range(y - 75, y + 75):
                        screen.blit(player[5], (x, y))
                        object_x[0] -= 10
                    elif event.pos[0] <= x and event.pos[1] in range(y - 75, y + 75):
                        screen.blit(player[7], (x, y))
                        object_x[0] += 10
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                screen.fill((60, 179, 113))
                if event.pos[0] in range(object_x[2]-200,object_x[2]+200) and event.pos[1] in range(object_x[2]-200,object_x[2]+200):
                    if doge_x > x:
                        hint_text = font.render(hints[0], True, (255, 255, 255))
                    elif doge_x < x:
                        hint_text = font.render(hints[2], True, (255, 255, 255))
                    elif doge_y < y:
                        hint_text = font.render(hints[1], True, (255, 255, 255))
                    elif doge_y > y:
                        hint_text = font.render(hints[3], True, (255, 255, 255))
                    screen.blit(hint_text, (600, 400))
                elif event.pos[1] >= y and event.pos[0] in range(x - 75, x + 75):
                    screen.blit(player[1], (x, y))
                    object_y[0] -= 10
                    doge_y -= 10
                    object_y[2] -= 10
                    object_y[3] -= 10
                    object_y[4] -= 10
                    object_y[5] -= 10
                    zombie_y -= 10
                elif event.pos[1] <= y and event.pos[0] in range(x - 75, x + 75):
                    screen.blit(player[2], (x, y))
                    object_y[0] += 10
                    doge_y += 10
                    object_y[2] += 10
                    object_y[3] += 10
                    object_y[4] += 10
                    object_y[5] += 10
                    zombie_y += 10
                elif event.pos[0] >= x and event.pos[1] in range(y - 75, y + 75):
                    screen.blit(player[0], (x, y))
                    object_x[0] -= 10
                    doge_x -= 10
                    object_x[2] -= 10
                    object_x[3] -= 10
                    object_x[4] -= 10
                    object_x[5] -= 10
                    zombie_x += 10
                elif event.pos[0] <= x and event.pos[1] in range(y - 75, y + 75):
                    screen.blit(player[4], (x, y))
                    object_x[0] += 10
                    doge_x += 10
                    object_x[2] += 10
                    object_x[3] += 10
                    object_x[4] += 10
                    object_x[5] += 10
                    zombie_x += 10
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pygame.draw.line(screen, (255, 215, 0), (x+42, y+42), (event.pos[0], event.pos[1]), 5)
        if event.type == pygame.KEYDOWN:
            dialoge = False
        dialoges("черт,этот растяпа убежал.", tablet_sprites[0])
        screen.blit(doge, (doge_x, doge_y))
        screen.blit(grass[grass_set[1]], (object_x[1], object_y[1]))
        screen.blit(hint_tree, (object_x[2], object_y[2]))
        screen.blit(grass[grass_set[1]], (object_x[3], object_y[3]))
    if x > zombie_x:

        screen.blit(zombies_sprites[0], (zombie_x, zombie_y))
        zombie_x += 1
        if zombie_x == x:
            health -= 1
            zombie_x -= 50
    if x < zombie_x:
        screen.blit(zombies_sprites[1], (zombie_x, zombie_y))
        zombie_x -= 1
        if zombie_x == x:
            health -= 1
            zombie_x += 50
    if y < zombie_y:
        screen.blit(zombies_sprites[2], (zombie_x, zombie_y))
        zombie_y -= 1
        if zombie_y == y:
            health -= 1
            zombie_y += 50
    if y > zombie_y:
        screen.blit(zombies_sprites[3], (zombie_x, zombie_y))
        zombie_y += 1
        if zombie_y == y:
            health -= 1
            zombie_y -= 50
    if x == doge_x and y == doge_y:
        pygame.quit()
        sys.exit()
    pygame.display.flip()
