import numpy as np
import os
import time
import tkinter as tk

#global variable to interrupt the loop
loop = True

def create_grid(rows, cols):
    """Create a new grid of the given size."""
    return np.random.choice([0, 1], size=(rows, cols))

def draw_grid(grid, canvas, tileSize):
    """Draw the grid on the window"""
    rows, cols = len(grid), len(grid[0])
    canvas.delete('all')
    for row in range(rows):
        for col in range(cols):
            color = 'black' if grid[row][col] else 'white'
            canvas.create_rectangle(col*tileSize, row*tileSize, (col+1)*tileSize, (row+1)*tileSize, outline=color, fill=color)

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

def next_generation(window, canvas, grid, tileSize):
    draw_grid(grid, canvas, tileSize)
    new_grid = update_grid(grid)
    grid[:] = new_grid
    if loop:
        window.after(500, lambda:next_generation(window, canvas, grid, tileSize))

def stopLoop(event):
    global loop
    loop=False

def game_of_life(rows=20, cols=20, tileSize=10):
    """Run Conway's Game of Life."""
    window = tk.Tk()
    window.geometry("+0+0")
    canvas = tk.Canvas(window, width=cols*tileSize, height=rows*tileSize)
    canvas.pack()
    grid = create_grid(rows, cols)
    next_generation(window, canvas, grid, tileSize)
    window.bind('<Key>', stopLoop)
    tk.Label(window, text="Press a key to stop").pack()
    window.mainloop()

if __name__ == '__main__':
    game_of_life()