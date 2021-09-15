#Collision condition of ball and slit made efficient
import random
import math
import pygame
pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
exit_game = False
screen_width = 900
screen_height = 600
# x=48
# y=88
x = screen_width/2
y = screen_height/2
velocity_x = 0
# velocity_y=0
velocity_y = 5
slit_x = x
slit_y = screen_height-90
slit_x_v = 0
slit_y_v = 0
fps = 30
slit_width = x
slit_height = screen_height-90

pygame.display.set_caption("Bouncing Ball")

gameWindow = pygame.display.set_mode((screen_width, screen_height))
# bg_img = pygame.image.load("bg_img1.jpg")
# bg_img = pygame.transform.scale(
    # bg_img, (screen_width, screen_height)).convert_alpha()
font = pygame.font.SysFont(None, 55)
clock = pygame.time.Clock()
lst1 = [5, -5]
lst2 = [5, 5, -5]


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


# increased ball size, more responsive game
# cir = pygame.draw.circle(gameWindow, black, (x, y), 20, 24)
# rect = pygame.draw.rect(gameWindow, black, [slit_x, slit_y, 88, 28])
ball = pygame.image.load("ball1.jpg")
# just create rectangle of image, and work like rectangle figure with it
ballrect = ball.get_rect()    #rectangle around ball created
bat = pygame.image.load("bat1.jpg")
batrect = bat.get_rect()




while not exit_game:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            exit_game = True
            break
        elif(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_q):
                exit_game = True
                break
            if(event.key == pygame.K_LEFT):
                slit_x_v = -5
            if(event.key == pygame.K_RIGHT):
                slit_x_v = 5
    text_screen("High Score: "+str(5), red, 500, 50)

    # point = pygame.mouse.get_pos()
    #Collision condition of ball and slit made efficient
    # point = (x, y)  # coordinates of ball
    # Boolean variable handling collision or not
    # collide = batrect.collidepoint(point)
    collide=False
    if(slit_x-x<30 and slit_y-y<=30):
        collide=True
    # print(point,collide)
    # Hower on rectangle to change color, initially black
    color = (255, 0, 0) if collide else (0, 0, 0)
    #Left wall
    if(x <= 0 and y <= screen_height):
        velocity_x = 7
        # velocity_y = 5
        # lst2 to make +5 more biased, ball come back to bottom
        velocity_y += random.choice(lst2)
    #Top wall
    if(x <= screen_width and y <= 0):
        velocity_x = 7
        velocity_y = 4
    #If in almost middle of top,then go down
    if(((x >= int(screen_width/2)-20) and x <= int(screen_width/2)+20) and (y <= 0)):
        velocity_y = 5
        velocity_x = 0
    #Right wall
    if(x >= screen_width-90 and y <= screen_height):
        velocity_x = -5
        velocity_y = 7
    # if(x>=screen_width and y>=screen_height/2):
        # velocity_x=-5
        # velocity_y=5
    if(collide):  # due to this rectangle is drawn outside the game loop
        temp = random.choice(lst1)
        velocity_x += temp
        # velocity_y+=-6
        velocity_y += -8
    #Condition: if ball touch bottom wall, then exit game
    elif(y >= screen_height):
        # exit_game = True
        # break
        velocity_x += random.choice(lst1)
        velocity_y = -7

    x += velocity_x
    y += velocity_y
    if(slit_x>screen_width-90):
        slit_x_v=-5
    elif(slit_x<5):
        slit_x_v=5
    
    slit_x += slit_x_v
    # print(slit_x,slit_y, x,y)
    gameWindow.fill(white)
    # gameWindow.blit(bg_img, (0, 0))

    # pygame.draw.circle(gameWindow, black, (x, y), 20, 18)
    # pygame.draw.rect(gameWindow, black, [slit_x, slit_y, 88, 28])
    # rect = pygame.draw.rect(gameWindow, color, [slit_x, slit_y, 88, 28])
    # gameWindow.blit(ball, ballrect)
    gameWindow.blit(ball, (x, y))
    # gameWindow.blit(bat, batrect)  # while running press key, ball coming from bat
    gameWindow.blit(bat,(slit_x,slit_y))

    pygame.display.update()
    clock.tick(fps)
pygame.quit()
quit()
