#grid.py tartalmazza a megjelenítést végző kódot
from grid import *

'''
Minden feladat elején létre kell hozni egy táblázatot, megadva a sorok és oszlopok számát,
valamint a megjelnítéskor használt cella méretet

A következő sor egy 25x25-ös táblázatot fog létrehozni, és 20 pixel nagyságú négyzetekkel fogja kirajzolni
'''
grid = Grid(25, 25, 20)

#az ablak címét testre lehet szabni
TITLE = "Alakzatok"

'''
A táblázat minden cellája alapból 0, ami hátérszínnel jelenik meg (üres).
A cellákba többféle dolgot is írhatunk, amivel a színét módosítani tudjuk.

* egész szám: a grid.colors színlista megfelelő indexű elemét használja majd színként 
              (vagy feketét, ha nincs elég szín a listában)
* szín neve szövegesen: (link a readme-ben a színlistához)
* szín kódja: (r, g, b) hármas            
'''
grid[4][8] = 1
grid[8][2] = "darkgreen"
grid[12][18] = (255, 128, 0)

'''
Feladat: ciklusok segítségével színezzük ki a táblázat mezőit. Az egyes színezések kerüljenek külön függvénybe!
    1. ✅ egy adott sor legyen egy színű
    2. ✅ egyik átló egyik szín, másik átló másik szín
    3. ✅ a négy lehetséges háromszög (hozzá tartozó átlóval)
    4. ⛏️ két átló adott színnel, keret másik színnel
    5. ⛏️ Próbáld átméretezni a grid-et, működnek továbbra is a függvényeid?

A feladat megoldása előtt kommentezd ki nyugodtan a fenti 3 cella szinezését, az csak mintaképp volt ott.
A táblázat méretét a grid.rows (sorok száma) és a grid.cols (oszlopok száma) is tartalmazza.
'''

def sor_szinez(sor, szin):
    #❓ mi jön ide ❓
    pass;

sor_szinez(5, 'darkgreen')
sor_szinez(15, 'goldenrod')

'''
☢️ ez legyen mindig az utolsó hívás: a megjelenítés elindítása
ez a függvény soha nem tér vissza, a megjelenítő program a megfelelő nevű függvényeket fogja hívni
'''
grid.show()
# ide már nem jut el a program