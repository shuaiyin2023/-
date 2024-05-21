import pygame
import sys

# 初始化Pygame
pygame.init()

# 设置屏幕大小
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sprite Sheet Animation')

# 加载包含所有帧的长图像
sprite_sheet = pygame.image.load('./images/sunflower.png')  # 向日葵
# 切分长图像成单独的帧
frames = []
# 定义每个小图的宽度和高度
frame_width = 82
frame_height = 77

zombie = pygame.image.load('./images/zombie.png')  # 僵尸
Peashooter = pygame.image.load('./images/Peashooter.png')  # 豌豆射手

# 调整图像大小
Peashooter = pygame.transform.scale(Peashooter, (frame_width, frame_height))


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

sunflowers = []  # 定义一个向日葵列表
peashooter_list = []  # 定义一个豌豆射手列表
zombie_list = []  # 定义一个僵尸列表


def update_sunflowers():
    """
    判断种植的植物是否超过屏幕范围
    :return:
    """
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
            if event.button == 1:
                sunflowers.append([position_x, position_y])
            if event.button == 3:
                peashooter_list.append([position_x, position_y])

    print(sunflowers)
    print("豌豆射手： ", peashooter_list)
    # 设置动态效果的时间频率
    image_timer += 1
    if image_timer >= image_delay:
        current_frame = (current_frame + 1) % len(frames)  # 无限轮播(如果第一遍轮播到最后一张图片，则继续从第一张开始轮播)
        image_timer = 0

    # 绘制图片
    screen.fill((0, 0, 0))
    for flower in sunflowers:
        screen.blit(frames[current_frame], (flower[0], flower[1]))  # 当用户点击鼠标，就种植向日葵
    for peashooter in peashooter_list:
        screen.blit(Peashooter, (peashooter[0], peashooter[1]))  # 当用户点击鼠标，就种植向日葵
    pygame.display.flip()


