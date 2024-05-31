import pygame
from pygame.locals import *


pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("pygame")
font = pygame.font.SysFont(None, 24)


clock = pygame.time.Clock()

str1 = ""
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            str1 += str(event.unicode)

    screen.fill((0, 0, 0))
    current_text = font.render(str1, True, "green")
    screen.blit(current_text, (20, 20))
    pygame.display.update()

