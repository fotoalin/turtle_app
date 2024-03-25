import pygame
import random

# Initialize Pygame
pygame.init()

# Screen Dimensions
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Player Setup
player_width = 100  # Increased width for a wider catch area
player_height = 20
player_x = (screen_width / 2) - (player_width / 2)
player_y = screen_height - player_height - 10
player_velocity = 2  # Reduced velocity for better control

# Falling Object Setup
falling_object_x = random.randrange(0, screen_width)
falling_object_y = -20
falling_object_width = 20
falling_object_height = 20
falling_object_velocity = 2  # Reduced velocity for better game pacing

# Score
score = 0
font = pygame.font.SysFont(None, 35)

def show_score(x, y, score):
    score_text = font.render("Score: " + str(score), True, white)
    screen.blit(score_text, (x, y))

# Main Game Loop
running = True
while running:
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_velocity
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_velocity

    # Falling Object Movement
    falling_object_y += falling_object_velocity
    if falling_object_y > screen_height:
        falling_object_y = -20
        falling_object_x = random.randrange(0, screen_width)

    # Collision Detection
    if player_y < falling_object_y + falling_object_height and player_y + player_height > falling_object_y:
        if player_x < falling_object_x + falling_object_width and player_x + player_width > falling_object_x:
            falling_object_y = -20
            falling_object_x = random.randrange(0, screen_width)
            score += 1  # Increase score only when the object is caught

    # Drawing
    pygame.draw.rect(screen, white, [player_x, player_y, player_width, player_height])
    pygame.draw.rect(screen, red, [falling_object_x, falling_object_y, falling_object_width, falling_object_height])
    show_score(10, 10, score)

    pygame.display.update()

pygame.quit()

