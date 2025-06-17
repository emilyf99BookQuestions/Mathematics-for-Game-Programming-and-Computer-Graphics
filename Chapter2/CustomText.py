import pygame

pygame.init()
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

done = False
white = pygame.Color(255, 255, 255)

pygame.font.init()
font = pygame.font.Font('Sugar Fruit.ttf', 120)
text = font.render('Hello World', False, white)


font = pygame.font.Font('BarberChop.ttf', 120)
secondText = font.render('Bottom Text', False, white)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        screen.blit(text, (10,10))
        screen.blit(secondText, (10, 200))
        pygame.display.update()
pygame.quit()