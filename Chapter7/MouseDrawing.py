import pygame
from pygame.locals import *

pygame.init()
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

done = False
mouse_down = False

white = pygame.Color(255, 255, 255)
last_mouse_pos = (0, 0)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            mouse_down = True

        elif event.type == MOUSEBUTTONUP and event.button == 1:
            mouse_down = False
            last_mouse_pos = pygame.mouse.get_pos()

        elif event.type == MOUSEMOTION and mouse_down is True:
            pygame.draw.line(screen, white,last_mouse_pos, pygame.mouse.get_pos(), 5)
            last_mouse_pos = pygame.mouse.get_pos()

    pygame.display.update()
pygame.quit()


