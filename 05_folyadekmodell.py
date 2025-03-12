from grid import *
from random import random, randint


'''
A folyadék modell nagyon hasonlít a gázra.
Annyit kell rajta módosítani, hogy a folyadék részecskéi ragaszkodjanak egymáshoz: nem mozognak akárhova.
Egy új helyre csak akkor mennek át, ha ezzel nem csökken a szomszédjainak a száma.
'''
TITLE = "Folyadék modell szimuláció"
ICON = "ikon.png"

grid = Grid(50, 80, 8)
grid.cell_draw_size = grid.cell_size

fill_ratio = 0.5


'''
Ezt valószínűleg átvehetjük a gáz modelltől
'''
def update():
    pass

'''
Ezt is valószínűleg átvehetjük a gáz modelltől.
De fontos módosítás:

✅ 1. feladat: mozgás
A folyadék részecske tapadós: üres helyre csak akkor mozog, ha az új helyen legalább annyi szomszédja van, mint
amennyi előtte volt. Ha a véletlenül  kiválasztott irányra ez nem teljesül, akkor nem mozog. 

szomszedok(regi) <= szomszedok(uj)

✅ 2. feladat: gravitáció
A gravitációt úgy tudjuk figyelembe venni, hogy ha a szomszéd számok összevetésénél alkalmazunk egy kompenzáló
tényezőt, ami a függőleges változás irányából számítódik ki egy "gravitációs" paraméter segítségével

fuggo_valtozas = uj.sor - regi.sor
szomszédok(regi) + G * fuggo_valtozas <= szomszedok(uj)

Ha G=0, visszakapjuk az alap modellt gravitáció nélkül. A pozitív és negatív G értékek a fölfelé és lefelé mozgást segítik.
'''

def lep():
    # ❓ véletlen választás, majd lépés, ha a szomszedszam megengedi
    pass

'''
✅ 3. (szorgalmi) feladat: egérrel lehessen folyadék molekulákat létrehozni, vagy eltüntetni
'''
def on_mouse_move(pos, rel, buttons):
    if mouse.LEFT in buttons:
        pass #letrehoz
    if mouse.RIGHT in buttons:
        pass #eltuntet

grid.show()