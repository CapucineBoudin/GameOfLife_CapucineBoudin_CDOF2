import numpy as np
import os
import time
import random

def create_grid(rows, cols):
    """Create a new grid of the given size."""
    return np.random.choice([0, 1], size=(rows, cols))

def draw_grid(grid):
    """Draw the grid to the console."""
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in grid:
        print(' '.join(['█' if cell else ' ' for cell in row]))

def count_neighbors(grid, row, col):
    """Count the number of live neighbors around the given cell."""
    rows, cols = len(grid), len(grid[0])
    count = 0
    for i in range(max(0, row-1), min(rows, row+2)):
        for j in range(max(0, col-1), min(cols, col+2)):
            if (i, j) != (row, col):
                count += grid[i][j]
    return count

def update_grid(grid):
    """Update the grid for the next generation."""
    new_grid = np.copy(grid)
    rows, cols = len(grid), len(grid[0])

    for row in range(rows):
        for col in range(cols):
            neighbors = count_neighbors(grid, row, col)
            if grid[row][col] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_grid[row][col] = 0
            elif neighbors == 3:
                new_grid[row][col] = 1
    return new_grid

def game_of_life(rows=20, cols=20, delay=0.5):
    """Run Conway's Game of Life."""
    grid = create_grid(rows, cols)

    try:
        while True:
            draw_grid(grid)
            grid = update_grid(grid)
            time.sleep(delay)
    except KeyboardInterrupt:
        print("Game of Life terminated.")

if __name__ == '__main__':
    game_of_life()
