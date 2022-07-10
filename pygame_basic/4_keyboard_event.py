import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Hawky Game 1")

background = pygame.image.load("E:/4_Study/Python/1_Pr/pygame_basic/background.png")
character = pygame.image.load("E:/4_Study/Python/1_Pr/pygame_basic/horsepig_1.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2
character_y_pos = screen_height

#이동 좌표
to_x = 0
to_y = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN: #키 누르면
            if event.key == pygame.K_LEFT:
                to_x -= 5
            elif event.key == pygame.K_RIGHT:
                to_x += 5
            elif event.key == pygame.K_UP:
                to_y -= 5
            elif event.key == pygame.K_DOWN:
                to_y += 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: #더 이상 좌우로 안 움직이면
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN: #위 아래로 더 안 움직이면
                to_y = 0

    character_x_pos += to_x            
    character_y_pos += to_y

    if character_x_pos < 0 + (character_width/2):
        character_x_pos = 0 + (character_width/2)
    elif character_x_pos > (screen_width - character_width/2):
        character_x_pos = screen_width - character_width/2
    elif character_y_pos < 0 + character_height:
        character_y_pos = 0 + character_height
    elif character_y_pos > screen_height:
        character_y_pos = screen_height
    
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos-(character_width/2), character_y_pos-character_height))

    pygame.display.update()

pygame.quit()