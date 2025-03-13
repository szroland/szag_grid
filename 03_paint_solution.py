from grid import *
from pygame.rect import Rect
'''
https://pygame-zero.readthedocs.io/en/latest/colors_ref.html
'''
colors = ["indianred", "greenyellow", "peru", "lemonchiffon", "seagreen", "deepskyblue"]
color = 0

grid = Grid(100, 200, 4)
position = Position(grid.rows//2, grid.cols//2)

grid[position] = color
line = False

fps = FPS()

def draw0():
    grid.draw()
    #screen.draw.text(f"FPS: {fps.fps} redraw: {grid.redraw} skip={grid.skip}", (20, 100), fontsize=60, color="black")

    screen.draw.filled_rect(Rect(5, 5, 200, 30), "gray")
    screen.draw.text(f"FPS: {fps.fps} redraw: {grid.redraw} skip={grid.skip}", (10, 10),
                        color="black", fontsize=20)

def update():
    fps.update()
    if not line:
        grid[position] = 0
    if keyboard.RETURN:
        grid.reset()

    if keyboard.left:
        position.col = (position.col - 1) % grid.cols
    if keyboard.right:
        position.col = (position.col + 1) % grid.cols
    if keyboard.up:
        position.row = (position.row - 1) % grid.rows
    if keyboard.down:
        position.row = (position.row + 1) % grid.rows
    grid[position] = colors[color]

def on_key_down(key):
    global color, line
    if key == 49:
        color = (color + 1) % len(colors)
    elif key == 50:
        color = (color - 1) % len(colors)
    elif key == 32:
        line = not line


def on_mouse_down(pos, button):
    if button == mouse.LEFT:
        col = pos[0] // grid.cell_size
        row = pos[1] // grid.cell_size

        grid[row][col] = colors[color]

def on_mouse_move(pos, rel, buttons):
    col = pos[0] // grid.cell_size
    row = pos[1] // grid.cell_size
    if mouse.LEFT in buttons:
        grid[row][col] = colors[color]
    if mouse.RIGHT in buttons:
        grid[row][col] = 0

grid.show()