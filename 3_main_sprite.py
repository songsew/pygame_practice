import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width,screen_height))



# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") 

# 배경 이미지 불러오기
background = pygame.image.load('/Users/swsong/Jupyter/pygame_basic/logo.png')

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load('/Users/swsong/Jupyter/pygame_basic/charactor.png')
character_size = character.get_rect().size # 이미지 크기를 구해옴
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width - character_width)/ 2 
character_y_pos = screen_height - character_height


# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 계속 발생
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생
            running = False # 게임이 진행중이 아닙니다.d
    #screen.blit(background, (0, 0)) # 배경 그리기
    screen.fill((0, 0, 255))
    screen.blit(character, (character_x_pos,character_y_pos))
    pygame.display.update() # 화면 다시 그리기(반복)
# pygame 종료
pygame.quit()