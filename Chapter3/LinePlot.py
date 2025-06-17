import pygame

pygame.init()

screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))

done = False
white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 255, 0)

xOriginOffset = int(screen.get_width() / 2)
yOriginOffset = int(screen.get_height() / 2)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # X Axis
    for x in range(-500, 500):
        screen.set_at((x + xOriginOffset, yOriginOffset), green)

    #y Axis
    for y in range(-400, 400):
        screen.set_at((xOriginOffset, y + yOriginOffset), green)

    for x in range(-500, 500):
        y = 2 * x + 4
        screen.set_at((x + xOriginOffset, y + yOriginOffset), white)

    pygame.display.update()
pygame.quit()


