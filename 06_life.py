import pgzero.clock

from grid import *
from random import random, randint

'''
Az élet játéka egy képzeletbeli populációt szimulál és egyszerű szabályai ellenére érdekes és komplex működést
eredményezhet (pl. számítógépet lehet építeni belőle, ami képes "programot" futtatni).

A szabályok egyszerűek. A szimuláció minden egyes lépése egy új táblázatot tölt ki a régi alapján.

Az új táblázatban akkor "él" egy cella, ha:
 * a régi táblázatban, a szimuláció előző állapotában, 3 szomszédja volt, vagy
 * ha csak 2 szomszédja volt, de ő maga élt az előző állapotban
 
Fontos, hogy a szomszédok számolásánál az eredei állapotot vegyük figyelembe. Emiatt nem lehet a táblázatot 
helyben frissíteni, hiszen a későbbi cellák szomszéd számai megváltoznának.

Szintén fontos, hogy egy cellának max 8 szomszédja lehet, önmagát nem számítjuk szomszédnak.
'''

TITLE = "Game of Life"
ICON = "ikon.png"

grid = Grid(105, 105, 7)

fill_ratio = 0.6
'''
✅ 1. feladat
Töltsük ki a teret véletlenszerűen, a fill_ratio paraméter alapján
'''


running = True

'''
✅ 2. feladat: futassuk a szimulációt
(Ha lassítani szeretnénk, akkor van egy Timer osztály a grid.py-ban erre, de magunktól is megoldhatjuk)
'''
def update(dt):
    lep()

def lep():
    #új két dimenziós tömb, a következő állapot kiszámolásához
    next_grid = create_list_of_lists(grid.rows, grid.cols, 0)

    #... itt  valami történik...


    #frissítjük a táblázatot
    grid.grid = next_grid

'''
✅ 3. feladat: szimuláció megállítása
SPACE gombbal álljon meg a szimuláció, újabb SPACE gombbal folytatódjun
ENTER billentyűre (13) törlődjön a grid összes cellája és álljon le a szimuláció, hogy szerkeszteni lehessen
'''
def on_key_down(key):
    if key == 32:
        pass
    if key == 13:
        pass
'''
✅ 4. feladat: cellák létrehozása és törlés egérrel
'''
def on_mouse_move(pos, rel, buttons):
    pass #egér mozog

def on_mouse_down(pos, button):
    pass #egér kattint

'''
✅ 5. feladat: állapot betöltése fájlból (pl. life alkönyvtár)
'''
filename = sys.argv[1] if len(sys.argv) > 1 else None
if filename:
    #van paraméter, töltsük be a megfelelő fájl taralmát
    pass
else:
    #nincs paraméter, marad a véletlenszerű kitöltés
    pass




grid.show()