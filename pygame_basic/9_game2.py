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
character_x_pos = screen_width/2
character_y_pos = screen_height - character_height

to_x = 0
to_y = 0
character_speed = 0.6

enemy1 = pygame.image.load("E:/4_Study/Python/1_Pr/pygame_basic/monster_zombie_1.png")
enemy1_size = enemy1.get_rect().size
enemy1_width = enemy1_size[0]
enemy1_height = enemy1_size[1]
enemy1_x_pos = random.randrange(0, 640-(enemy1_width))
enemy1_y_pos = 0

enemy2 = pygame.image.load("E:/4_Study/Python/1_Pr/pygame_basic/monster_rocky_1.png")
enemy2_size = enemy2.get_rect().size
enemy2_width = enemy2_size[0]
enemy2_height = enemy2_size[1]
enemy2_x_pos = random.randrange(0, 640-(enemy2_width))
enemy2_y_pos = 0

game_font = pygame.font.Font(None, 40)
total_time = 10
start_ticks = pygame.time.get_ticks()

######### 3. 무조건 쓰는 부분 #################################
running = True
while running:
    dt = clock.tick(60)

    ######## 3.1 이벤트 처리#######################
    #monsters falling
    #key action
    #collision action
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
    elif character_x_pos > (screen_width - character_width/2):
        character_x_pos = screen_width - character_width/2

    ######## 3.3 화면에 그리기 #############################
    screen.blit(background, (0, 0))
    screen.blit(character, character_x_pos)
    screen.blit(enemy1, (100, 100))
    screen.blit(enemy2, (200, 200))
    
    ######### 3.4 화면 계속 업데이트 #####################
    pygame.display.update()

pygame.time.delay(2000)
pygame.quit()
