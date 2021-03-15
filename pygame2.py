import pygame
from random import *
#############################################################################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init() # 초기화 반드시 필요

#화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 #세로 크기
screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Frog's First_Game") #게임 이름

#FPS
clock = pygame.time.Clock()
#############################################################################################################

#1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)
#배경화면
background = pygame.image.load("C:/Python/practice/Basic/PyGame_Quiz/background.png")
 
#캐릭터 이미지
character = pygame.image.load("C:\Python\practice\Basic\PyGame_Quiz\character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_X_pos = (screen_width / 2) - (character_width/2)
character_Y_pos = screen_height - character_height - 3

enemy = pygame.image.load("C:\Python\practice\Basic\PyGame_Quiz\enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_X_pos = randint(0,(screen_width - enemy_width))
enemy_Y_pos= 0

# 캐릭터의 속도
character_speed = 0.6
enemy_speed = 0.6
to_x=0
to_y=0


running = True
while running:
    dt = clock.tick(30) #게임 화면의 초당 프레임수를 설정

#캐릭터가 1초 100만큼 이동을 해야함
#10 fps : 1초 동안에 10번 동작 -> 1번 동작에 몇 만큼 이동? 10만큼! 10 * 10 = 100
#20 fps : 1초 동안에 20번 동작 -> 1번 동작에 5만큼! 5*20 = 100
    
    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get(): #어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였는가?
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                to_x = 0
    
    character_X_pos += to_x * dt
    enemy_Y_pos += enemy_speed *dt
    #3. 게임 캐릭터 위치 정의
    if character_X_pos < 0:
        character_X_pos = 0
    elif character_X_pos > (screen_width - character_width):
        character_X_pos =  (screen_width - character_width)
    if enemy_Y_pos > screen_height:
        enemy_Y_pos = 0
        enemy_X_pos = randint(0, screen_width - enemy_width)

    #4.충돌 처리


    character_rect = character.get_rect()
    character_rect.left = character_X_pos
    character_rect.top = character_Y_pos
    
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_X_pos
    enemy_rect.top = enemy_Y_pos

    
    # background_border = background.get_rect().size
    # background_rect_height =  background_border[1]
    # background_rect = background.get_rect()
    # background_rect.top = background_rect_height + enemy_height

    if character_rect.colliderect(enemy_rect):
        print("충돌을 감지했습니다.")
        running = False
    
    # if enemy_rect.colliderect(background_rect):
    #     enemy_Y_pos = 0
    #     enemy_X_pos = randint(0,(screen_width - enemy_width)+1)

    # 5. 화면에 그리기
    screen.blit(background,(0,0))
    screen.blit(character,(character_X_pos,character_Y_pos))
    screen.blit(enemy,(enemy_X_pos,enemy_Y_pos))
    pygame.display.update() # 게임 화면을 다시 그리기! 


# pygame 종료
pygame.quit()