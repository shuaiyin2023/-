import pygame
import random
import sys
import time

# 初始化pygame
pygame.init()

# 设置颜色
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 设置屏幕大小
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

flower = pygame.image.load("./images/sunflower.png")
print("向日葵的高: ", flower.get_height(), flower.get_width())



