
import sys
import time
import math
import palette

from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
environ['SDL_VIDEO_CENTERED'] = '1'

import pgzero.screen
import pgzero.constants
import pygame
from dataclasses import dataclass

def create_list_of_lists(rows:int, cols:int, value):
    return [[value for _ in range(cols)] for _ in range(rows)]

grid = None

def draw():
    if grid is not None:
        grid.draw()

def on_key_down(key):
    if key == 27: # sys.modules["__main__"].keys.ESCAPE:
        exit()

def get_screen() -> pgzero.screen.Screen:
    return sys.modules["__main__"].screen

screen:pgzero.screen.Screen

BACKGROUND = (220, 220, 220)

class Position:
    def __init__(self, row: int = 0, col: int = 0):
        self.row = row
        self.col = col

    def __iter__(self):
        return iter((self.row, self.col))

    def __repr__(self):
        return f"Position(row={self.row}, col={self.col})"

class Grid:
    def __init__(self, rows: int = 70, cols: int = 120, cell_size: int = 5, init_value = 0, colors = None):
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        if self.cell_size < 1:
            self.cell_size = 1
        self.cell_draw_size = self.cell_size-1
        if self.cell_draw_size < 3:
            self.cell_draw_size = self.cell_size

        self.grid = create_list_of_lists(rows, cols, init_value)
        self.previous_grid = create_list_of_lists(rows, cols, init_value-1)
        self.init_value = init_value

        self.first_draw = True
        self.redraw = 0
        self.skip = 0
        self.colors = colors if colors is not None else [BACKGROUND] + palette.generate_neon_palette(max(cols, rows))

        global grid
        grid = self

    def __getitem__(self, key) -> list:
        if isinstance(key, Position):
            return self.grid[key.row][key.col]
        return self.grid[key]

    def __setitem__(self, key, value):
        if isinstance(key, Position):
            self.grid[key.row][key.col] = value
        elif isinstance(key, int):
            if not isinstance(value, list) or len(value) != self.cols:
                raise ValueError("Row assignment must be a list of correct length")
            self.grid[key] = value
        else:
            raise TypeError(f"Invalid index type: {type(key)}")

    def reset(self):
        v = self.init_value
        r = v-1
        for r in range(self.rows):
            for c in range(self.cols):
                self.grid[r][c] = v
                self.previous_grid[r][c] = r

    def force_redraw(self):
        for r in range(self.rows):
            for c in range(self.cols):
                self.previous_grid[r][c] = -1

    def draw(self):
        screen = get_screen()
        if self.first_draw:
            screen.fill((255, 255, 255))
            self.first_draw = False

        redraw = 0
        skip = 0
        for y in range(self.rows):
            for x in range(self.cols):
                c = self.grid[y][x]
                p = self.previous_grid[y][x]
                if c != p:

                    if isinstance(c, int):
                        if c == 0:
                            color_used = self.colors[0]
                        else:
                            color_used = self.colors[1 + (c-1) % (len(self.colors)-1)]
                    else:
                        color_used = c

                    screen.draw.filled_rect(
                        pygame.Rect(
                            (x * self.cell_size, y * self.cell_size),
                            (self.cell_draw_size, self.cell_draw_size)
                        ),
                        color=color_used
                    )
                    redraw = redraw+1
                    self.redraw = redraw
                    self.previous_grid[y][x] = c
                else:
                    skip = skip+1


    def show(self):
        task_module = sys.modules["__main__"]

        if not hasattr(task_module, "draw"):
            task_module.draw = draw
        if not hasattr(task_module, "on_key_down"):
            task_module.on_key_down = on_key_down
        if not hasattr(task_module, "WIDTH"):
            task_module.WIDTH = max(self.cell_size * self.cols, 100)
        if not hasattr(task_module, "HEIGHT"):
            task_module.HEIGHT = max(self.cell_size * self.rows, 100)
        if not hasattr(task_module, "TITLE"):
            task_module.TITLE = "Grid"
        if not hasattr(task_module, "ICON"):
            task_module.ICON = "ikon.png"

        import pgzrun
        pgz_module = sys.modules["__main__"]
        pgzrun.go()

class FPS:
    def __init__(self):
        self.sec = math.floor(time.time())
        self.fps = 0
        self.count = 0

    def update(self):
        s = math.floor(time.time())
        if self.sec != s:
            self.fps = self.count
            self.sec = s
            self.count = 1
        else:
            self.count = self.count+1


class Timer:
    def __init__(self, interval:float):
        self.interval = interval
        self.dt = 0.0

    def passed(self, dt:float) -> bool:
        self.dt = self.dt + dt
        result = self.dt > self.interval
        if result:
            self.dt -= self.interval
        return result

@dataclass
class KeyboardHelper:
    RETURN: bool
    esc: bool
    left: bool
    right: bool
    up: bool
    down: bool
    space: bool

keyboard:KeyboardHelper

@dataclass
class KeysHelper:
    LEFT: bool
    RIGHT: bool
    UP: bool
    DOWN: bool
    RETURN: bool
    A: bool
    B: bool
    C: bool
    D: bool
    E: bool
    F: bool

keys: KeysHelper

@dataclass
class MouseHelper:
    LEFT:bool
    RIGHT:bool
    UP:bool
    DOWN:bool

mouse:MouseHelper

