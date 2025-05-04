import math
import time
import random

from grid import Grid, Position

TITLE = "Automatikus mozgás"
grid = Grid(15, 130, 10)

sor = 7
oszlop = 65
sebesseg = 0.2
irany = 1

def akadaly_generalas():
    y_pos = random.randint(0, 129)
    x_pos = random.randint(0, 14)
    grid[x_pos][y_pos] = 2

def update(dt):
    global sor
    global oszlop
    global irany
    grid[sor][int(oszlop)] = 0

    oszlop = (oszlop + (sebesseg * irany)) % 129
    grid[sor][int(oszlop)] = 20

    if random.random() < 0.05:
        akadaly_generalas()

def on_key_down(key):
    global sor
    global oszlop

    from pgzero.constants import keys  

    if key == keys.DOWN:
        if sor + 1 < 15:
            grid[sor][int(oszlop)] = 0
            sor += 1
            grid[sor][int(oszlop)] = 2

    elif key == keys.UP:
        if sor - 1 >= 0:
            grid[sor][int(oszlop)] = 0
            sor -= 1
            grid[sor][int(oszlop)] = 2

    if random.random() < 0.005:
        akadaly_generalas()

grid.show()










