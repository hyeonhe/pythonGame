import pygame
import os
import random
from game import *

pygame.init()
# 화면 크기 설정
screen_width = 640  # 가로 크기
screen_height = 480  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Shooting Game")

# FPS
clock = pygame.time.Clock()
##############################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
current_path = os.path.dirname(__file__)  # 현재 파일의 위치 반환
image_path = os.path.join(current_path, "images")  # images 폴더 위치 반환

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.svg"))

# 스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.svg"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]  # 스테이지의 높이 위에 캐릭터를 두기 위해 사용

# 캐릭터 만들기


class Character(pygame.sprite.Sprite):
    def __init__(self, image):
        self.image = image
        self.size = image.get_rect().size
        self.width = self.size[0]
        self.height = self.size[1]
        self.x_pos = (screen_width - self.width) / 2
        self.y_pos = screen_height - self.height - stage_height
        self.to_x = 0  # 캐릭터 이동 방향
        self.speed = 5  # 캐릭터 이동 속도
        self.rect = self.image.get_rect()


character = Character(pygame.image.load(
    os.path.join(image_path, "character.svg")).convert_alpha())

# 무기 만들기


class Weapon(pygame.sprite.Sprite):
    def __init__(self, image):
        self.image = image
        self.size = self.image.get_rect().size
        self.width = self.size[0]
        self.speed = 10
        # 사라질 무기 변수
        self.to_remove = -1
        # 무기 위치 일단 안보이게
        self.x_pos = 640
        self.y_pos = 480


weapon = Weapon(pygame.image.load(os.path.join(
    image_path, "weapon.svg")).convert_alpha())

# 무기는 한 번에 여러 발 발사 가능
weapons = []


# # 사라질 무기, 공 정보 저장 변수
ball_to_remove = -1

# 공 만들기 (4개 크기에 대해 따로 처리)
ball_images = [
    pygame.image.load(os.path.join(
        image_path, "Ellipse 1.svg")).convert_alpha(),
    pygame.image.load(os.path.join(
        image_path, "Ellipse 2.svg")).convert_alpha(),
    pygame.image.load(os.path.join(
        image_path, "Ellipse 3.svg")).convert_alpha(),
    pygame.image.load(os.path.join(image_path, "Ellipse 4.svg")).convert_alpha()]

# 공 크기에 따른 최초 스피드
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


# Font 정의
game_font = pygame.font.SysFont("arial", 30)
total_time = 100
elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000  # ms -> s
start_ticks = pygame.time.get_ticks()  # 시작 시간 정의

# 게임 종료 메시지
# Time Over(시간 초과 실패)
# Mission Complete(성공)
# Game Over (캐릭터 공에 맞음, 실패)
game_result = "Game Over"

main = pygame.image.load(os.path.join(image_path, "main.svg"))
how = pygame.image.load(os.path.join(image_path, "howTo.svg"))

score_int = 0  # 실질적점수

# 음악
# 출처: https://freemusicarchive.org/home
pygame.mixer.music.load(os.path.join('Bio Unit - Orbit.mp3'))
# 출처: https://www.soundeffectsplus.com/product/balloon-explode-01/#google_vignette
ballon = pygame.mixer.Sound(os.path.join('ballon.mp3'))
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(loops=-1)
