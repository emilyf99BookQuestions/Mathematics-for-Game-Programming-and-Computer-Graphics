import pygame
from pygame.display import update

pygame.init()
screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pretty Background')
done = False

background = pygame.image.load('background.jpg')
sprite = pygame.image.load('blue-bird.png')

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.blit(background, (0,0))
    screen.blit(sprite, (100,100))
    pygame.display,update()
pygame.quit()