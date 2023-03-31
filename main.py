"""
An implementation of Conway's Game of Life using pygame.
rules:
    1. Any live cell with fewer than two live neighbours dies: underpopulation.
    2. Any live cell with two or three live neighbours lives on to the next generation.
    3. Any live cell with more than three live neighbours dies: overpopulation.
    4. Any dead cell with exactly three live neighbours becomes a live cell: reproduction.

Author: J-A-Collins
    """

# Imports
import pygame
from copy import deepcopy
from random import randint


class GameOfLife:
    """class for the game of life simulation
    :param width: width of the window
    :param height: height of the window
    :param tile: size of the tiles
    :param fps: frames per second
    """

    def __init__(self, width, height, tile, fps):
        self.width = width
        self.height = height
        self.tile = tile
        self.w = self.width // self.tile
        self.h = self.height // self.tile
        self.fps = fps
        self.current_state = [
            [randint(0, 1) for i in range(self.w)] for j in range(self.h)
        ]
        self.next_state = [[0 for i in range(self.w)] for j in range(self.h)]

    def cell_check(self, x, y):
        """checks the state of the cell
        :param x: x coordinate of the cell
        :param y: y coordinate of the cell
        :return: 1 if the cell is alive, 0 if the cell is dead
        """
        count = sum(
            self.current_state[j % self.h][i % self.w]
            for j in range(y - 1, y + 2)
            for i in range(x - 1, x + 2)
        )
        count -= self.current_state[y][x]
        return 1 if (count == 3) or (count == 2 and self.current_state[y][x]) else 0

    def draw_grid(self, surface):
        """draws the grid on the screen"""
        for x in range(0, self.width, self.tile):
            pygame.draw.line(surface, pygame.Color("black"), (x, 0), (x, self.height))
        for y in range(0, self.height, self.tile):
            pygame.draw.line(surface, pygame.Color("black"), (0, y), (self.width, y))

    def draw_cells(self, surface):
        """draws the cells on the screen"""
        for x in range(1, self.w - 1):
            for y in range(1, self.h - 1):
                cell_color = pygame.Color("black") if self.current_state[y][x] else pygame.Color("white")
                pygame.draw.rect(surface, cell_color, (x * self.tile + 2, y * self.tile + 2, self.tile - 2, self.tile - 2))
                self.next_state[y][x] = self.cell_check(x, y)

    def update(self):
        """updates the current state of the game"""
        self.current_state = deepcopy(self.next_state)

    def run(self):
        """runs the game of life simulation"""
        pygame.init()
        surface = pygame.display.set_mode((self.width, self.height))
        clock = pygame.time.Clock()

        pygame.display.set_caption("The Game of Life")

        gen = 0
        while True:
            surface.fill(pygame.Color("white"))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            self.draw_grid(surface)
            self.draw_cells(surface)
            self.update()

            pygame.display.set_caption(f"The Game of Life - Generation {gen}")
            pygame.display.flip()
            print(f"FPS for Generation {gen}: {clock.get_fps():.5f}")
            gen += 1
            clock.tick(self.fps)


if __name__ == "__main__":
    game_of_life = GameOfLife(width=450, height=450, tile=15, fps=10)
    game_of_life.run()
