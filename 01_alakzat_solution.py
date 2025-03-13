from grid import *

grid = Grid(25, 25, 20)
grid.colors = [BACKGROUND] + palette.generate_neon_palette(10)
def fill1():
    for r in range(grid.rows):
        for c in range(r+1):
            grid[r][c] = 1

def fill(fn):
    for r in range(grid.rows):
        for c in range(grid.cols):
            grid[r][c] = fn(r, c)

def parity(r, c):
    return (r + c) % 2 == 0

def frame_x(r, c):
    s = min(grid.cols, grid.rows)-1
    if r == 0 or r == s or c == 0 or c == s:
        return c+1
    if r == c or r+c == s:
        return r
    return 0


fill(frame_x)


grid.show()

