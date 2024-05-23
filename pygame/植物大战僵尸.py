import pygame
import sys
from pygame.locals import *

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
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
        self.base_damage = 20  # 初始伤害

    # 循环发射子弹
    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            bullet = Bullet(self.rect.center)
            all_plants_sprites.add(bullet)  # 将循环生成的子弹添加到植物精灵组中是为了将与植物相关的子弹循环生成，实现循环发射的效果
            bullets.add(bullet)  # 这里将子弹加入子弹精灵组中是为了在子弹精灵组中专门处理子弹的移动、碰撞等逻辑

        ''' 因为在Plants的循环发射子弹中，每新增一颗子弹，都会在植物精灵组中也添加一个子弹精灵，
                如果数据过大占用过多内存影响性能，所以当子弹超出边界，将其从精灵组中删除 '''
        for _sprite in all_plants_sprites:
            if _sprite.rect.right >= WIDTH:
                _sprite.kill()

        self.be_devoured()

    # 植物是否被僵尸吃掉
    def be_devoured(self):
        for _sprite in all_plants_sprites:
            for _zombie in all_zombie_sprites:
                if pygame.sprite.collide_rect(_sprite, _zombie):
                    _sprite.kill()
                    # _zombie.kill()


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
        screen.blit(self.image, self.rect)

    # def update(self):
    #     pass


""" 豌豆射手类 """


class Peashooter(Plants):

    def __init__(self, pos):
        super().__init__(pos)
        self.image = pygame.image.load('./images/Peashooter.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))


""" 子弹类 """


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)  # 创建带有Alpha通道的表面对象
        pygame.draw.circle(self.image, (255, 123, 0), (10, 10), 10)  # 绘制红色圆形子弹
        self.rect = self.image.get_rect(center=pos)
        self.speed = 2

    # 子弹移动及是否超出范围
    def update(self):
        self.rect.x += self.speed
        if self.rect.right < 0:
            self.kill()


""" 僵尸类 """


class Zombies(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load('./images/zombie.png').convert_alpha()  # 僵尸
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(center=pos)
        self.speed = 1
        self.blood_volume = 100

    # 僵尸移动
    def update(self):
        self.rect.x -= self.speed
        if self.rect.left < 0:
            self.kill()

        self.is_attack()

    # 检测僵尸是否被攻击
    def is_attack(self):
        for _bullet in bullets:
            for _zombie in all_zombie_sprites:
                if pygame.sprite.collide_rect(_bullet, _zombie):
                    _bullet.kill()
                    # 因为在主循环中点击鼠标时，初始化了plant对象，属于全局可见，所以可以直接访问此属性plant.base_damage
                    self.take_damage(plant.base_damage)

    # 根据血量进行处理
    def take_damage(self, damage):
        self.blood_volume -= damage
        if self.blood_volume <= 0:
            self.kill()


all_plants_sprites = pygame.sprite.Group()  # 所有植物类精灵
all_zombie_sprites = pygame.sprite.Group()  # 所有僵尸类精灵
bullets = pygame.sprite.Group()  # 所有植物类子弹精灵

clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                plant = SunFlowers(event.pos)
                plant.deal_image()  # 调用 deal_image() 方法来切分图像
                all_plants_sprites.add(plant)
            if event.button == 3:
                zombie = Zombies(event.pos)
                all_zombie_sprites.add(zombie)

    # 这个for循环用于展示向日葵的动态效果
    for sprite in all_plants_sprites:
        if isinstance(sprite, SunFlowers):
            sprite.dynamic_effect()

    # 子弹超出边界则将其销毁
    for bullet in bullets:
        if bullet.rect.right <= 0:
            bullet.kill()
    all_plants_sprites.update()  # 将精灵组中的所有精灵对象的状态和属性及时更新
    all_zombie_sprites.update()  # 将精灵组中的所有精灵对象的状态和属性及时更新

    print("僵尸: \n", all_zombie_sprites, len(all_zombie_sprites))
    print("植物: \n", all_plants_sprites, len(all_plants_sprites))
    print("子弹: \n", bullets, len(bullets))

    screen.fill((0, 0, 0))
    all_plants_sprites.draw(screen)  # 将所有精灵组中的精灵对象绘制到屏幕上
    all_zombie_sprites.draw(screen)  # 将所有精灵组中的精灵对象绘制到屏幕上

    pygame.display.flip()

pygame.quit()
sys.exit()
