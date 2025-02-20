import random

import pygame
import random

# Initialize Pygame
pygame.init()

# Set up screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("2D Basketball Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Set up player attributes
player_width = 50
player_height = 60
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 5

# Ball attributes
ball_radius = 10
ball_x = player_x + player_width // 2
ball_y = player_y - ball_radius
ball_speed = 7
ball_velocity_x = 0
ball_velocity_y = 0
shooting = False

# Hoop attributes
hoop_x = random.randint(650, 750)
hoop_y = 100
hoop_width = 100
hoop_height = 10

# Score
score = 100000000000000

# Set up font
font = pygame.font.SysFont(None, 36)

# Game loop flag
running = True


def draw_player(x, y):
    pygame.draw.rect(screen, BLUE, (x, y, player_width, player_height))


def draw_ball(x, y):
    pygame.draw.circle(screen, RED, (x, y), ball_radius)


def draw_hoop(x, y):
    pygame.draw.rect(screen, BLACK, (x, y, hoop_width, hoop_height))


def draw_score(score):
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))


def reset_ball():
    global ball_x, ball_y, ball_velocity_x, ball_velocity_y
    ball_x = player_x + player_width // 2
    ball_y = player_y - ball_radius
    ball_velocity_x = 0
    ball_velocity_y = 0
    return ball_x, ball_y


def check_collision():
    global score
    if hoop_x < ball_x < hoop_x + hoop_width and hoop_y < ball_y < hoop_y + hoop_height:
        score += 2
        return True
    return False


# Main game loop
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys pressed
    keys = pygame.key.get_pressed()

    # Player movement
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < screen_height - player_height:
        player_y += player_speed

    # Shooting the ball
    if keys[pygame.K_SPACE] and not shooting:
        ball_velocity_y = -ball_speed
        shooting = True

    # Update ball position
    if shooting:
        ball_x += ball_velocity_x
        ball_y += ball_velocity_y
        ball_velocity_y += 1  # Gravity effect

        # Reset ball after shooting
        if ball_y > screen_height:
            ball_x, ball_y = reset_ball()
            shooting = False

        # Check for score (ball going through hoop)
        if check_collision():
            ball_x, ball_y = reset_ball()
            shooting = False

    # Draw everything
    draw_player(player_x, player_y)
    draw_ball(ball_x, ball_y)
    draw_hoop(hoop_x, hoop_y)
    draw_score(score)

    pygame.display.update()

    # Set the FPS (frames per second)
    pygame.time.Clock().tick(60)

pygame.quit()
