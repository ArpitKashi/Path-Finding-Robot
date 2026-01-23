import pygame
import time
from env import GridWorld
from agent import DQNAgent

# Initialize pygame
pygame.init()

CELL_SIZE = 50
GRID_SIZE = 10
WIDTH = HEIGHT = GRID_SIZE * CELL_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Path Finding Robot - DQN")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)

env = GridWorld(size=GRID_SIZE)
agent = DQNAgent(4, 4)
agent.epsilon = 0  # No random moves

state = env.reset()

def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        for y in range(0, HEIGHT, CELL_SIZE):
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, BLACK, rect, 1)

def draw_elements():
    # Goal
    gx, gy = env.goal
    pygame.draw.rect(
        screen, GREEN,
        (gy*CELL_SIZE, gx*CELL_SIZE, CELL_SIZE, CELL_SIZE)
    )

    # Obstacles
    for ox, oy in env.obstacles:
        pygame.draw.rect(
            screen, RED,
            (oy*CELL_SIZE, ox*CELL_SIZE, CELL_SIZE, CELL_SIZE)
        )

    # Robot
    rx, ry = env.agent_pos
    pygame.draw.rect(
        screen, BLUE,
        (ry*CELL_SIZE, rx*CELL_SIZE, CELL_SIZE, CELL_SIZE)
    )

running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)
    draw_grid()
    draw_elements()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    action = agent.act(state)
    state, reward, done = env.step(action)

    pygame.display.flip()
    clock.tick(2)  # robot speed (slow for visibility)

    if done:
        print("Goal Reached 🎯")
        time.sleep(2)
        running = False

pygame.quit()