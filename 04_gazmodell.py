from grid import *
from random import random, randint

'''
Gázokat fogunk szimulálni. A gáz kitölti a teret és véletlen szerűen mozog.
A gravitáció hat rá, nagyobb valószínűséggel mozog lefelé, de nem csak lefelé tud menni.
'''
TITLE = "Gáz modell szimuláció"
ICON = "ikon.png"

grid = Grid()

fill_ratio = 0.2

'''
✅ 1. feladat
Töltsük ki a teret "gázzal". Az egyes cellákba véletlen szerűen a fill_ration paraméternek megfelelő
valószínűséggel kerül valamilyen gáz (nem 0 érték vagy szín), vagy marad üres
'''

# ❓ grid[0][0] = 1 ❓


'''
✅ 2. feladat: mozgás
Mozogjon a gáz: minden lépésben válaszzunk egy cellát, illetve annak a szomszédját, majd cseréljük meg a benne levő
dolgokat.

✅ 3. feladat: gyorsabb szimuláció
Nagyon sok lépést kell szimulálni, hogy látványos legyen a mozgás. Az update függvény minden hívásakor végezzünk 
több 100 vagy több ezer szimulációs lépést

✅ 4. feladat: diffúzió
Induljunk ki két, nem egyenletesen elhelyezkedő gázzal. Hosszú távon igaz az, hogy a gáz kitölti a teret és 
egyenletesen oszlik el akkor is, ha kezdetben pl. az "edény" két oldalán volt a két különbözö gáz?

✅ 5. feladat: gravitáció
Most a véletlen választásnál csak gáz molekulát válasszunk, a cél helynek pedig p valószínűséggel fölötte, 1-p
valószínűséggel alatta levő pozíciót. A p paraméterrel mi módosul? Modellezi ez a gravitációt?

'''
def update():
    lep()

def lep():
    #❓ véletlen választás, majd lépés
    pass

# megjelenítés indítása
grid.show()