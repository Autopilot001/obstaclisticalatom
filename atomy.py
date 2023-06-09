import pygame
import random

# Define some constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 50
OBSTACLE_SPEED = 5

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Avoid the Obstacles')

# Set up the clock
clock = pygame.time.Clock()

# Load images
player_img = pygame.image.load('player.png')
obstacle_img = pygame.image.load('obstacle.png')

# Define the Player class
class Player:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT - PLAYER_HEIGHT - 10
        self.width = PLAYER_WIDTH
        self.height = PLAYER_HEIGHT
        self.img = player_img
    
    def draw(self):
        screen.blit(self.img, (self.x, self.y))

# Define the Obstacle class
class Obstacle:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH - OBSTACLE_WIDTH)
        self.y = -OBSTACLE_HEIGHT
        self.width = OBSTACLE_WIDTH
        self.height = OBSTACLE_HEIGHT
        self.img = obstacle_img
    
    def update(self):
        self.y += OBSTACLE_SPEED
    
    def draw(self):
        screen.blit(self.img, (self.x, self.y))

# Set up the game loop
player = Player()
obstacles = []
game_over = False
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    
    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= 5
    if keys[pygame.K_RIGHT] and player.x < SCREEN_WIDTH - PLAYER_WIDTH:
        player.x += 5
    
    # Spawn new obstacles
    if random.randint(0, 100) < 10:
        obstacles.append(Obstacle())
    
    # Update and draw obstacles
    for obstacle in obstacles:
        obstacle.update()
        obstacle.draw()
        
        # Check for collisions
        if player.x < obstacle.x + obstacle.width and player.x + player.width > obstacle.x and player.y < obstacle.y + obstacle.height and player.y + player.height > obstacle.y:
            game_over = True
    
    # Draw the player
    player.draw()
    
    # Update the screen
