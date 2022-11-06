"""
Conway's Game of Life
A cellular automata devised in 1970 by John Conway
recreated here in Python

J-A-Collins 06-11-22
"""

# Imports
from copy import deepcopy
from random import randint

import pygame

# Variables
WIDTH = 450
HEIGHT = 450
RES = WIDTH, HEIGHT
TILE = 15
W = WIDTH // TILE
H = HEIGHT // TILE
FPS = 10


def cell_check(current_state, x, y):
    count = 0
    for j in range(y - 1, y + 2):
        for i in range(x - 1, x + 2):
            if current_state[j][i]:
                count += 1

    if current_state[y][x]:
        count -= 1
        if count == 2 or count == 3:
            return 1
        return 0
    else:
        if count == 3:
            return 1
        return 0


if __name__ == "__main__":
    pygame.init()
    surface = pygame.display.set_mode(RES)
    clock = pygame.time.Clock()

    gen = 0
    next_state = [[0 for i in range(W)] for j in range(H)]
    current_state = [[randint(0, 1) for i in range(W)] for j in range(H)]

    while True:
        surface.fill(pygame.Color("white"))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        [
            pygame.draw.line(surface, pygame.Color("black"), (x, 0), (x, HEIGHT))
            for x in range(0, WIDTH, TILE)
        ]
        [
            pygame.draw.line(surface, pygame.Color("black"), (0, y), (WIDTH, y))
            for y in range(0, HEIGHT, TILE)
        ]
        # Draw cells
        for x in range(1, W - 1):
            for y in range(1, H - 1):
                if current_state[y][x]:
                    pygame.draw.rect(
                        surface,
                        pygame.Color("black"),
                        (x * TILE + 2,
                         y * TILE + 2,
                         TILE - 2,
                         TILE - 2),
                    )
                next_state[y][x] = cell_check(current_state, x, y)

        current_state = deepcopy(next_state)

        pygame.display.set_caption('The Game of Life')
        pygame.display.flip()
        print(f"FPS for Generation {gen}: {clock.get_fps():.5f}")
        gen += 1
        clock.tick(FPS)
