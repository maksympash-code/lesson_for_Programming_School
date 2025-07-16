import pygame


clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((618, 359))
pygame.display.set_caption("Pygame SHAITAN Game")
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

myfont = pygame.font.Font('fonts/font.ttf', 40)
text_logo = myfont.render('SHAITAN', False, 'Green')

background = pygame.image.load('images/background.png')
background_sound = pygame.mixer.Sound('sounds/background_sound.mp3')
# background_sound.play()

walk_left = [
    pygame.image.load('images/player_left_1.png'),
    pygame.image.load('images/player_left_2.png'),
    pygame.image.load('images/player_left_3.png'),
    pygame.image.load('images/player_left_4.png')
]

walk_right = [
    pygame.image.load('images/player_right_1.png'),
    pygame.image.load('images/player_right_2.png'),
    pygame.image.load('images/player_right_3.png'),
    pygame.image.load('images/player_right_4.png')
]

player_anim_count = 0
background_x = 0

player_speed = 5
player_x = 150
player_y = 250

is_jump = False
jump_count = 7

running = True
while running:
    screen.blit(background, (background_x, 0))
    screen.blit(background, (background_x + 618, 0))


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        screen.blit(walk_left[player_anim_count], (player_x, player_y))
    else:
        screen.blit(walk_right[player_anim_count], (player_x, player_y))


    if keys[pygame.K_LEFT] and player_x > 50:
        player_x -= player_speed
    elif keys[pygame.K_RIGHT] and player_x < 200:
        player_x += player_speed


    if not is_jump:
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -7:
            if jump_count > 0:
                player_y -= (jump_count ** 2) / 2
            else:
                player_y += (jump_count ** 2) / 2

            jump_count -= 1
        else:
            is_jump = False
            jump_count = 7


    if player_anim_count == 3:
        player_anim_count = 0
    else:
        player_anim_count += 1


    background_x -= 2
    if background_x == -618:
        background_x = 0


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    clock.tick(15)