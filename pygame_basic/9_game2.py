import time
import pygame
import random

###############1. 게임만들기 기본 깔고 갈 것#####################
pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Hawky G 1")
clock = pygame.time.Clock()
################################################################

######## 2. 기본 설정(배경, 게임 이미지, 좌표, 폰트, 속도 등)####
background = pygame.image.load("E:/4_Study/Python/1_Pr/pygame_basic/background.png")
character = pygame.image.load("E:/4_Study/Python/1_Pr/pygame_basic/horsepig_1.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_height - character_height

to_x = 0
character_speed = 0.5
start_time = pygame.time.get_ticks()

enemy_Link = "E:/4_Study/Python/1_Pr/pygame_basic/monster_zombie_1.png"

enemy = pygame.image.load(enemy_Link)
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randrange(0, (screen_width-enemy_width))
enemy_y_pos = 0
enemy_speed = 10

pop_Link = "E:/4_Study/Python/1_Pr/pygame_basic/pop_1.png"
pop = pygame.image.load(pop_Link)
pop_size = pop.get_rect().size
pop_width = pop_size[0]
pop_height = pop_size[1]
pop_x_pos = 0
pop_y_pos = 0

game_font = pygame.font.Font(None, 40)

total_time = 60
start_ticks = pygame.time.get_ticks()
score = 0

######### 3. 무조건 쓰는 부분 #################################
running = True
while running:
    dt = clock.tick(60)

    ######## 3.1 이벤트 처리#######################
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
        
    ######### 3.2 캐릭터 위치 정의 ##################    
    character_x_pos += to_x * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - (character_width):
        character_x_pos = screen_width - (character_width)

    if enemy_y_pos < screen_height:
        enemy_y_pos += enemy_speed    
    else:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0, screen_width - enemy_width)

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    ###### Collide ##################################
    # 개선하자: 폭발 이미지가 0.5초 남아있다 사라지게
    if character_rect.colliderect(enemy_rect):
        print("Got ya!")
        score += 1            # Score
        pop_x_pos = enemy_x_pos
        pop_y_pos = enemy_y_pos
        enemy_y_pos = -enemy_height
        enemy_x_pos = random.randint(0, screen_width - enemy_width)

    ####### Scoreboard ###################################
    scoreboard = game_font.render(str(score), True, (243, 196, 25))

    ####### Timer ####################################
    time_passed = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render(str(int(total_time - time_passed)), True, (243, 196, 25))
    if total_time - time_passed < 0:
        print("Time's up.")
        running = False

    ######## 3.3 화면에 그리기 #############################
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    screen.blit(timer, (10, 10))
    screen.blit(scoreboard, (420, 10))
    screen.blit(pop, (pop_x_pos, pop_y_pos))
  
    ######### 3.4 화면 계속 업데이트 #####################
    pygame.display.update()

pygame.time.delay(2000)
pygame.quit()
