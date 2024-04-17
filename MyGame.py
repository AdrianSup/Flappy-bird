import pygame

# Initialize pygame and some basic setup
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('MyGame')
clock = pygame.time.Clock()
text_font = pygame.font.Font(None, 50)

# Background and game over surfaces
background_sky_sur = pygame.image.load('Sky.png').convert()
background_ground_sur = pygame.image.load('ground.png').convert()
background_ground_rect = background_ground_sur.get_rect(topleft=(0,300))
game_over_sur = text_font.render('Game Over', False, 'Black')
game_over_rect = game_over_sur.get_rect(center=(400,200))

# Obstacle surface and rect
obstacle1_sur = pygame.image.load('flappy_pipe.png').convert_alpha()
obstacle1_rect = obstacle1_sur.get_rect(center=(700,300))
obstacle2_sur = pygame.image.load('flappy_pipe_invert.png').convert_alpha()
obstacle2_rect = obstacle2_sur.get_rect(center=(700,0))

obstacle3_sur = pygame.image.load('flappy_pipe.png').convert_alpha()
obstacle3_rect = obstacle1_sur.get_rect(center=(1050,325))
obstacle4_sur = pygame.image.load('flappy_pipe_invert.png').convert_alpha()
obstacle4_rect = obstacle2_sur.get_rect(center=(1050,25))

obstacle5_sur = pygame.image.load('flappy_pipe.png').convert_alpha()
obstacle5_rect = obstacle1_sur.get_rect(center=(1400,275))
obstacle6_sur = pygame.image.load('flappy_pipe_invert.png').convert_alpha()
obstacle6_rect = obstacle2_sur.get_rect(center=(1400,-25))

obstacle_list = [obstacle1_rect,obstacle2_rect,obstacle3_rect,obstacle4_rect, obstacle5_rect, obstacle6_rect]

# Player surface
player_sur = pygame.image.load('angry_bird.png').convert_alpha()
player_rect = player_sur.get_rect(center=(100,150))
player_gravity = 0

game_state = "start"    # defining game states (playing, start, game over)

while True:
    for event in pygame.event.get():    # get all input from user
        if event.type == pygame.QUIT:   # stop the game without error when "X" button is pressed to close the program
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:        # "Jump" feature, when space is pressed
            if event.key == pygame.K_SPACE:
                player_gravity = -10

    if game_state == "start":                           # Pause the game when starting
        screen.blit(background_sky_sur, (0, 0))         # Waiting for a mouse click to start the game
        screen.blit(obstacle1_sur, obstacle1_rect)
        screen.blit(obstacle2_sur, obstacle2_rect)
        screen.blit(obstacle3_sur, obstacle3_rect)
        screen.blit(obstacle4_sur, obstacle4_rect)
        screen.blit(obstacle5_sur, obstacle5_rect)
        screen.blit(obstacle6_sur, obstacle6_rect)
        screen.blit(background_ground_sur, background_ground_rect)
        screen.blit(player_sur, player_rect)

        for key in pygame.mouse.get_pressed():
            if key:
                game_state = True

    elif game_state:                                # When game state is True (playing)
        screen.blit(background_sky_sur, (0,0))

        obstacle2_rect.right -= 5                   # moving all the obstacles to the left by constant speed
        obstacle1_rect.right -= 5
        obstacle3_rect.right -= 5
        obstacle4_rect.right -= 5
        obstacle5_rect.right -= 5
        obstacle6_rect.right -= 5
        screen.blit(obstacle1_sur, obstacle1_rect)
        screen.blit(obstacle2_sur, obstacle2_rect)
        screen.blit(obstacle3_sur, obstacle3_rect)
        screen.blit(obstacle4_sur, obstacle4_rect)
        screen.blit(obstacle5_sur, obstacle5_rect)
        screen.blit(obstacle6_sur, obstacle6_rect)

        screen.blit(background_ground_sur, background_ground_rect)

        for i in obstacle_list:                 # To loop back all the obstacle to the right of the screen
            if i.right <= 0: i.left = 1050
            if player_rect.colliderect(i):      # Check if player collide with the obstacle, game over
                print(i)
                game_state = False

        player_gravity += 1                     # player gravity to keep pulling the player going down
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300  # if player is on the ground, stop pulling
        screen.blit(player_sur, player_rect)
    else:                                       # when game over
        screen.blit(game_over_sur,game_over_rect)
        for key in pygame.mouse.get_pressed():  # waiting for mouse click to retry
            if key:
                obstacle1_rect = obstacle1_sur.get_rect(center=(700, 300))
                obstacle2_rect = obstacle2_sur.get_rect(center=(700, 0))
                obstacle3_rect = obstacle1_sur.get_rect(center=(1050, 325))
                obstacle4_rect = obstacle2_sur.get_rect(center=(1050, 25))
                obstacle5_rect = obstacle1_sur.get_rect(center=(1400, 275))
                obstacle6_rect = obstacle2_sur.get_rect(center=(1400, -25))
                player_rect = player_sur.get_rect(center=(100, 150))
                obstacle_list = [obstacle1_rect, obstacle2_rect, obstacle3_rect, obstacle4_rect, obstacle5_rect,
                                 obstacle6_rect]
                game_state = True
    
    pygame.display.update()     # update the frame every time
    clock.tick(60)              # cap the frame to 60 per second
