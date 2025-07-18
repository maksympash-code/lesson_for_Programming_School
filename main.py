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
pygame.time.set_timer(enemy_timer, 2000)
enemy_list_in_game = []

bullet = pygame.image.load('images/bullet.png').convert_alpha()
bullets = []
bullets_left = 5

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
jump_count = 8

gamePlay = True
label = pygame.font.Font('fonts/font.ttf', 40)
lose_label = label.render('You lose!', False, (193, 196, 199))
restart_label = label.render('Play again', False, (115, 132, 148))
restart_label_rect = restart_label.get_rect(topleft = (225, 150))

running = True
while running:
    screen.blit(background, (background_x, 0))
    screen.blit(background, (background_x + 618, 0))


    if gamePlay:
        player_rect = walk_left[0].get_rect(topleft = (player_x, player_y))

        if enemy_list_in_game:
            for (i, el) in enumerate(enemy_list_in_game):
                screen.blit(enemy, el)
                el.x -= 10

                if el.x < -10:
                    enemy_list_in_game.pop(i)

                if player_rect.colliderect(el):
                    gamePlay = False


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
            if jump_count >= -8:
                if jump_count > 0:
                    player_y -= (jump_count ** 2) / 2
                else:
                    player_y += (jump_count ** 2) / 2

                jump_count -= 1
            else:
                is_jump = False
                jump_count = 8


        if player_anim_count == 3:
            player_anim_count = 0
        else:
            player_anim_count += 1


        background_x -= 2
        if background_x == -618:
            background_x = 0

        if bullets:
            for (i, el) in enumerate(bullets):
                screen.blit(bullet, (el.x, el.y))
                el.x += 4

                if el.x > 630:
                    bullets.pop(i)

                if enemy_list_in_game:
                    for (index, enemy_el) in enumerate(enemy_list_in_game):
                        if el.colliderect(enemy_el):
                            enemy_list_in_game.pop(index)
                            bullets.pop(i)

    else:
        screen.fill((87, 88, 89))
        screen.blit(lose_label, (230, 100))
        screen.blit(restart_label, restart_label_rect)

        mouse = pygame.mouse.get_pos()
        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gamePlay = True
            player_x = 150
            enemy_list_in_game.clear()
            bullets.clear()


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == enemy_timer:
            enemy_list_in_game.append(enemy.get_rect(topleft = (620, 250)))
        if gamePlay and event.type == pygame.KEYUP and event.key == pygame.K_b and bullets_left >= 0:
            bullets.append(bullet.get_rect(topleft = (player_x + 30, player_y + 10)))
            bullets_left -= 1

    clock.tick(15)