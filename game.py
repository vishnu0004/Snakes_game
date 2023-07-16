import pygame
import random
import os 
pygame.init()

#colors
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
blue = (25, 72,233)
marun = (128, 0, 0)
green = (22,214,102)

screen_with = 900
screen_height = 600

#Creating Windows
gamewindow = pygame.display.set_mode((screen_with,screen_height))

#game title
pygame.display.set_caption("My First Game !")
pygame.display.update()


def text_screen(text,color,x,y):
    screen_text = font.render(text,True,color)
    gamewindow.blit(screen_text, [x,y])

def plot_snake(gamewindow,color,snk_list,snake_size):
     for x,y in snk_list :
        pygame.draw.rect(gamewindow,color,[x,y,snake_size,snake_size])

font = pygame.font.SysFont(None,55)

def welcom():
    exit_game = False
    while not exit_game:
        gamewindow.fill(green)
        text_screen("Welcom to Snakes!",black,276,240)
        text_screen("Press Space Bar to Play",black,232,290)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()

        pygame.display.update()
        
#Creating a game loop 
def gameloop():
       #Game Specific Variables
    exit_game = False 
    game_over = False
    velocity_x = 0
    velocity_y = 0
    snake_x = 45
    snake_y = 55
    snake_size = 15
    fps = 50
    score = 0
    init_velocity = 5
    snk_list = []
    snk_length = 1

    #chack if hiscore file exists
    if(not os.path.exists("hiscore.txt")):
        with open("hiscore.txt","w") as f:
            f.write("0")
    with open("hiscore.txt","r") as f :
        hiscore = f.read()

    food_x = random.randint(20,screen_with/2)
    food_y = random.randint(20,screen_height/2)
    clock = pygame.time.Clock()
    
    while not exit_game:
        if game_over: 
            with open("hiscore.txt","w") as f :
                f.write(str(hiscore)) 
            gamewindow.fill(green) 
            text_screen("Game Over! Press Enter To Continue",red,100,250)
            text_screen("Your Score =" + str(score),red,290,190,)

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = 5
                        velocity_y = 0 

                    if event.key == pygame.K_LEFT:
                        velocity_x = -5
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - 5
                        velocity_x = 0
            
                    if event.key == pygame.K_DOWN:
                        velocity_y = + 5
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y  

            if abs(snake_x - food_x)<11 and abs(snake_y - food_y)<11:
                score +=10
            
                
                food_x = random.randint(20,screen_with/2)
                food_y = random.randint(20,screen_height/2)
                snk_length +=5

                if score>int(hiscore):
                    hiscore = score

            gamewindow.fill(white)
            text_screen("Score: " + str(score) +"  Hiscore: "+ str(hiscore),blue ,250,5)
            pygame.draw.rect(gamewindow,red,[food_x,food_y,snake_size,snake_size])

            head =[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0] 

            if head in snk_list[:-1]:
                game_over = True

            if snake_x<0 or snake_x>screen_with or snake_y<0 or snake_y>screen_height:
                game_over = True
            plot_snake(gamewindow,black,snk_list,snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

welcom()