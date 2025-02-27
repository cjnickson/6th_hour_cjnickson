import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Platformer Adventure")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Game settings
clock = pygame.time.Clock()
player_speed = 5
gravity = 0.5
jump_strength = -10
score = 0

# Fonts
font = pygame.font.SysFont("Arial", 30)

# Define game objects
player_width = 50
player_height = 60
player_x = 100
player_y = screen_height - player_height - 60
player_velocity_y = 0
on_ground = False

# Platform class
class Platform:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self):
        pygame.draw.rect(screen, GREEN, self.rect)

# Enemy class
class Enemy:
    def __init__(self, x, y, width, height, speed):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed
        self.direction = 1  # 1: moving right, -1: moving left

    def update(self):
        self.rect.x += self.speed * self.direction
        if self.rect.x < 0 or self.rect.x > screen_width - self.rect.width:
            self.direction *= -1

    def draw(self):
        pygame.draw.rect(screen, RED, self.rect)

# Collectible class
class Collectible:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self):
        pygame.draw.circle(screen, BLUE, self.rect.center, self.rect.width // 2)

# Create game objects
player = pygame.Rect(player_x, player_y, player_width, player_height)
platforms = [Platform(0, screen_height - 40, screen_width, 40), Platform(200, 400, 200, 20), Platform(500, 300, 200, 20)]
enemies = [Enemy(400, 500, 50, 50, 3), Enemy(600, 200, 50, 50, 2)]
collectibles = [Collectible(random.randint(100, 700), random.randint(100, 500), 20, 20) for _ in range(5)]

# Game loop
while True:
    screen.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player.x += player_speed
    if keys[pygame.K_SPACE] and on_ground:
        player_velocity_y = jump_strength
        on_ground = False

    # Apply gravity
    player_velocity_y += gravity
    player.y += player_velocity_y

    # Collision with platforms
    on_ground = False
    for plat in platforms:
        if player.colliderect(plat.rect) and player_velocity_y >= 0:
            player_velocity_y = 0
            player.y = plat.rect.top - player.height
            on_ground = True

    # Update enemies
    for enemy in enemies:
        enemy.update()

    # Collectibles logic
    for collectible in collectibles[:]:
        if player.colliderect(collectible.rect):
            collectibles.remove(collectible)
            score += 1

    # Draw platforms
    for plat in platforms:
        plat.draw()

    # Draw enemies
    for enemy in enemies:
        enemy.draw()

    # Draw collectibles
    for collectible in collectibles:
        collectible.draw()

    # Draw player
    pygame.draw.rect(screen, BLACK, player)

    # Draw score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Check for game over
    if player.y > screen_height:
        game_over_text = font.render("Game Over! Press R to restart.", True, RED)
        screen.blit(game_over_text, (screen_width // 3, screen_height // 2))
        pygame.display.update()

        # Wait for restart input
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    # Reset the game
                    player.x = 100
                    player.y = screen_height - player_height - 60
                    player_velocity_y = 10
                    collectibles = [Collectible(random.randint(100, 700), random.randint(100, 500), 20, 20) for _ in range(5)]
                    score = 0
                    break

    # Update screen
    pygame.display.update()
    clock.tick(60)
