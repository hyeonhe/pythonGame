import pygame
import random
import os
from info1 import *


class Coin(pygame.sprite.Sprite):
    def __init__(self, image):
        self.image = image
        self.size = self.image.get_rect().size
        self.width = self.size[0]
        self.height = self.size[1]
        self.speed = 10
        self.x_pos = random.randint(0, screen_width - self.width)
        self.y_pos = 0
        self.rect = self.image.get_rect()


coin = Coin(pygame.image.load(os.path.join(
    image_path, "coin.svg")).convert_alpha())
