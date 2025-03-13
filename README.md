# Előkészítés

## PyCharm konfigurálása

A projekt betöltésekor a PyCharm automatikusan választ egy környezetet, ha volt már ilyen 
beállítva korábban, vagy pedig egy dialógusban felajánlja egyből a megfelelő Python
környezet kiválasztását.

A környezetet utólag is módosíthatjuk:

`File` > `Settings` > `Project <név>` > `Python Interpreter`
(`Ctrl`+`Alt`+`S`)

Ellenőrizzük, hogy legyen kiválasztva Python Interpreter, és hogy a kiválasztott környezet a
C meghajtón van (Hálózati meghajtó, pl. a H: nem működik jól az iskolai hálózatban). 

Ha nincs megfelelő környezet, akkor létre kell hozni egyet.

## Új Python környezet létrehozása

1. Válasszuk az `Add Interpreter` > `Add Local Interpreter` opciót!
2. Environment: `Generate new`
3. Type: `Virtualenv`
4. Base python: válasszuk az elérhető legújabb Python-t
5. Location: **itt nagyon fontos, hogy a C: meghajtón levő helyet adjunk meg**
A legkönnyebb, ha a `mappa` ikonra kattintunk, majd az első, `házikó` ikonnal
megnyitjuk a Home könyvtárunkat, és itt hozunk létre egy új mappát pl. `venv`
néven.
6. Végül kattintsunk az OK-ra, ekkor létrejön a környezet

## Python csomagok telepítése

Ehhez a projekthez legalább a **pgzero** csomag telepítése szükséges, ezeket a függőségeket a 
requirements.txt tartalmazza, amit a PyCharm felismer. Bármelyik python fájl megnyitása után
a szerkesztő tetején megjelenik egy sárga sáv, benne egy gomb: `Install requirements`

A bal gomb sorban a `Python Packages` gomb alatt ellenőrizhetjük, hogy milyen csomagok 
vannak telepítve.

## Manuális telepítés (csak szükség esetén)

Ha valamiért a PyCharm nem telepíti a függőségeket, de egyébként biztosak vagyunk benne, hogy 
a virtuális környezet megfelelően létrejött, kézzel is telepíthetjük a függőségeket. 

Ehhez a bal oldali gombsor Terminal gombjával nyithatjuk meg a parancssori terminált. 
Fontos, hogy a virtuális python környezet aktiválva legyen, ez, ha minden jól van beállítva, 
automatikusan megtörténik. Ha nem, akkor a virtuális környezet könyvtárában futtassuk a 
`Scripts\activate` szkriptet. Ezután már telepíthetjük a csomagokat a környezetbe:
```
pip install -r requirements.txt
```
# Linkek

## Python
* [Python Cheet Sheet 1](https://quickref.me/python.html)
* [Python Cheat Sheet 2](https://www.pythoncheatsheet.org/)
* [Python for Data Science Cheat Sheet](https://www.utc.fr/~jlaforet/Suppl/python-cheatsheets.pdf)

## PyGameZero
* [Eseménykezelő függvények](https://pygame-zero.readthedocs.io/en/latest/hooks.html)
* [Beépített objektumok](https://pygame-zero.readthedocs.io/en/latest/builtins.html)
* [Színlista](https://pygame-zero.readthedocs.io/en/latest/colors_ref.html)

## Game of life
* [Game of life wiki](https://conwaylife.com/)
* [Glider gun](https://conwaylife.com/wiki/Glider_gun)

## Modellezés és szimuláció
* [ELTE egyetemi jegyzet](https://tantargy4.elte.hu/downloads/scorm/index.html)

## PyCharm
* [Virtuális környezet beállításai](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html)