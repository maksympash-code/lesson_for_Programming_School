import pygame

pygame.init()
screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption("Pygame SHAITAN Game")
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

myfont = pygame.font.Font('fonts/font.ttf', 40)
text_logo = myfont.render('SHAITAN', False, 'Green')

player = pygame.image.load('images/icon.png')

square = pygame.Surface((50, 170))
square.fill(('Blue'))

running = True
while running:
    pygame.draw.circle(screen, 'Red', (70, 40), 30)
    screen.blit(square, (50, 10))
    screen.blit(text_logo, (150, 100))
    screen.blit(player, (100, 50))


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
