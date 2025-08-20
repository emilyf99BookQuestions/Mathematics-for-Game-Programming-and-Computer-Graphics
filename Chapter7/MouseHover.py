import pygame
from pygame.locals import *

pygame.init()
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

done = False

# Color DefMouseDrawing.py
white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 255, 0)

# Button Def
button = (0, 0, 100, 30)

while not done:
    pygame.draw.rect(screen, green, button)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            mx = mouse_pos[0]
            my = mouse_pos[1]

            if button[0] < mx < (button[0] + button[2]) and button[1] < my > (button[1] + button[3]):
                print("Mouse Over")
    pygame.display.update()
pygame.quit()


