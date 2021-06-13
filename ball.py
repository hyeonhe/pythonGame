from info import *
# 공 만들기 (4개 크기에 대해 따로 처리)


class Ball():
    def __init__(self, image):
        self.image = image


ball_images = [
    pygame.image.load(os.path.join(
        image_path, "Ellipse 1.svg")).convert_alpha(),
    pygame.image.load(os.path.join(
        image_path, "Ellipse 2.svg")).convert_alpha(),
    pygame.image.load(os.path.join(
        image_path, "Ellipse 3.svg")).convert_alpha(),
    pygame.image.load(os.path.join(image_path, "Ellipse 4.svg")).convert_alpha()]


# class Ball(pygame.sprite.Sprite):
#     def __init__(self, balls):
#         for ball_idx, ball_val in enumerate(balls):
#             # self.image = image
#             # self.speed_y = speed_y
#             self.pos_x = ball_val["pos_x"]
#             self.pos_y = ball_val["pos_y"]
#             self.img_idx = ball_val["img_idx"]

#             self.size = ball_images[self.img_idx].get_rect().size
#             self.width = self.size[0]
#             self.height = self.size[1]

#             # if self.pos_x < 0 or self.pos_x > screen_width - self.width:
#             #     ball_val["to_x"] = ball_val["to_x"] * -1

#             # if self.pos_y >= screen_height - stage_height - self.height:
#             #     ball_val["to_y"] = ball_val["init_spd_y"]
#             # else:
#             #     ball_val["to_y"] += 0.5

#             # ball_val["pos_x"] += ball_val["to_x"]
#             # ball_val["pos_y"] += ball_val["to_y"]


# weapon.mask = pygame.mask.from_surface(weapon.image)


# # 공 크기에 따른 최초 스피드
ball_speed_y = [-18, -15, -12, -9]  # index 0, 1, 2, 3 에 해당하는 값

# 공들
balls = []

# 최초 발생하는 큰 공 추가
balls.append({
    "pos_x": 50,  # 공의 x 좌표
    "pos_y": 50,  # 공의 y 좌표
    "img_idx": 0,  # 공의 이미지 인덱스
    "to_x": 3,  # x축 이동방향, -3 이면 왼쪽으로, 3 이면 오른쪽으로
    "to_y": -6,  # y축 이동방향,
    "init_spd_y": ball_speed_y[0]})  # y 최초 속도

print(balls)
