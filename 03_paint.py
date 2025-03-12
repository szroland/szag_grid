from grid import *
from pygame.rect import Rect
'''
https://pygame-zero.readthedocs.io/en/latest/colors_ref.html
'''

grid = Grid(100, 200, 4)

'''
A feladat az, hogy most a felhasználó tudjon rajzolni.

1. ✅ Nyilakkal tudjon jobbra, balra, le, fel menni
2. ✅ Space-el lehessen beállítani, hogy húzzon vonalat, vagy ne
3. ✅ Egérrel is lehessen rajzolni (vagy egyesével kattintva, vagy húzva)
4. ⛏️ (Opcionális) lehessen színt változtatni
'''

'''
⛏️ Az update() függvény folyamatosan hívódik, és itt le tudjuk ellenőrizni, hogy éppen le van-e nyomva valami 
billentyű vagy egér gomb is akár.
'''
def update():
    if keyboard.RETURN:
        pass #❓ épp nyomja az entert!
    if keyboard.left:
        pass #épp nyomja a balra gombot
    #if keyboard.right: ...

    #❓ ... és valamit meg is kell jelenítsünk


'''
⛏️ Az on_key_down() egyszer hívódik meg, amikor a felhasználó lenyom egy gombot a billentyűzeten
'''
def on_key_down(key):
    if key == 49:
        pass #❓ 1-es gomb lenyomva, jó ez valamire?
    elif key == 50:
        pass #2-es gomb
    elif key == 32:
        pass #❓ SPACE lenyomása

'''
⛏️ Egér kattintás történt
'''
def on_mouse_down(pos, button):
    if button == mouse.LEFT:
        pass #❓ bal gomb

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