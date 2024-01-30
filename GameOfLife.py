import numpy as np
import os
import time

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
    neighbors = grid[max(0, row-1):min(row+2, grid.shape[0]), max(0, col-1):min(col+2, grid.shape[1])]
    return np.sum(neighbors) - grid[row][col]

def update_grid(grid):
    """Update the grid for the next generation."""
    new_grid = np.copy(grid)
    rows, cols = grid.shape

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
