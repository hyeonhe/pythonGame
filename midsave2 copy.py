from info import *
from main import *
from game import *
import pygame

##############################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init()

whole = True
while whole:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            whole = False
    mainn

    pygame.display.update()
pygame.init()


# if quitbool == True:
# 게임 오버 메시지
# msg = game_font.render(game_result, True, (255, 255, 0))  # 노란색
# msg_rect = msg.get_rect(
#     center=(int(screen_width / 2), int(screen_height / 2)))
# screen.blit(msg, msg_rect)
# pygame.display.update()

# # 2초 대기
pygame.time.delay(2000)

# # pygame.quit()

# pygame.quit()
