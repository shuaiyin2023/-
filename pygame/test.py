# import pygame
# import sys
#
# # 初始化Pygame
# pygame.init()
#
# # 设置屏幕大小
# WIDTH, HEIGHT = 800, 600
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption('Animated Image')
#
# # 加载动态图像
# images = [pygame.image.load('./images/map1.png'), pygame.image.load('./images/map2.png'), pygame.image.load('./images/僵尸.png')]
# current_image = 0
# image_timer = 0
# image_delay = 50  # 图像切换延迟
#
# # 主循环
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#
#     # 切换图像
#     image_timer += 1
#     if image_timer >= image_delay:
#         current_image = (current_image + 1) % len(images)
#         image_timer = 0
#
#     # 绘制屏幕
#     screen.fill((0, 0, 0))
#     screen.blit(images[current_image], (0, 0))
#
#     pygame.display.flip()


import pygame
import sys

# 初始化Pygame
pygame.init()

# 设置屏幕大小
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sprite Sheet Animation')

# 加载包含所有帧的长图像
sprite_sheet = pygame.image.load('./images/sunflower.png')

# 切分长图像成单独的帧
frames = []

# 定义每个小图的宽度和高度
frame_width = 82
frame_height = 77

for x in range(0, sprite_sheet.get_width(), frame_width):
    for y in range(0, sprite_sheet.get_height(), frame_height):
        if sprite_sheet.get_width() - x < frame_width:  # 这个if语句用于判断原图的最后一个位置是否满足切割大小
            break
        sub = sprite_sheet.subsurface(pygame.Rect(x, y, frame_width, frame_height))
        frames.append(sub)


image_timer = 0
image_delay = 150  # 图像切换延迟
current_frame = 0  # 当前图片

position_x = position_y = 0
# 定义一个向日葵列表
sunflowers = []


# 如果种植超过范围，则种植无效
def update_sunflowers():
    global sunflowers
    for _flower in sunflowers:
        if _flower[0] >= screen.get_width() or _flower[1] >= screen.get_height():
            sunflowers.remove(_flower)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            position_x, position_y = pygame.mouse.get_pos()
            sunflowers.append([position_x, position_y])

    print(sunflowers)
    # 设置动态效果的时间频率
    image_timer += 1
    if image_timer >= image_delay:
        current_frame = (current_frame + 1) % len(frames)  # 无限轮播(如果第一遍轮播到最后一张图片，则继续从第一张开始轮播)
        image_timer = 0

    # 绘制图片
    screen.fill((0, 0, 0))
    for flower in sunflowers:
        screen.blit(frames[current_frame], (flower[0], flower[1]))  # 当用户点击鼠标，就种植向日葵
    pygame.display.flip()


