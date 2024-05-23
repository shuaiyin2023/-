import pygame
import sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("植物大战僵尸")

""" 植物类 """


class Plants(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))  # 绿色
        self.rect = self.image.get_rect(center=pos)
        self.last_shot = pygame.time.get_ticks()
        self.shoot_delay = 1000  # 子弹发射间隔（毫秒）

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            bullet = Bullet(self.rect.center)
            all_sprites.add(bullet)
            bullets.add(bullet)


""" 向日葵类 """


class SunFlowers(Plants):

    def __init__(self, pos):
        super().__init__(pos)
        self.image = pygame.image.load('./images/sunflower.png')
        # 切分长图像成单独的帧
        self.frames = []
        # 定义每个小图的宽度和高度
        self.frame_width = 82
        self.frame_height = 77
        # 动态效果参数
        self.image_timer = 0  # 控制时间的初始值
        self.image_delay = 10  # 图像切换延迟
        self.current_frame = 0  # 当前图片

    # 图片的动态效果处理
    def deal_image(self):
        for image_width in range(0, self.image.get_width(), self.frame_width):
            for image_height in range(0, self.image.get_height(), self.frame_height):
                if self.image.get_width() - image_width < self.frame_width:  # 这个if语句用于判断原图的最后一个位置是否满足切割大小
                    break
                sub = self.image.subsurface(pygame.Rect(image_width, image_height, self.frame_width, self.frame_height))
                self.frames.append(sub)

    # 实现图片的动态效果
    def dynamic_effect(self):
        # 设置动态效果的时间频率
        self.image_timer += 1
        if self.image_timer >= self.image_delay:
            self.current_frame = (self.current_frame + 1) % len(self.frames)  # 无限轮播(如果第一遍轮播到最后一张图片，则继续从第一张开始轮播)
            self.image_timer = 0

        # 获取当前帧的小图
        self.image = self.frames[self.current_frame]

        # 在屏幕上绘制当前帧的小图
        screen.blit(self.image, self.rect)


""" 豌豆射手类 """


# class Peashooter(Plants)


""" 子弹类 """


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)  # 创建带有Alpha通道的表面对象
        pygame.draw.circle(self.image, (255, 123, 0), (10, 10), 10)  # 绘制红色圆形子弹
        self.rect = self.image.get_rect(center=pos)
        self.speed = 5

    def update(self):
        self.rect.x += self.speed
        if self.rect.bottom < 0:
            self.kill()


all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()

clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            # plant = Plant(event.pos)
            plant = SunFlowers(event.pos)
            plant.deal_image()  # 调用 deal_image() 方法来切分图像
            all_sprites.add(plant)
    for sprite in all_sprites:
        if isinstance(sprite, SunFlowers):
            sprite.dynamic_effect()
    all_sprites.update()

    for bullet in bullets:
        if bullet.rect.top <= 0:
            bullet.kill()

    screen.fill((0, 0, 0))
    all_sprites.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()
