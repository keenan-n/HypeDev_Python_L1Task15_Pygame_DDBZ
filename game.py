# Import game library:
import pygame

# Import random numbers:
import random

# Initialize pygame:
pygame.init()

# Set Caption, Icon:
icon = pygame.image.load("icon.png")
pygame.display.set_caption("Dragon Dodge Ball Z")
pygame.display.set_icon(icon)

# Set screen size:
screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
# Screen Background:
background = pygame.image.load("background.jpg")

# Player:
player = pygame.image.load("player.png")
# Enemy:
enemy_up = pygame.image.load("enemy_ball_up.png")
enemy_down = pygame.image.load("enemy_ball_down.png")
enemy_left = pygame.image.load("enemy_ball_right.png")
enemy_right = pygame.image.load("enemy_ball_left.png")
# Prize:
prize = pygame.image.load("prize.png")

# Player Height & Width:
image_height = player.get_height()
image_width = player.get_width()
# Enemy Height & Width:
# Enemy Ball 1:
enemy_height_1u = enemy_up.get_height()
enemy_width_1u = enemy_up.get_width()
# Enemy Ball :
enemy_height_2d = enemy_down.get_height()
enemy_width_2d = enemy_down.get_width()
# Enemy Ball 3:
enemy_height_3l = enemy_left.get_height()
enemy_width_3l = enemy_left.get_width()
# Enemy Ball 4:
enemy_height_4r = enemy_right.get_height()
enemy_width_4r = enemy_right.get_width()

# Prize Height & Width:
prize_height = prize.get_height()
prize_width = prize.get_width()

print(f"Player Height: {image_height}")
print(f"Player Width: {image_width}")
print("")

# Player Position:
player_posX = 650
player_posY = 250
vel_player = 7

# Enemy Positions:
enemy_posY_1u = 800
enemy_posX_1u = random.randint(0, screen_width - enemy_width_1u)

enemy_posY_2d = - 500
enemy_posX_2d = random.randint(0, screen_width - enemy_width_2d)

enemy_posX_3l = - 500
enemy_posY_3l = random.randint(0, screen_height - enemy_height_3l)

enemy_posX_4r = 1400
enemy_posY_4r = random.randint(0, screen_height - enemy_height_4r)

# Prize Position:
prize_posX = 4000
prize_posY = random.randint(0, screen_height - prize_height)
# Check if keys are pressed:
keyUp = False
keyDown = False
keyLeft = False
keyRight = False
escape = False

# Game Loop:
while 1:

    screen.fill((0, 0, 0))  # Clears Screen.
    # Background Draw:
    screen.blit(background, (0, 0))
    # Draw Player:
    screen.blit(player, (player_posX,
                         player_posY))
    # Draw Enemy:
    screen.blit(enemy_up, (enemy_posX_1u, enemy_posY_1u))
    screen.blit(enemy_down, (enemy_posX_2d, enemy_posY_2d))
    screen.blit(enemy_left, (enemy_posX_3l, enemy_posY_3l))
    screen.blit(enemy_right, (enemy_posX_4r, enemy_posY_4r))

    # Draw Prize:
    screen.blit(prize, (prize_posX, prize_posY))

    # Update Screen:
    pygame.display.flip()

    # Event Game Loop:
    for event in pygame.event.get():
        # Check if player quits game.
        # If player quits game, end program:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        # Check if Key is Down:
        if event.type == pygame.KEYDOWN:
            # Test:
            if event.key == pygame.K_UP:
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True
            if event.key == pygame.K_ESCAPE:
                keyRight = True

        # Check if Key is Up:
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False
            if event.key == pygame.K_ESCAPE:
                escape = False

    # Player Move:
    if keyUp:
        if player_posY > 0:
            player_posY -= vel_player
    if keyDown:
        if player_posY < screen_height - image_height:
            player_posY += vel_player

    if keyLeft:
        if player_posX > 0:
            player_posX -= vel_player
    if keyRight:
        if player_posX < screen_width - image_width:
            player_posX += vel_player

    if escape:
        pygame.quit()
        exit(0)

    # PlayerBox:
    playerBox = pygame.Rect(player.get_rect())
    # Make Box stay around player:
    playerBox.top = player_posY
    playerBox.left = player_posX

    # EnemyBox 1:
    enemyBox1 = pygame.Rect(enemy_up.get_rect())
    enemyBox1.top = enemy_posY_1u
    enemyBox1.left = enemy_posX_1u

    # EnemyBox 2:
    enemyBox2 = pygame.Rect(enemy_down.get_rect())
    enemyBox2.top = enemy_posY_2d
    enemyBox2.left = enemy_posX_2d

    # EnemyBox 3:
    enemyBox3 = pygame.Rect(enemy_left.get_rect())
    enemyBox3.top = enemy_posY_3l
    enemyBox3.left = enemy_posX_3l

    # EnemyBox 4:
    enemyBox4 = pygame.Rect(enemy_right.get_rect())
    enemyBox4.top = enemy_posY_4r
    enemyBox4.left = enemy_posX_4r

    # Prize:
    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prize_posY
    prizeBox.left = prize_posX

    # If player hits Plasma Bolt, Print Lose Statement:
    if playerBox.colliderect(enemyBox1):
        print("You've Hit Plasma Bolt 1")
        print("You Lose!")
        print("IT'S NOT OVER WHEN YOU LOSE!! IT'S OVER WHEN YOU QUIT!!")
        # Quit Program:
        pygame.quit()
        exit(0)
    elif playerBox.colliderect(enemyBox2):
        print("You've Hit Plasma Bolt 2")
        print("You Lose!")
        print("IT'S NOT OVER WHEN YOU LOSE!! IT'S OVER WHEN YOU QUIT!!")
        # Quit Program:
        pygame.quit()
        exit(0)
    elif playerBox.colliderect(enemyBox3):
        print("You've Hit Plasma Bolt 3")
        print("You Lose!")
        print("IT'S NOT OVER WHEN YOU LOSE!! IT'S OVER WHEN YOU QUIT!!")
        # Quit Program:
        pygame.quit()
        exit(0)
    elif playerBox.colliderect(enemyBox4):
        print("You've Hit Plasma Bolt 4")
        print("You Lose!")
        print("IT'S NOT OVER WHEN YOU LOSE!! IT'S OVER WHEN YOU QUIT!!")
        # Quit Program:
        pygame.quit()
        exit(0)

    if playerBox.colliderect(prizeBox):
        print("You've collected the DragonBall, You Win!")
        # Quit Program:
        pygame.quit()
        exit(0)

    if prize_posX < 0:
        print("You've Missed The DragonBall!")
        print("You Lose!")
        print("IT'S NOT OVER WHEN YOU LOSE!! IT'S OVER WHEN YOU QUIT!!")

        pygame.quit()
        exit(0)

    # Enemy approach:
    # Up:
    enemy_posY_1u -= 4
    # Down:
    enemy_posY_2d += 4
    # Left:
    enemy_posX_3l += 4
    # Right:
    enemy_posX_4r -= 4

    # Prize approach:
    prize_posX -= 8
