import pygame
pygame.init()

screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

done = False
white = pygame.Color(255, 255, 255)


def to_pygame_coordinates(display, x , y):
    return x,display.get_height() - y


def draw_star(x, y, size):
    screen_x, screen_y = to_pygame_coordinates(screen, x, y)
    pygame.draw.rect(screen, white, (screen_x, screen_y, size, size))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    draw_star(150, 150, 10)
    draw_star(300, 200, 10)
    draw_star(305, 300, 5)
    draw_star(600, 100, 10)
    draw_star(550, 350, 5)
    draw_star(600, 200, 5)
    draw_star(550, 275, 20)
    draw_star(650, 400, 5)
    draw_star(700, 350, 5)

    pygame.display.update()
pygame.quit()