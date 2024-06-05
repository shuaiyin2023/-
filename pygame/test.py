# # import pygame
# # from pygame.locals import *
# #
# # pygame.init()
# # screen = pygame.display.set_mode((600, 500))
# # pygame.display.set_caption("pygame")
# # font = pygame.font.SysFont("kaiti", 24)
# #
# # figure = pygame.Rect(20, 20, 100, 100)
# # pygame.draw.rect(screen, (0, 214, 222), figure)
# # left_boundary = figure.x + figure.width
# # top_boundary = figure.y + figure.height
# #
# # figure_2 = pygame.Rect(left_boundary + 50, 20, 100, 100)
# # pygame.draw.rect(screen, (0, 10, 150), figure_2)
# # left_boundary_2 = figure_2.x + figure_2.width
# # top_boundary_2 = figure_2.y + figure_2.height
# #
# # figure_count = figure_2_count = 0
# #
# # # figure_list = []
# # # figure_list.append(
# # #     {"figure": figure, "left_boundary": figure.x + figure.width, "top_boundary": figure.y + figure.height, "count": 0})
# # # figure_list.append(
# # #     {"figure": figure_2, "left_boundary": figure_2.x + figure_2.width, "top_boundary": figure_2.y + figure_2.height,
# # #      "count": 0})
# #
# #
# # # def draw_figure(figure_obj, count, left_border, top_border, pos_x, pos_y):
# # #     if figure_obj.collidepoint(pos_x, pos_y):
# # #         count += 1
# # #         text = font.render(str(count), True, "green")
# # #     else:
# # #         text = font.render(str(count), True, "green")
# # #
# # #     screen.blit(text, (figure_obj.x + ((left_border - figure_obj.x) // 2), top_border + 20))
# # #
# # #     return text
# #
# #
# # clock = pygame.time.Clock()
# #
# # str1 = ""
# # while True:
# #
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             pygame.quit()
# #         if event.type == pygame.KEYDOWN:
# #             str1 += str(event.unicode)
# #         if event.type == MOUSEBUTTONDOWN:
# #             print("鼠标事件: ", event.pos)
# #             screen.fill((0, 0, 0))
# #             pygame.draw.rect(screen, (0, 214, 222), figure)
# #             pygame.draw.rect(screen, (0, 10, 150), figure_2)
# #             x, y = event.pos
# #
# #             # for figure_obj in figure_list:
# #             #     draw_figure(figure_obj["figure"], figure_obj["count"], figure_obj["left_boundary"],
# #             #                 figure_obj["top_boundary"], x, y)
# #             if figure.collidepoint(x, y):
# #                 figure_count += 1
# #                 current_text = font.render(str(figure_count), True, "green")
# #             else:
# #                 current_text = font.render(str(figure_count), True, "green")
# #
# #             if figure_2.collidepoint(x, y):
# #                 figure_2_count += 1
# #                 current_text_2 = font.render(str(figure_2_count), True, "green")
# #             else:
# #                 current_text_2 = font.render(str(figure_2_count), True, "green")
# #
# #             screen.blit(current_text, (figure.x + ((left_boundary - figure.x) // 2), top_boundary + 20))
# #             screen.blit(current_text_2, (figure_2.x + ((left_boundary_2 - figure_2.x) // 2), top_boundary_2 + 20))
# #
# #             # if current_index < len(text_list):
# #             #     current_text = font.render(text_list[current_index], True, "green")
# #             #     screen.blit(current_text, (left, top))
# #             #     top += 30
# #             #     current_index += 1
# #             # else:
# #             #     current_index = 0
# #             #     screen.fill((0, 0, 0))
# #             #     top = 20
# #
# #     pygame.display.update()
#
#
#
#
#
import pygame
import sys

# 初始化Pygame
pygame.init()

# 设置窗口大小和格子大小
cell_row_count = 8
window_size = (800, 400)
cell_size = window_size[0] // cell_row_count

# 颜色定义
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# 定义格子类
class GridCell:
    def __init__(self):
        self.plant = None


# 创建游戏窗口
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("植物大战僵尸")
# 游戏背景
background = pygame.image.load("./images/grassland.png").convert()

image = pygame.image.load('./images/Peashooter.png').convert_alpha()
image = pygame.transform.scale(image, (cell_size, cell_size))

# 创建一个10x10的格子
grid_row_size = window_size[1] // cell_size
grid_column_size = 8
grid = [[GridCell() for _ in range(grid_row_size)] for _ in range(grid_column_size)]
print("grid: ", grid)


""" 植物类 """


class Plants(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        # self.image.fill((0, 255, 0))  # 绿色
        self.rect = self.image.get_rect(center=pos)
        self.last_shot = pygame.time.get_ticks()
        self.shoot_delay = 1000  # 子弹发射间隔（毫秒）
        self.base_damage = 20  # 初始伤害


""" 向日葵类 """


class SunFlowers(Plants):

    def __init__(self, pos):
        super().__init__(pos)
        self.image = pygame.image.load('./images/sunflower.png').convert_alpha()
        # 切分长图像成单独的帧
        self.frames = []
        # 定义每个小图的宽度和高度
        self.frame_width = 82
        self.frame_height = 77
        # 动态效果参数
        self.image_timer = 0  # 控制时间的初始值
        self.image_delay = 10  # 图像切换延迟
        self.current_frame = 0  # 当前图片

    # 图片的切割处理
    def deal_image(self):
        for image_width in range(0, self.image.get_width(), self.frame_width):
            for image_height in range(0, self.image.get_height(), self.frame_height):
                if self.image.get_width() - image_width < self.frame_width:  # 这个if语句用于判断原图的最后一个位置是否满足切割大小
                    break
                sub = self.image.subsurface(pygame.Rect(image_width, image_height, self.frame_width, self.frame_height))
                self.frames.append(sub)

    # 轮播图片
    def dynamic_effect(self):
        # 设置动态效果的时间频率
        self.image_timer += 1
        if self.image_timer >= self.image_delay:
            self.current_frame = (self.current_frame + 1) % len(self.frames)  # 无限轮播(如果第一遍轮播到最后一张图片，则继续从第一张开始轮播)
            self.image_timer = 0

        # 获取当前帧的小图
        self.image = self.frames[self.current_frame]

        # 在屏幕上绘制当前帧的小图
        window.blit(self.image, self.rect)

    # def update(self):
    #     pass

sunflower = SunFlowers

# 游戏主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # 左键点击
                x, y = event.pos
                print(x, y)
                cell_x = x // cell_size
                cell_y = y // cell_size
                print(cell_x)
                print(cell_y)

                if grid[cell_x][cell_y].plant is None:  # 检查格子是否为空
                    new_plant = SunFlowers(event.pos)
                    grid[cell_x][cell_y].plant = new_plant

    # window.blit(background, (0, 0))
    window.fill(WHITE)

    # 绘制格子和植物
    # window.fill(WHITE)
    # 绘制草坪方格和分割线
    for x in range(0, window_size[0], cell_size):
        pygame.draw.line(window, GREEN, (x, 0), (x, window_size[1]))  # 绘制垂直分割线
    for y in range(0, window_size[1], cell_size):
        pygame.draw.line(window, GREEN, (0, y), (window_size[0], y))  # 绘制水平分割线
    for x in range(grid_column_size):
        for y in range(grid_row_size):
            # rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
            # pygame.draw.rect(window, GREEN if grid[x][y].plant else WHITE, rect)
            if grid[x][y].plant:
                window.blit(image, (x * cell_size, y * cell_size))
                grid[x][y].plant.deal_image()
                grid[x][y].plant.dynamic_effect()

    pygame.display.flip()

