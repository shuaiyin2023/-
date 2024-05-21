keyboard_dict = {
    "K_DOWN": (1, 0),
    "K_UP": (-1, 0),
    "K_LEFT": (0, -1),
    "K_RIGHT": (0, 1),
}


def events_func(event):
    ''' 鼠标事件 '''
    if event.type == pygame.MOUSEBUTTONDOWN:
        # print("按下鼠标了···", event.pos)
        if event.button == 1:
            position_x, position_y = event.pos
            screen.blit(image_2, (int(position_x), int(position_y)))
            pygame.display.update()
    if event.type == pygame.MOUSEBUTTONUP:
        print("鼠标弹起了···")
    if event.type == pygame.MOUSEMOTION:
        pass
        # print("鼠标移动了···")
        # mx, my = event.pos
        # r = random.randint(0, 255)
        # g = random.randint(0, 255)
        # b = random.randint(0, 255)
        # pygame.draw.circle(image_surface, (r, g, b), (int(mx), int(my)), 20)
        # pygame.display.update()

    ''' 键盘事件 '''
    if event.type == KEYDOWN:
        # 打印按键的英文字符
        key_name = pygame.key.name(event.key)
        print('键盘按下', key_name)

        # y, x = keyboard_dict.get(event.key) if keyboard_dict.get(event.key) else y, x
        if event.key == K_DOWN:
            y = 1
            x = 0
            print("向下移动了一个位置 ", event.key)  # 559 213
        elif event.key == K_UP:
            y = -1
            x = 0
            print("向上移动了一个位置")
        elif event.key == K_LEFT:
            x = -1
            y = 0
            print("向左移动了一个位置")
        elif event.key == K_RIGHT:
            x = 1
            y = 0
            print("向右移动了一个位置")

    elif event.type == KEYUP:
        print("松开了键盘")
        x = 0
        y = 0