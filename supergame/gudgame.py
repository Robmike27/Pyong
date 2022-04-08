import pygame, sys, random

clock = pygame.time.Clock()

from pygame.locals import *
pygame.init() #starts pygame

pygame.display.set_caption('Supagame')

WINDOW_SIZE = (480,340)

screen = pygame.display.set_mode(WINDOW_SIZE,0,32) #initiate the window

moving_up = False
moving_down = False

moving_2_up = False
moving_2_down = False

player_1_location = [50,170]
player_2_location = [430,170]

player_1_rect = pygame.Rect(player_1_location[0], player_1_location[1], 25, 50)
player_2_rect = pygame.Rect(player_2_location[0], player_2_location[1], 25, 50)

player_1_pad = pygame.Rect(player_1_location[0] + 13, player_1_location[1], 2, 50)
player_2_pad = pygame.Rect(player_2_location[0] - 13, player_2_location[1], 2, 50)

ball_position = [240,170]
ball_rect = pygame.Rect(ball_position[0],ball_position[1],20,20)

ball_y_momentum = -.5
ball_x_momentum = -1

redWin_image = pygame.image.load("./supergame/red_wins.png",)
bluWin_image = pygame.image.load("./supergame/blue_wins.png",)

while True: #game loop
    screen.fill((0,0,0))

    player_1_rect.y = player_1_location[1]
    player_2_rect.y = player_2_location[1]

    
    player_1_top_pad = pygame.Rect(player_1_location[0], player_1_location[1] - 3, 30, 5)
    player_1_bottom_pad = pygame.Rect(player_1_location[0], player_1_location[1] + 50, 30, 5)
    player_1_front_pad = pygame.Rect(player_1_location[0] + 21, player_1_location[1] + 5, 1, 40)

    player_2_top_pad = pygame.Rect(player_2_location[0], player_2_location[1] - 3, 30, 5)
    player_2_bottom_pad = pygame.Rect(player_2_location[0], player_2_location[1] + 50, 30, 5)
    player_2_front_pad = pygame.Rect(player_2_location[0] - 2, player_2_location[1], 1, 50)

    #draw player 1
    pygame.draw.rect(screen,(25,200,0), player_2_top_pad)
    pygame.draw.rect(screen,(200,0,0), player_2_bottom_pad)
    pygame.draw.rect(screen,(255,0,0), player_1_rect)
    pygame.draw.rect(screen,(255,50,50), player_2_front_pad)

    #draw player 2
    pygame.draw.rect(screen,(0,0,255), player_2_rect)
    
    #player 1 and 2 paddle hit.
    
    if (player_1_top_pad.colliderect(ball_rect) or player_2_top_pad.colliderect(ball_rect)) and (ball_y_momentum > 0):
        ball_position[1] -= 1
        ball_y_momentum = ball_y_momentum * -1
    
    if player_1_bottom_pad.colliderect(ball_rect) or player_2_bottom_pad.colliderect(ball_rect):
        ball_position[1] += 1
        ball_y_momentum = ball_y_momentum * -1
    
    if player_1_front_pad.colliderect(ball_rect):
            pygame.draw.rect(screen,(0,255,0),ball_rect)
            ball_position[0] += 3
            ball_x_momentum = ball_x_momentum * -1.01
            ball_y_momentum = ball_y_momentum * 1.01

    if player_2_front_pad.colliderect(ball_rect):
            pygame.draw.rect(screen,(0,255,0),ball_rect)
            ball_position[0] -= 3
            ball_x_momentum = ball_x_momentum * -1.01
            ball_y_momentum = ball_y_momentum * 1.01


    #moves player 1 paddle
    if moving_up == True:
        player_1_location[1] -= 5
    if moving_down == True:
        player_1_location[1] += 5
    if int(player_1_location[1]) + 50 > int(WINDOW_SIZE[1]):
        moving_down = False
    if player_1_location[1] < 0:
        moving_up = False

    #moves player 2 paddle
    if moving_2_up == True:
        player_2_location[1] -= 5
    if moving_2_down == True:
        player_2_location[1] += 5
    if int(player_2_location[1]) + 50 > int(WINDOW_SIZE[1]):
        moving_2_down = False
    if player_2_location[1] < 0:
        moving_2_up = False

    #WIN screen
    if ball_position[0] < 0:
        screen.blit(bluWin_image,[240,170])
    
    if ball_position[0] > WINDOW_SIZE[0]:
        screen.blit(redWin_image,[120,170])

    #ball wall bounce
    if ball_position[1] < 0:
        ball_y_momentum = ball_y_momentum * -1
    
    if ball_position[1] > int(WINDOW_SIZE[1])-20:
        ball_y_momentum = ball_y_momentum * -1
    
    if ball_x_momentum > 10:
        ball_x_momentum = 10
    
    if ball_y_momentum > 10:
        ball_y_momentum = 10
        

    pygame.draw.rect(screen,(255,255,255),ball_rect)
    ball_position[0] += ball_x_momentum
    ball_rect.x = ball_position[0]
    ball_position[1] += ball_y_momentum
    ball_rect.y = ball_position[1]

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        #player 1 movement
        if event.type == KEYDOWN:
            if event.key == K_w:
                moving_up = True
            if event.key == K_s:
                moving_down = True
            
        if event.type == KEYUP:
            if event.key == K_w:
                moving_up = False
            if event.key == K_s:
                moving_down = False
        
        #player 2 movement
        if event.type == KEYDOWN:
            if event.key == K_UP:
                moving_2_up = True
            if event.key == K_DOWN:
                moving_2_down = True
        if event.type == KEYUP:
            if event.key == K_UP:
                moving_2_up = False
            if event.key == K_DOWN:
                moving_2_down = False

    
    pygame.display.update()
    clock.tick(120)