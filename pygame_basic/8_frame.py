import pygame

###############1. 게임만들기 기본 깔고 갈 것#####################
pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Hawky G 1")
clock = pygame.time.Clock()
################################################################

######## 2. 기본 설정(배경, 게임 이미지, 좌표, 폰트, 속도 등)####


######### 3. 무조건 쓰는 부분 #################################
running = True
while running:
    dt = clock.tick(60)

    ######## 3.1 이벤트 처리#######################
 
 

    ######### 3.2 캐릭터 위치 정의 ##################    



    ######## 3.3 화면에 그리기 #############################
 
 
    
    ######### 3.4 화면 계속 업데이트 #####################
    pygame.display.update()

pygame.time.delay(2000)
pygame.quit()



        

            