import pygame
import sys

# 初始化Pygame
pygame.init()

# 设置屏幕大小
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sprite Sheet Animation')

# 加载包含所有帧的长图像
sprite_sheet = pygame.image.load('./images/sunflower.png').convert_alpha()  # 向日葵
# 切分长图像成单独的帧
frames = []
# 定义每个小图的宽度和高度
frame_width = 82
frame_height = 77

zombie = pygame.image.load('./images/zombie.png').convert_alpha()  # 僵尸
Peashooter = pygame.image.load('./images/Peashooter.png').convert_alpha()  # 豌豆射手

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


def generate_zombie():
    """
    此函数用于自动生成僵尸
    :return:
    """
    global zombie_list


# 子弹的移动速度
speed = 0.3
bullets = []  # 创建一个子弹列表
speeds = []  # 每颗子弹单独存放
white = (255, 255, 255)
blue = (0, 0, 255)
pink = (255, 192, 203)


def bullet_update():
    """
    此函数用于更新子弹移动轨迹
    :return:
    """

    global bullets, speed, WIDTH

    for i, bullet in enumerate(bullets):
        bullet[0] += speeds[i]  # 假设子弹向右移动
        # 检查子弹是否超出屏幕边界
        if bullet[0] < 0 or bullet[0] > WIDTH:
            # 子弹触碰到左右边界时，反转水平速度方向
            # bullet[0] = max(0, min(bullet[0], WIDTH))  # 限制子弹在屏幕范围内
            # speeds[i] = -speeds[i]  # 反向移动
            bullets.remove(bullet)  # 子弹触碰到边框则消失
            speeds.remove(speeds[i])



def bullet_draw():
    """
    此函数用于生成子弹
    :return:
    """
    global bullets
    for bullet in bullets:
        pygame.draw.circle(screen, pink, (int(bullet[0]), int(bullet[1])), 10)


alive = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            position_x, position_y = pygame.mouse.get_pos()
            if event.button == 1:
                sunflowers.append([True, position_x, position_y])  # 向日葵
                bullets.append([position_x, position_y])  # 子弹
                speeds.append(speed)  # 子弹移动速度
            if event.button == 3:
                peashooter_list.append([position_x, position_y])
    # if alive:

    print("向日葵: ", sunflowers)
    print("豌豆射手: ", peashooter_list)


    # 设置动态效果的时间频率
    image_timer += 1
    if image_timer >= image_delay:
        current_frame = (current_frame + 1) % len(frames)  # 无限轮播(如果第一遍轮播到最后一张图片，则继续从第一张开始轮播)
        image_timer = 0

    # 刷新背景
    screen.fill((0, 0, 0))

    # 调用子弹函数
    bullet_update()
    bullet_draw()
    print("子弹: ", bullets)
    print("子弹的速度: ", speeds)
    for flower in sunflowers:
        screen.blit(frames[current_frame], (flower[1], flower[2]))  # 种植向日葵
        if flower[0]:
            now = pygame.time.get_ticks()
            last_shot = pygame.time.get_ticks()  # 上一次发射子弹的时间
            shoot_delay = 300  # 子弹发射间隔（毫秒）
            if now - last_shot > shoot_delay:
                last_shot = now
                bullets.append([flower[1], flower[2]])  # 子弹
                speeds.append(speed)  # 子弹移动速度
                bullet_draw()

    # for peashooter in peashooter_list:
    #     screen.blit(Peashooter, (peashooter[0], peashooter[1]))  # 种植豌豆射手
    pygame.display.flip()


