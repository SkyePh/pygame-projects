import pygame
import time
import sys
import random

pygame.init() #initialize pygame

pygame.mixer.init()

pygame.font.init() #initialize the fonts

#creating the window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake")

font_style = pygame.font.SysFont(None, 30) #making our font style
score_font = pygame.font.SysFont(None, 45)
gameover_font = pygame.font.SysFont(None, 45)
start_font = pygame.font.SysFont(None, 45)

clock = pygame.time.Clock() #making clock speed

#assign color variables
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0 ,0)

#starting screen
def startscreen():
    starttext = start_font.render("Welcome to Snake! Space- Play, Esc- Quit", True, white)
    screen.blit(starttext, [width / 8, height / 3])

#game over screen
def gameover():
    gameover_text = gameover_font.render("Game Over! Space- Play Again, Esc- Quit", True, red)
    screen.blit(gameover_text, [width / 8, height / 3])

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                mainloop()
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()                

#score drawing
def your_score(score):
    value = score_font.render("Score: " + str(score), True, white)
    screen.blit(value, [0, 0])
    pygame.display.flip()

#main loop
def mainloop():

    game = True

    eat_sound = pygame.mixer.Sound('C:\\Users\\mario\\OneDrive\\Desktop\\Coding\\Snake\\Rizz effect.mp3')

    #var for snake
    xchange = 0
    ychange = 0

    #assigning variables
    snake_size = 10
    snake_speed = 15

    x1 = width / 2
    y1 = height / 2

    #snake size increasing using a list
    snake_list = []
    snake_length = 1

    #randomly generates coords for food
    xfood = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
    yfood = round(random.randrange(0, height - snake_size) / 10.0) * 10.0

    while game:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #assinging controls
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    if xchange>0 or xchange<0:
                        xchange = xchange
                        ychange = 0   
                    else:
                        xchange -= snake_size 
                        ychange = 0   
                elif event.key == pygame.K_d:
                    if xchange<0 or xchange>0:
                        xchange = xchange
                        ychange = 0   
                    else:
                        xchange += snake_size
                        ychange = 0
                elif event.key == pygame.K_w:
                    if ychange>0 or ychange<0:
                        xchange = 0
                        ychange = ychange  
                    else:
                        xchange = 0
                        ychange -= snake_size
                elif event.key == pygame.K_s:
                    if ychange<0 or ychange>0:
                        xchange = 0
                        ychange = ychange
                    else:
                        xchange = 0
                        ychange += snake_size      
        
        #snake moves
        x1 += xchange
        y1 += ychange

        screen.fill(black)

        if snake_length > 1:
            if snake_head in snake_list[:-1]:
                game = False

        #assigning the head to be part of the snake
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        pygame.draw.rect(screen, red, [xfood, yfood, snake_size, snake_size])

        if (x1 >= width or x1<= 0) or (y1>= height or y1<= 0):
            game = False

        if (x1 == xfood and y1 == yfood):
            eat_sound.play()
            snake_length += 1 
            xfood = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
            yfood = round(random.randrange(0, height - snake_size) / 10.0) * 10.0 

        if len(snake_list) > snake_length:
            del snake_list[0]       

        for x in snake_list:
            pygame.draw.rect(screen, green, [x[0], x[1], snake_size, snake_size]) 

        your_score(snake_length - 1)         

        pygame.display.flip()
        clock.tick(snake_speed)

#Starting screen display
start = True
while start:
    waiting_for_key = True

    while waiting_for_key:
        screen.fill(black)
        startscreen()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting_for_key = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()  
    
    start = False    

mainloop()                          

screen.fill(black)
pygame.display.flip()

#Game Over screen display
gameoverbool = True
while gameoverbool:
    screen.fill(black)
    gameover()
    pygame.display.flip()

pygame.quit()
quit()


