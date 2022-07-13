import random
import pygame
from sys import exit
import time

pygame.init()

clock = pygame.time.Clock()

WIDTH, HEIGHT = 1280, 960
screen = pygame.display.set_mode((WIDTH, HEIGHT))

main = True

pygame.display.set_caption('Pong')

back_surf = pygame.image.load('black.jpg').convert_alpha()

x1, x2 = 20, 1240

y1, y2 = 400, 400

bx, by = 640, 450

going_left = True
going_right = False
ball_dir = random.randint(0, 1)
speed = 5

ls, rs = 0, 0

pixfont = pygame.font.Font('Pixeltype.ttf', 50)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(back_surf, (0,0))
    if main:
        # pongs
        left_pong = pygame.draw.rect(screen, (255, 255, 255), (x1, y1, 20, 70))
        right_pong = pygame.draw.rect(screen, (255, 255, 255), (x2, y2, 20, 70))

        #ball
        ball = pygame.draw.circle(screen, (255, 255, 255), (bx, by), 7, 12)


        ls_surface = pixfont.render(str(ls), False, 'White')
        ls_rect = ls_surface.get_rect(center = (20, 30))

        rs_surface = pixfont.render(str(rs), False, 'White')
        rs_rect = rs_surface.get_rect(center = (1260, 30))

        screen.blit(ls_surface, ls_rect)
        screen.blit(rs_surface, rs_rect)


        # key press if statement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            y1 -= 10
        if keys[pygame.K_s]:
            y1 += 10
        if keys[pygame.K_UP]:
            y2 -= 10
        if keys[pygame.K_DOWN]:
            y2 += 10


        # RETURN TO
        # --------------------------------
        # if ball_dir == 0:
        #     by += random.randint(1, 10)
        # else:
        #     by -= random.randint(1, 10)

        if going_left:
            bx -= speed
            if ball_dir == 0:
                by += random.randint(1, 5)
            else:
                by -= random.randint(1, 5)

        if going_right:
            bx += speed
            if ball_dir == 0:
                by += random.randint(1, 5)
            else:
                by -= random.randint(1, 5)

        if by <= 0:
            by = 1
            ball_dir = 0
        if by >= 960:
            by = 959
            ball_dir = 1

        if left_pong.colliderect(ball):
            going_left = False
            speed += .5
            going_right = True


        if right_pong.colliderect(ball):
            going_right = False
            speed += .05
            going_left = True

        if y1 <= 0: y1 = 0
        if y2 <= 0: y2 = 0
        if y1 >= 890: y1 = 890
        if y2 >= 890: y2 = 890


        if bx <= -20:
            speed = 5
            rs += 1
            pygame.display.update()
            bx, by = 640, 450
            going_left = False
            going_right = True
        if bx >= 1300:
            speed = 5
            ls += 1
            pygame.display.update()
            bx, by = 640, 450
            going_right = False
            going_left = True


    pygame.display.update()
    clock.tick(60)