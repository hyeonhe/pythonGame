from info import *
from main import *
import pygame


def game():
    running = True
    dt = clock.tick(30)
    while running:

        # 2. 이벤트 처리 (키보드, 마우스 등)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:  # 캐릭터를 왼쪽으로
                    character_to_x -= character_speed
                elif event.key == pygame.K_RIGHT:  # 캐릭터를 오른쪽으로
                    character_to_x += character_speed
                elif event.key == pygame.K_SPACE:  # 무기 발사
                    weapon_x_pos = character_x_pos + \
                        (character_width / 2) - (weapon_width / 2)
                    weapon_y_pos = character_y_pos
                    weapons.append([weapon_x_pos, weapon_y_pos])

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    character_to_x = 0

        # 3. 게임 캐릭터 위치 정의
        character_x_pos += character_to_x

        if character_x_pos < 0:
            character_x_pos = 0
        elif character_x_pos > screen_width - character_width:
            character_x_pos = screen_width - character_width

        # 무기 위치 조정
        # 100, 200 -> 180, 160, 140, ...
        # 500, 200 -> 180, 160, 140, ...
        weapons = [[w[0], w[1] - weapon_speed] for w in weapons]  # 무기 위치를 위로

        # 천장에 닿은 무기 없애기
        weapons = [[w[0], w[1]] for w in weapons if w[1] > 0]

        # 공 위치 정의
        for ball_idx, ball_val in enumerate(balls):
            ball_pos_x = ball_val["pos_x"]
            ball_pos_y = ball_val["pos_y"]
            ball_img_idx = ball_val["img_idx"]

            ball_size = ball_images[ball_img_idx].get_rect().size
            ball_width = ball_size[0]
            ball_height = ball_size[1]

            # 가로벽에 닿았을 때 공 이동 위치 변경 (튕겨 나오는 효과)
            if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
                ball_val["to_x"] = ball_val["to_x"] * -1

            # 세로 위치
            # 스테이지에 튕겨서 올라가는 처리
            if ball_pos_y >= screen_height - stage_height - ball_height:
                ball_val["to_y"] = ball_val["init_spd_y"]
            else:  # 그 외의 모든 경우에는 속도를 증가
                ball_val["to_y"] += 0.5

            ball_val["pos_x"] += ball_val["to_x"]
            ball_val["pos_y"] += ball_val["to_y"]

        # 4. 충돌 처리

        # 캐릭터 rect 정보 업데이트
        character_rect = character.get_rect()
        character_rect.left = character_x_pos
        character_rect.top = character_y_pos

        for ball_idx, ball_val in enumerate(balls):
            ball_pos_x = ball_val["pos_x"]
            ball_pos_y = ball_val["pos_y"]
            ball_img_idx = ball_val["img_idx"]

            # 공 rect 정보 업데이트
            ball_rect = ball_images[ball_img_idx].get_rect()
            ball_rect.left = ball_pos_x
            ball_rect.top = ball_pos_y

            # 공과 캐릭터 충돌 체크
            if character_rect.colliderect(ball_rect):
                running = False
                break

            # 공과 무기들 충돌 처리
            for weapon_idx, weapon_val in enumerate(weapons):
                weapon_pos_x = weapon_val[0]
                weapon_pos_y = weapon_val[1]

                # 무기 rect 정보 업데이트
                weapon_rect = weapon.get_rect()
                weapon_rect.left = weapon_pos_x
                weapon_rect.top = weapon_pos_y

                # 충돌 체크
                if weapon_rect.colliderect(ball_rect):
                    weapon_to_remove = weapon_idx  # 해당 무기 없애기 위한 값 설정
                    ball_to_remove = ball_idx  # 해당 공 없애기 위한 값 설정

                    # 가장 작은 크기의 공이 아니라면 다음 단계의 공으로 나눠주기
                    if ball_img_idx < 3:
                        # 현재 공 크기 정보를 가지고 옴
                        ball_width = ball_rect.size[0]
                        ball_height = ball_rect.size[1]

                        # 나눠진 공 정보
                        small_ball_rect = ball_images[ball_img_idx + 1].get_rect()
                        small_ball_width = small_ball_rect.size[0]
                        small_ball_height = small_ball_rect.size[1]

                        # 왼쪽으로 튕겨나가는 작은 공
                        balls.append({
                            # 공의 x 좌표
                            "pos_x": ball_pos_x + (ball_width / 2) - (small_ball_width / 2),
                            # 공의 y 좌표
                            "pos_y": ball_pos_y + (ball_height / 2) - (small_ball_height / 2),
                            "img_idx": ball_img_idx + 1,  # 공의 이미지 인덱스
                            "to_x": -3,  # x축 이동방향, -3 이면 왼쪽으로, 3 이면 오른쪽으로
                            "to_y": -6,  # y축 이동방향,
                            "init_spd_y": ball_speed_y[ball_img_idx + 1]})  # y 최초 속도

                        # 오른쪽으로 튕겨나가는 작은 공
                        balls.append({
                            # 공의 x 좌표
                            "pos_x": ball_pos_x + (ball_width / 2) - (small_ball_width / 2),
                            # 공의 y 좌표
                            "pos_y": ball_pos_y + (ball_height / 2) - (small_ball_height / 2),
                            "img_idx": ball_img_idx + 1,  # 공의 이미지 인덱스
                            "to_x": 3,  # x축 이동방향, -3 이면 왼쪽으로, 3 이면 오른쪽으로
                            "to_y": -6,  # y축 이동방향,
                            "init_spd_y": ball_speed_y[ball_img_idx + 1]})  # y 최초 속도
                    if ball_img_idx == 0:
                        score_int += 10
                    elif ball_img_idx == 1:
                        score_int += 20
                    elif ball_img_idx == 2:
                        score_int += 40
                    elif ball_img_idx == 3:
                        score_int += 80
                    break
            else:  # 계속 게임을 진행
                continue  # 안쪽 for 문 조건이 맞지 않으면 continue. 바깥 for 문 계속 수행
            break  # 안쪽 for 문에서 break 를 만나면 여기로 진입 가능. 2중 for 문을 한번에 탈출

        # for 바깥조건:
        #     바깥동작
        #     for 안쪽조건:
        #         안쪽동작
        #         if 충돌하면:
        #             break
        #     else:
        #         continue
        #     break

        # 충돌된 공 or 무기 없애기
        if ball_to_remove > -1:
            del balls[ball_to_remove]
            ball_to_remove = -1

        if weapon_to_remove > -1:
            del weapons[weapon_to_remove]
            weapon_to_remove = -1

        # 모든 공을 없앤 경우 게임 종료 (성공)
        if len(balls) == 0:
            game_result = "Mission Complete"
            running = False

        # 5. 화면에 그리기
        screen.blit(background, (0, 0))

        for weapon_x_pos, weapon_y_pos in weapons:
            screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

        for idx, val in enumerate(balls):
            ball_pos_x = val["pos_x"]
            ball_pos_y = val["pos_y"]
            ball_img_idx = val["img_idx"]
            screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))

        screen.blit(stage, (0, screen_height - stage_height))
        screen.blit(character, (character_x_pos, character_y_pos))

        # 경과 시간 계산
        elapsed_time = (pygame.time.get_ticks() -
                        start_ticks) / 1000  # ms -> s
        timer = game_font.render("Time : {}".format(
            int(total_time - elapsed_time)), True, (255, 255, 255))
        score = game_font.render("Score : {}".format(
            int(score_int)), True, (255, 255, 255))
        screen.blit(timer, (10, 10))
        screen.blit(score, (10, 50))

        # 시간 초과했다면
        if total_time - elapsed_time <= 0:
            game_result = "Time Over"
            running = False

        pygame.display.update()
