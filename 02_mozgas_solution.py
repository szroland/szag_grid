import math
from math import sin, cos, floor
import time
import random

from grid import Grid, Position

TITLE = "Automatikus mozgás"


grid = Grid(150, 150, 5)

dir = 1
phase = 0

tail = []
tail_len = 200

def grid_position(x, y) -> Position:
    return Position(
        floor(grid.rows / 2 + y * grid.rows * 0.5) % grid.rows,
        floor(grid.cols / 2 + x * grid.cols * 0.5) % grid.cols,
    )

def line(t: float, speed: float = 0.2, randomness: float = 0) -> Position:
    x = 2*(speed*t - math.floor(speed*t)) - 1
    y = random.uniform(-randomness, randomness)
    return grid_position(x,y)


def circle(t: float, speed: float = 2.0) -> Position:
    x = cos(phase * speed)
    y = sin(phase * speed)
    return grid_position(x,y)

def flower(phase: float, factor: float = 5.0):
    x = cos(phase * factor) * sin(phase)
    y = sin(phase * factor) * cos(phase)

    return grid_position(x,y)

def heart(phase: float) -> Position:
    x = (16 * sin(phase) ** 3)/16
    y = -(13 * cos(phase) - 5 * cos(2 * phase) - 2 * cos(3 * phase) - cos(4 * phase))/15 - 0.15
    return grid_position(x,y)

def crazy(phase: float) -> Position:
    t = time.time() / 6.28
    rand_factor_x = 0.7 + 0.3 * sin(t) * random.uniform(0.9, 1.1)
    rand_factor_y = 0.7 + 0.3 * cos(t) * random.uniform(0.9, 1.1)

    # The base equation for the shape with sinusoidal components
    x = rand_factor_x * (1.0 * sin(phase) + 0.6 * cos(2 * phase) + 0.4 * cos(3 * phase) )
    y = rand_factor_y * (1.0 * cos(phase) + 0.6 * sin(2 * phase) + 0.4 * sin(3 * phase) )

    return grid_position(x*0.5, y*0.5)

def update(dt):
    if len(tail) > tail_len:
        p = tail.pop(0)
        grid[p] = 0

    global phase
    phase = phase + dir * dt

    pos = heart(0.5* phase)
    grid[pos] = 1+int(phase*10)
    tail.append(pos)

def on_key_down(key):
    global dir
    if key == 32:
        dir = -1 * dir

grid.show()




