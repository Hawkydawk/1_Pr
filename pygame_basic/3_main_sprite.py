import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Hawky Game 1")

background = pygame.image.load("E:/4_Study/Python/1_Pr/pygame_basic/background.png")

# 스프라이트 불러오기
character = pygame.image.load("E:/4_Study/Python/1_Pr/pygame_basic/horsepig_1.png")
character_size = character.get_rect().size #이미지 크기 불러오기
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 #화면 가로 중앙
character_y_pos = screen_height #화면 가장 아래

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos-(character_width/2), character_y_pos-(character_height)))
    pygame.display.update()


pygame.quit()