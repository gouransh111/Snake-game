import os
import pygame
import random
import time
pygame.init()
#background

#colors
blue = (255,62,150)
yellow = (255,185,15)
green = (69,139,116)
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
screen_width = 800
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("SNAke game")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 50)
font2 = pygame.font.SysFont(None, 20)
bg = pygame.image.load('E:/Snake game/gallery/sprites/snk.jpg')
bg = pygame.transform.scale(bg,(screen_width,screen_height)).convert_alpha()
def desksc(text,color,x,y):
      screen_text = font.render(text,True,color)
      gameWindow.blit(screen_text,[x,y])

     
def plot(gameWindow,color,snk_list,snake_size):
      for x,y in snk_list: 
            #if x,y == snk_list[0][0],snk_list[0][1]:
            pygame.draw.rect(gameWindow , red, [x,y, snake_size,snake_size])
            #else:
              # pygame.draw.rect(gameWindow , black, [x,y, snake_size,snake_size])
def welcome():
      exit_game = False       
      while not exit_game: 
        gameWindow.fill(green)
        desksc("Welcome to the snake game",black,100,100)
        desksc("Press enter to continue",black,100,150)

         
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                 gameloop()
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                  exit_game = True
        pygame.display.update()
        clock.tick(30)
      pygame.quit
      quit()
def pause():
      exit_game = False
      while not exit_game:
            gameWindow.fill(white)
            desksc("Game paused",red,200,300)
            desksc("Press space to continue",red,190,340)
            for event in pygame.event.get():
                  if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        return None    
def gameloop():
     pygame.mixer.init()
     pygame.mixer.music.load('E:\Snake game\gallery\music\ply.mp3')
     pygame.mixer.music.play() 
     fps = 30
     velocity_x = 0
     velocity_y = 0
     exit_game = False
     game_over =  False
     snake_x = 70
     snake_y = 55
     snake_size = 10
     food_x = random.randint(21,screen_width)
     food_y = random.randint(20,screen_height)
     snk_list = []
     snk_len = 1
     if(not os.path.exists("high.txt")):
        with open("high.txt","w") as f:
             f.write("0")
     with open("high.txt","r") as f:
         highscore =  f.read()
      
     score = 10    
     while not exit_game:
           
 
          if game_over:
                with open("high.txt","w") as f:
                    f.write(str(highscore))
                gameWindow.fill(white)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                       game_over = False
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                         welcome()
                desksc("Game over press enter to  continue",black,20,20)
                if game_over == False:
                   pygame.quit
                   quit()
          else:
                
                for event in pygame.event.get():
                  if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                      exit_game = True
                  if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        pause()

                  if event.type == pygame.KEYDOWN:
                      if event.key == pygame.K_RIGHT:
                         velocity_x = 4
                         velocity_y = 0
                  if event.type == pygame.KEYDOWN:
                      if event.key == pygame.K_LEFT:
                          velocity_x = -4
                          velocity_y = 0

                  if event.type == pygame.KEYDOWN:
                      if event.key == pygame.K_UP:
                         velocity_y = -4
                         velocity_x = 0

                  if event.type == pygame.KEYDOWN:
                      if event.key == pygame.K_DOWN:
                          velocity_y = 4
                          velocity_x = 0
                snake_x = snake_x + velocity_x       
                if abs(snake_x - food_x)<6 and abs(snake_y -food_y)<6:
                     score += 10
                     
                     food_x = random.randint(21,screen_width/2)
                     food_y = random.randint(20,screen_height/2)
                     snk_len += 5
                     if score>int(highscore):
                           highscore = score

                     
                snake_y = snake_y + velocity_y
                gameWindow.fill(white)
                screen_text2 = font.render("Food is in pink colour",True,black)
                gameWindow.blit(screen_text2,[10,780])
                gameWindow.blit(bg,(0,0))
                desksc("SCORE:"+ str(score) + " Highscore:" + str(highscore) ,(blue),5,5)


                pygame.draw.rect(gameWindow , black, [food_x,food_y, snake_size,snake_size])
                pygame.draw.rect(gameWindow , red, [snake_x,snake_y, snake_size,snake_size])
                head =[]
                head.append(snake_x)
                head.append(snake_y)
                snk_list.append(head)

                if len(snk_list)>snk_len:
                      del snk_list[0]

                if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                      game_over = True
                      pygame.mixer.music.load('E:\Snake game\gallery\music\Beeper_Emergency_Call.mp3')
                        
                      pygame.mixer.music.play()
                      time.sleep(2)
                if head in snk_list[:-1]:
                      game_over = True
                      pygame.mixer.music.load('E:\Snake game\gallery\music\Beeper_Emergency_Call.mp3')
                      pygame.mixer.music.play()
                      time.sleep(2)
          #if snake_x == screen_width or snake_y == screen_height:
                #exit_game = True
                plot(gameWindow,red,snk_list,snake_size)
          pygame.display.update()
          clock.tick(fps)

     pygame.quit()
     quit()
welcome()
gameloop()






