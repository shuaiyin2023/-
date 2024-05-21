import os.path

import pygame

pygame.init()

# 创建游戏窗口
width, height = 1000, 600
screen = pygame.display.set_mode(size=(width, height), flags=pygame.RESIZABLE)
pygame.display.set_caption("植物大战僵尸")

# 处理背景
background = pygame.Surface(screen.get_size())
background = background.convert()  # convert(): 将Surface对象转换为单个像素的格式
background.fill((255, 255, 255))

image_path = "D:/Company-yin/DjangoProjects/djangoProject/myself_file/pygame/images/"

""" 创建图片加载函数 """


def image_load(name):
    # 加载图片
    file_path = os.path.join(image_path, name)
    image = pygame.image.load(file_path)
    image = image.convert_alpha()

    return image


""" 创建地图类 """


class Map:
    def __init__(self):
        pass


""" 创建植物类 """


class Plants(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()


""" 向日葵类 """


class SunFlowers(Plants):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./images/sunflower.png')
        # 切分长图像成单独的帧
        self.frames = []
        # 定义每个小图的宽度和高度
        self.frame_width = 82
        self.frame_height = 77
        # 动态效果参数
        self.image_timer = 0  # 控制时间的初始值
        self.image_delay = 150  # 图像切换延迟
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

        # 绘制图片
        screen.fill((0, 0, 0))
        screen.blit(self.frames[self.current_frame], (0, 100))
        pygame.display.flip()


""" 子弹类 """


class Bullet(pygame.sprite.Sprite):
    click = False

    def __init__(self):
        super().__init__()

    # 子弹移动
    def move(self, speed):
        global position_x, position_y
        screen.fill((0, 0, 0))
        position_x += speed
        # position_y += speed
        pygame.draw.circle(screen, pink, (int(position_x), int(position_y)), 20)


click = False
white = (255, 255, 255)
blue = (0, 0, 255)
pink = (255, 192, 203)
position_x = position_y = x = y = 0
speed = 5


def game_running():
    global click
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            ''' 鼠标事件 '''
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = not click
                    position_x, position_y = event.pos
                    pygame.draw.circle(screen, pink, (int(position_x), int(position_y)), 20)
        if click:
            Bullet.move(speed)
        screen.blit(background, (0, 0))
        background.blit(image_load("sunflower.png"), (0, 200))
        pygame.display.flip()


if __name__ == "__main__":
    # game_running()
    flower_obj = SunFlowers()
    flower_obj.deal_image()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        flower_obj.dynamic_effect()



