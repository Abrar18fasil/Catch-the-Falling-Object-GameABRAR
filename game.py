# Import necessary libraries
import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch the Falling Objects")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Game settings
basket_width = 100
basket_height = 20
basket_x = SCREEN_WIDTH // 2 - basket_width // 2
basket_y = SCREEN_HEIGHT - basket_height - 10
basket_speed = 10

# Falling object settings
object_width = 30
object_height = 30
object_speed = 5
object_x = random.randint(0, SCREEN_WIDTH - object_width)
object_y = -object_height

# Score
score = 0
font = pygame.font.SysFont(None, 36)

# Game loop
running = True
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Basket movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_x > 0:
        basket_x -= basket_speed
    if keys[pygame.K_RIGHT] and basket_x < SCREEN_WIDTH - basket_width:
        basket_x += basket_speed

    # Falling object movement
    object_y += object_speed
    if object_y > SCREEN_HEIGHT:
        object_y = -object_height
        object_x = random.randint(0, SCREEN_WIDTH - object_width)

    # Check for collision
    basket_rect = pygame.Rect(basket_x, basket_y, basket_width, basket_height)
    object_rect = pygame.Rect(object_x, object_y, object_width, object_height)
    if basket_rect.colliderect(object_rect):
        score += 1
        object_y = -object_height
        object_x = random.randint(0, SCREEN_WIDTH - object_width)

    # Draw basket and falling object
    pygame.draw.rect(screen, GREEN, basket_rect)
    pygame.draw.rect(screen, RED, object_rect)

    # Display score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Update the screen
    pygame.display.flip()
    pygame.time.Clock().tick(30)  # Set the frame rate

pygame.quit()
