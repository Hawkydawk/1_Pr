import pygame

pygame.init() #초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Hawky Game 1") #게임명

# 이벤트 루프 (화면 안 꺼지게 하며 사용자 입력값 받기)
running = True
while running:
    for event in pygame.event.get(): #어떤 이벤트가 발생했나?
        if event.type == pygame.QUIT: #창이 꺼짐?
            running = False
# 게임 종료
pygame.quit()