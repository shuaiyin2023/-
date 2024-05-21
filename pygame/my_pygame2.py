import sys

import pygame


# 创建精灵类
class Sprite(pygame.sprite.Sprite):

    def __init__(self, image, position):
        pygame.sprite.Sprite.__init__(self)
        # 加载图片
        # self.image = pygame.image.load(image)
        self.image = image
        # 获取图片的rect区域
        self.rect = self.image.get_rect()
        # 设置位置
        self.rect.topleft = position


pygame.init()
width = 800
height = 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("第二个pygame项目")
screen.fill((255, 255, 255))

# 设置草坪背景
grass_sprite = pygame.image.load("./背景.png")
grass_sprite = pygame.transform.scale(grass_sprite, (width, height))  # 缩放图片

image_1 = pygame.image.load("./豌豆射手.png")
image_1 = pygame.transform.scale(image_1, (50, 50))  # 缩放图片
position = (100, 150)  # 位置

image_2 = pygame.image.load("./僵尸.png")
image_2 = pygame.transform.scale(image_2, (50, 50))  # 缩放图片
position_2 = (600, 150)  # 位置


sprite_1 = Sprite(image_1, position)
sprite_2 = Sprite(image_2, position_2)

crash_result = pygame.sprite.collide_mask(sprite_1, sprite_2)

if crash_result:
    print("两个精灵碰撞了")
else:
    print("两个精灵没有碰撞")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        # 鼠标事件
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("按下鼠标了···", event.pos)
            print("按下鼠标的键位: ", event.button)  # 1: 左键，2: 滚轮，3: 右键
            mx, my = event.pos
            # 调用pygame.draw画图
            # pygame.draw.circle(screen, blue, (int(mx), int(my)), 50)
            if event.button == 1:
                screen.blit(sprite_1.image, (int(mx), int(my)))
            if event.button == 3:
                screen.blit(sprite_2.image, (int(mx), int(my)))
            pygame.display.update()

    # 绘制精灵到窗口
    # screen.blit(sprite_1.image, sprite_1.rect)
    # screen.blit(sprite_2.image, sprite_2.rect)
    screen.blit(grass_sprite, (0, 0))

    # 刷新屏幕
    pygame.display.update()



