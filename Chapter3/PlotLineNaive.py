import pygame
from pygame.locals import *
pygame.init()

screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
done = False

white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 255, 0)

timesClicked = 0

def plot_line(point1, point2):
    if point2[0] < point1[0]:
        temp = point2
        point2 = point1
        point1 = temp

    x0, y0 = point1
    x1, y1 = point2
    m = (y1 - y0) / (x1 - x0)
    c = y0 - (m * x0)

    for x in range (x0 , x1):
        y = m * x + c
        screen.set_at((int(x), int (y)), white)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == MOUSEBUTTONDOWN:
            if timesClicked == 0:
                point1 = pygame.mouse.get_pos()
            else:
                point2 = pygame.mouse.get_pos()
            timesClicked += 1
            if timesClicked > 1:
                plot_line(point1, point2)
                timesClicked = 0
    pygame.display.update()
pygame.quit()