import pygame


clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((618, 359))
pygame.display.set_caption("Pygame SHAITAN Game")
icon = pygame.image.load('images/icon.png').convert_alpha()
pygame.display.set_icon(icon)

myfont = pygame.font.Font('fonts/font.ttf', 40)
text_logo = myfont.render('SHAITAN', False, 'Green')

background = pygame.image.load('images/background.png').convert_alpha()
background_sound = pygame.mixer.Sound('sounds/background_sound.mp3')
# background_sound.play()

enemy = pygame.image.load('images/enemy.png').convert_alpha()
enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer, 2500)
enemy_list_in_game = []

walk_left = [
    pygame.image.load('images/player_left_1.png').convert_alpha(),
    pygame.image.load('images/player_left_2.png').convert_alpha(),
    pygame.image.load('images/player_left_3.png').convert_alpha(),
    pygame.image.load('images/player_left_4.png').convert_alpha()
]

walk_right = [
    pygame.image.load('images/player_right_1.png').convert_alpha(),
    pygame.image.load('images/player_right_2.png').convert_alpha(),
    pygame.image.load('images/player_right_3.png').convert_alpha(),
    pygame.image.load('images/player_right_4.png').convert_alpha()
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


    player_rect = walk_left[0].get_rect(topleft = (player_x, player_y))

    if enemy_list_in_game:
        for el in enemy_list_in_game:
            screen.blit(enemy, el)
            el.x -= 10

            if player_rect.colliderect(el):
                print("You lose")


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
        if event.type == enemy_timer:
            enemy_list_in_game.append(enemy.get_rect(topleft = (620, 250)))

    clock.tick(15)