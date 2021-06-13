from info import *
from game import *
import pygame


def mainn():
    main_run = True
    while main_run:
        clock.tick(30)
        main_x = 0   # 메인화면 그릴 x좌표
        main_y = 0   # 메인화면 그릴 y좌표
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return pygame.quit

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mouse.get_rel()
                mouse_pos = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONUP:
                if 430 <= mouse_pos[0] <= 581:
                    if 249 <= mouse_pos[1] <= 305:
                        main_x = 640
                        main_y = 480
                        screen.blit(main, (main_x, main_y))
                        pygame.display.update()
                        return game()

        screen.blit(main, (main_x, main_y))
        pygame.display.update()
