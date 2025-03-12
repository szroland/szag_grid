import math
from math import sin, cos, floor
import time
import random

from grid import Grid, Position

'''
Most nem csak statikus állapotot akarunk megjeleníteni, azt szeretnénk, ha a felület változna
Először létrehozunk egy grid-et a szokásos módon. A program utolsó sorában ezt jelenítjük meg 
a grid.show() hívással.
'''
TITLE = "Automatikus mozgás"
grid = Grid(150, 150, 5)


'''
A keretrendszer rendszeresen hívja az update nevű függvényt, egyeten opcionális paramétere van, amiben
megkapjuk a legutóbbi hívás óta eltelt időt. Ha elég gyors a program, akkor ez másodpercenként 60x történik,
de ha sokat számolunk, akkor lassabb lesz a frissítés.

✅ Első feladat:

Rajzoljunk ki egy pixelt, és az mozogjon folyamatosan valamilyen irányba (pl. vízszintesen, átlósan, 
szinusz hullámban, stb.)
A grid méreteit fentről leolvshatjuk, vagy a grid.rows (sorok száma) és a grid.cols (oszlopok száma) tartalmazza.
'''
def update(dt):
    #❓ Mi jön ide, hogy mozogjon a pixel a képen ❓
    pass

'''
A keretrendszer ún. callback függvényben értesít minket különböző eseményekről, pl. ha a felhasználó lenyomott
egy gombot, vagy kattintott az egérrel.

Az on_key_down akkor hívódik, amikor egy gombot lenyomnak, paraméterében pedig megkapja a lenyomott gomb kódját.
A SPACE gomb kódja pl. 32

✅ Második feladat
Az eseménykezelő segítségével érjük el, hogy az eddigi mozgás megfoduljon, visszafelé haladjon a pixel. Ehhez persze
az update függvényt is változtatnunk kell majd...
'''
def on_key_down(key):
    if key == 32:
        #❓ valamit tenni kellene, ha lenyomja a space-t...
        pass;

'''
Biztos nagyon érdekes mozgást találtál ki.
Lentebb van néhány paraméteres görbe pálya, ami, ha paraméterként megadod neki az eltelt időt (a mozgás fázisát),
akkor visszaad neked egy pozíciót (Position típus).

A visszaadott pozíciót felhasználhatod a gridben, pl.:
t = ... # eltelt idő
pos = circle(t)
grid[pos] = 1

Ez a t időhöz megfelelő pozíciót 1-re állítja...

✅ Harmadik feladat:
Módosítsd az update függvényt, hogy a lenti paraméteres függvényeket használja.
Az eredeti pályát saját függvénybe átrakhatod.

⛏️ Negyedik feladat (szorgalmi):
Ne csak a legutolsó pont látszódjon. Oldd meg, hogy az előző 10, 50, vagy 100 pozíciót is mutassa a program,
mintha egy kígyó mozogna a pályán.

⛏️ Ötödik feladat (szorgalmi):
Biztos ismered a Snake című játékot...
'''
def line(t: float, speed: float = 0.2, randomness: float = 0) -> Position:
    x = 2*(speed*t - math.floor(speed*t)) - 1
    y = random.uniform(-randomness, randomness)
    return grid_position(x,y)


def circle(phase: float, speed: float = 2.0) -> Position:
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

def grid_position(x, y) -> Position:
    return Position(
        floor(grid.rows / 2 + y * grid.rows * 0.5) % grid.rows,
        floor(grid.cols / 2 + x * grid.cols * 0.5) % grid.cols,
    )

#szokásos utolsó sor: a megjelenítés elindítása
grid.show()
#ide pedig már nem jutunk el soha




