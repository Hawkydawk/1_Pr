import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Hawky Game 1")
clock = pygame.time.Clock()

background = pygame.image.load("E:/4_Study/Python/1_Pr/pygame_basic/background.png")
character = pygame.image.load("E:/4_Study/Python/1_Pr/pygame_basic/horsepig_1.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width/2
character_y_pos = screen_height

to_x = 0
to_y = 0
character_speed = 0.6

enemy = pygame.image.load("E:/4_Study/Python/1_Pr/pygame_basic/monster_zombie_1.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width / 2) - (enemy_width / 2)
enemy_y_pos = (screen_height / 2) - (enemy_height / 2)

# 폰트 정의
game_font = pygame.font.Font(None, 40) #폰트 객체 생성(폰트, 크기)

# 총 시간
total_time = 10

# 시작 시간
start_ticks = pygame.time.get_ticks() #시작 tick 정보 받아오기

running = True
while running:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    if character_x_pos < 0 + (character_width/2):
        character_x_pos = 0 + (character_width/2)
    elif character_x_pos > (screen_width - character_width/2):
        character_x_pos = screen_width - character_width/2
    elif character_y_pos < 0 + character_height:
        character_y_pos = 0 + character_height
    elif character_y_pos > screen_height:
        character_y_pos = screen_height

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print("Craaash!")
        running = False
    
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos - (character_width/2), character_y_pos - character_height))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    # 타이머 넣기
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 #초 단위 표시(/1000)
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (243, 196, 25)) #카운트 다운 (출력할 글자, antialias, 글자색)
    screen.blit(timer, (10, 10))
    if total_time - elapsed_time < 0: #타임아웃
        print("Time's Up")
        running = False

    pygame.display.update()

# 종료 전 2초 대기
pygame.time.delay(2000)
pygame.quit()