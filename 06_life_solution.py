import math

import pgzero.clock

from grid import *
from random import random
from palette import *

TITLE = "Game of Life"
ICON = "ikon.png"
Grid()
grid = Grid(60, 70, 7 )

fill_ratio = 0.25
running = True

def load_txt_pattern(filename):
    g = []
    max_c = 0
    try:
        with open(filename, "r") as file:
            for row_idx, line in enumerate(file):
                max_c = max(max_c, len(line.strip()))
                row = []
                for char in line.strip():
                    row.append(1 if char != '.' else 0)
                g.append(row)
    except FileNotFoundError:
        pass

    dr = max(0, grid.rows - len(g)) // 2
    dc = max(0, grid.cols - max_c) // 2
    for r in range(len(g)):
        for c in range(len(g[r])):
            grid[r+dr][c+dc] = g[r][c]

filename = sys.argv[1] if len(sys.argv) > 1 else None
if filename:
    print(f"Betöltés: {filename}")
    load_txt_pattern(filename)
    running = False
else:
    for sor in range(grid.rows):
        for oszlop in range(grid.cols):
            if random() < fill_ratio:
                grid[sor][oszlop] = 1 #randint(1, len(COLORS)-1)


def szomszedok(r, c):
    s = 0
    for dr in range(-1, 2):
        for dc in range(-1, 2):
            if dr != 0 or dc != 0:
                rr = r + dr
                cc = c + dc
                if 0 <= rr < grid.rows and 0 <= cc < grid.cols and grid[rr][cc] != 0:
                    s = s+1
    return s

timer = Timer(0.1)

def update(dt):
    if running:# and timer.passed(dt):
        lep()

def szin(r, c):
    sr, sc = grid.rows//2, grid.cols//2
    distance = abs(r - sr) + abs(c - sc)
    return 1+2*int(distance / (sr+sc) * max(grid.rows, grid.cols))

def lep():
    next_grid = create_list_of_lists(grid.rows, grid.cols, 0)
    for r in range(grid.rows):
        for c in range(grid.cols):
            s = szomszedok(r,c)
            if s == 3 or grid[r][c] != 0 and s == 2:
                if grid[r][c] == 0:
                    next_grid[r][c] = szin(r, c)
                else:
                    next_grid[r][c] = szin(r, c)

    grid.grid = next_grid

def on_mouse_move(pos, rel, buttons):
    col = pos[0] // grid.cell_size
    row = pos[1] // grid.cell_size
    if 0 <= col < grid.cols and 0 <= row < grid.rows:
        if mouse.LEFT in buttons:
            grid[row][col] = 1
        if mouse.RIGHT in buttons:
            grid[row][col] = 0

def on_mouse_down(pos, button):
    col = pos[0] // grid.cell_size
    row = pos[1] // grid.cell_size
    if 0 <= col < grid.cols and 0 <= row < grid.rows:
        if mouse.LEFT == button:
            grid[row][col] = 1
        if mouse.RIGHT == button:
            grid[row][col] = 0

def on_key_down(key):
    global running
    if key == 32:
        running = not running
    if key == 13:
        grid.reset()
        running = False
    if key == keys.LEFT or key == keys.RIGHT or key == keys.F:
        lep()


grid.show()