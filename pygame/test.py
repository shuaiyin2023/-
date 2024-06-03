import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("pygame")
font = pygame.font.SysFont("kaiti", 24)

figure = pygame.Rect(20, 20, 100, 100)
pygame.draw.rect(screen, (0, 214, 222), figure)
left_boundary = figure.x + figure.width
top_boundary = figure.y + figure.height

figure_2 = pygame.Rect(left_boundary + 50, 20, 100, 100)
pygame.draw.rect(screen, (0, 10, 150), figure_2)
left_boundary_2 = figure_2.x + figure_2.width
top_boundary_2 = figure_2.y + figure_2.height

figure_count = figure_2_count = 0

# figure_list = []
# figure_list.append(
#     {"figure": figure, "left_boundary": figure.x + figure.width, "top_boundary": figure.y + figure.height, "count": 0})
# figure_list.append(
#     {"figure": figure_2, "left_boundary": figure_2.x + figure_2.width, "top_boundary": figure_2.y + figure_2.height,
#      "count": 0})


# def draw_figure(figure_obj, count, left_border, top_border, pos_x, pos_y):
#     if figure_obj.collidepoint(pos_x, pos_y):
#         count += 1
#         text = font.render(str(count), True, "green")
#     else:
#         text = font.render(str(count), True, "green")
#
#     screen.blit(text, (figure_obj.x + ((left_border - figure_obj.x) // 2), top_border + 20))
#
#     return text


clock = pygame.time.Clock()

str1 = ""
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            str1 += str(event.unicode)
        if event.type == MOUSEBUTTONDOWN:
            print("鼠标事件: ", event.pos)
            screen.fill((0, 0, 0))
            pygame.draw.rect(screen, (0, 214, 222), figure)
            pygame.draw.rect(screen, (0, 10, 150), figure_2)
            x, y = event.pos

            # for figure_obj in figure_list:
            #     draw_figure(figure_obj["figure"], figure_obj["count"], figure_obj["left_boundary"],
            #                 figure_obj["top_boundary"], x, y)
            if figure.collidepoint(x, y):
                figure_count += 1
                current_text = font.render(str(figure_count), True, "green")
            else:
                current_text = font.render(str(figure_count), True, "green")

            if figure_2.collidepoint(x, y):
                figure_2_count += 1
                current_text_2 = font.render(str(figure_2_count), True, "green")
            else:
                current_text_2 = font.render(str(figure_2_count), True, "green")

            screen.blit(current_text, (figure.x + ((left_boundary - figure.x) // 2), top_boundary + 20))
            screen.blit(current_text_2, (figure_2.x + ((left_boundary_2 - figure_2.x) // 2), top_boundary_2 + 20))

            # if current_index < len(text_list):
            #     current_text = font.render(text_list[current_index], True, "green")
            #     screen.blit(current_text, (left, top))
            #     top += 30
            #     current_index += 1
            # else:
            #     current_index = 0
            #     screen.fill((0, 0, 0))
            #     top = 20

    pygame.display.update()
