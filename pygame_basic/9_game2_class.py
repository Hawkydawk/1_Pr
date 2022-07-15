from asyncio.windows_events import NULL
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
background = pygame.image.load("E:/Study/Python/1_Pr/pygame_basic/background.png")
character = pygame.image.load("E:/Study/Python/1_Pr/pygame_basic/horsepig_1.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width/2
character_y_pos = screen_height - character_height
enemies = []

to_x = 0
to_y = 0
character_speed = 0.6
game_font = pygame.font.Font(None, 40)
total_time = 10
start_Time = pygame.time.get_ticks()
spawn_Time = 0

enemyLink1 = "E:/Study/Python/1_Pr/pygame_basic/monster_rocky_1.png"
enemyLink2 = "E:/Study/Python/1_Pr/pygame_basic/monster_zombie_1.png"

class Enemy:
    enemyLink = ""
    # 계속 시간을 체크할 수 있는 방법 필요
    spawn_Time = pygame.time.get_ticks()
    def enemy_Spawn():
        if int(spawn_Time%1000) == 0 and int(spawn_Time%2000) != 0:
            enemyLink = enemyLink1
        elif int(spawn_Time%1000) == 0 and int(spawn_Time()%2000) == 0:
            enemyLink = enemyLink2
        if enemyLink != "":
            enemy = pygame.image.load(enemyLink)
            enemy_size = enemy.get_rect().size
            enemy_width = enemy.size[0]
            enemy_height = enemy.size[1]
            enemy_x_pos = random.randrange(0, (640-enemy_width))
            enemy_y_pos = 0
        else:
            pass

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

    mob = Enemy.enemy_Spawn()
    if mob.enemy_Spawn() != NULL:
        enemies.append(mob)
    for mob_pop in enemies:
        if mob_pop.enemy_y_pos < screen_height:
            mob_pop.enemy_y_pos += 5

    ######## 3.3 화면에 그리기 #############################
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    for mob_pop in enemies:
        screen.blit(mob_pop, (mob_pop.enemy_x_pos, mob_pop.enemy_y_pos))
    
    ######### 3.4 화면 계속 업데이트 #####################
    pygame.display.update()

pygame.time.delay(2000)
pygame.quit()
