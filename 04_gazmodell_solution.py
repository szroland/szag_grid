from grid import *
from random import random, randint

TITLE = "Gáz modell szimuláció"
ICON = "ikon.png"

grid = Grid(70, 120, 10)
grid.colors = [BACKGROUND, ]

fill_ratio = 0.2

for sor in range(grid.rows):
    for oszlop in range(grid.cols):
        if random() < fill_ratio:
            grid[sor][oszlop] = randint(1, len(grid.colors)-1)

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


def update():
    for _ in range(10000):
        lep()

def lep():
    s = randint(0,grid.rows-1)
    o = randint(0,grid.cols-1)
    if grid[s][o] == 0:
        return

    p = 0.5
    if grid[s][o]==1:
        p = 0.45

    #ds = veletlen_irany(0.2, 0.5)
    ds = veletlen_fel(p)
    do = randint(-1, 1)

    ns = s + ds
    no = o + do

    if 0 <= ns < grid.rows and 0 <= no < grid.cols:
        tmp = grid[ns][no]
        grid[ns][no] = grid[s][o]
        grid[s][o] = tmp

grid.show()