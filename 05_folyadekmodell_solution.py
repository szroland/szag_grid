from grid import *
from random import random, randint

TITLE = "Folyadék modell szimuláció"
ICON = "ikon.png"

grid = Grid(50, 80, 8)
grid.colors = [BACKGROUND] + palette.generate_warm_palette(5)
grid.cell_draw_size = grid.cell_size

fill_ratio = 0.5
G = 2

for sor in range(grid.rows):
    for oszlop in range(grid.cols):
        if random() < fill_ratio:
            grid[sor][oszlop] = 1 #randint(1, len(COLORS)-1)

#for sor in range(grid.rows//2):
#    for oszlop in range(grid.cols):
#             grid[sor][oszlop] = 1 #randint(1, len(COLORS)-1)

def veletlen_irany(pn, pp):
    r = random()
    if r < pn:
        return -1
    if r >= 1 - pp:
        return 1
    return 0

def veletlen_fel(p):
    r = random()
    if r < p:
        return -1
    return 1

def szomszedok(r, c):
    s = 0
    for dr in range(-1, 2):
        for dc in range(-1, 2):
            rr = r + dr
            cc = c + dc
            if 0 <= rr < grid.rows and 0 <= cc < grid.cols and grid[rr][cc] != 0:
                s = s+1
    return s

def update():
    for _ in range(10000):
        lep()
    color_fix()

def color_fix():
    for r in range(grid.rows):
        for c in range(grid.cols):
            if grid[r][c] != 0:
                grid[r][c] = szomszedok(r, c)

def lep():
    s = randint(0,grid.rows-1)
    o = randint(0,grid.cols-1)
    if grid[s][o] == 0:
        return

    p = 0.5
    if grid[s][o]==1:
        p = 0.45

    #ds = veletlen_irany(0.2, 0.5)
    ds = randint(-1, 1)
    do = randint(-1, 1)

    ns = s + ds
    no = o + do

    dh = s - ns
    if 0 <= ns < grid.rows and 0 <= no < grid.cols and grid[ns][no] == 0 and szomszedok(s, o) + G*dh <= szomszedok(ns, no):
        grid[ns][no] = szomszedok(ns, no)
        grid[s][o] = 0


def on_mouse_move(pos, rel, buttons):
    col = pos[0] // grid.cell_size
    row = pos[1] // grid.cell_size
    if 0 <= col < grid.cols and 0 <= row < grid.rows:
        if mouse.LEFT in buttons:
            grid[row][col] = 1
        if mouse.RIGHT in buttons:
            grid[row][col] = 0


grid.show()