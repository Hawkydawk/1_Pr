import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Hawky Game 1")

#배경 불러오기
background = pygame.image.load("E:\\4_Study\\Python\\1_Pr\\pygame_basic\\background.png")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0)) #배경표시좌표(0, 0) == 좌측 상단
    # screen.fill((0, 0, 255)) #배경을 그림 말고 RGB 값으로 채움
    pygame.display.update() #배경을 계속 띄우기

pygame.quit()
