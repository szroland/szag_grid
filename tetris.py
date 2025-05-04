from grid import *
from pygame.rect import Rect

TITLE = "Tetris"
grid = Grid(40, 30, 12)


x = 1
y = 1

toll_lent= False

def update():

    global x
    global y
    global toll_lent

    if not toll_lent:
        grid[y][x]=0

    if keyboard.RETURN:
        pass #❓ épp nyomja az entert!
    if keyboard.left:
        x = (x-1) % 30

    if keyboard.right:
        x = (x+1) % 30


    grid[y][x] = 60

def on_key_down(key):
    global y
    if key == 32:
        sor = 39
        while grid[sor][x]!=0:
            sor = sor-1

        grid[sor][x] = 60


'''
⛏️ Egér kattintás történt
'''
def on_mouse_down(pos, button):
    if button == mouse.LEFT:
        pass

'''
⛏️ Mozog az egér
'''
def on_mouse_move(pos, rel, buttons):
    #❓ pos-ban van az egér pozíciója
    #grid.cell_size pedig megadja, mekkora egy cella...

    if mouse.LEFT in buttons:
        pass #❓ mozog az egér és közben a bal gomb nyomva...
    if mouse.RIGHT in buttons:
        pass #❓ mozog az egér és közben a jobb gomb nyomva...

grid.show()
