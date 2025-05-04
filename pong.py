from grid import Grid
import random

# Játék konfiguráció
CIM = "Pong"

# Pálya méretei
ROWS = 36  # Sorok száma
COLS = 64  # Oszlopok száma
CELL_SIZE = 24  # Cellák mérete

# Színek definíciói
WHITE = (255, 255, 255)  # Fehér
BLACK = (0, 0, 0)  # Fekete
RED = (255, 0, 0)  # Piros
GREEN = (0, 255, 0)  # Zöld
BLUE = (0, 0, 255)  # Kék


class Jatekos:
    def __init__(self, x, y, szin):
        self.x = x
        self.y = y
        self.szin = szin

        self.magassag = 10
        self.szelesseg = 2

    def mozgat(self, y):
        # Ütő mozgatása függőlegesen. Pozitív érték esetén lefelé mozgatja az ütőt, negatív érték esetén felfelé.
        self.y += y

    def rajzol(self, palya):
        for i in range(self.magassag):  # Először végigmegyünk a grid sorain
            if 0 <= int(self.y) + i < ROWS:  # Ellenőrizzük, hogy a sor a pályán belül van-e
                for j in range(self.szelesseg):  # Ezután végigmegyünk a grid oszlopain
                    if 0 <= int(self.x) + j < COLS:  # Ellenőrizzük, hogy az oszlop a pályán belül van-e
                        palya[int(self.y) + i][int(self.x) + j] = self.szin  # Ha mindkettő igaz, akkor kirajzoljuk a cellát


class Labda:
    def __init__(self):
        self.ujrakezd()

    def ujrakezd(self):
        self.x = COLS // 2  # Az középső oszlop
        self.y = ROWS // 2  # Az középső sor
        self.sebesseg_x = random.choice([-0.35, 0.35])  # Véletlenszerű sebesség x irányban
        self.sebesseg_y = random.choice([-0.35, 0.35])  # Véletlenszerű sebesség y irányban

    def mozgat(self):
        # Minden képkockánál egy adott sebességgel mozgatjuk a labdát
        self.x += self.sebesseg_x
        self.y += self.sebesseg_y

        # Ha a labda eléri a pálya szélét, azaz a falakat, akkor visszapattan
        if self.y <= 0 or self.y >= ROWS - 1:
            self.sebesseg_y *= -1

    def rajzol(self, palya):
        for i in range(2):  # A labda két cellányi méretű
            if 0 <= int(self.y) + i - 1 < ROWS:  # Ellenőrizzük, hogy a sor a pályán belül van-e
                for j in range(2):  # Ezután végigmegyünk a grid oszlopain
                    if 0 <= int(self.x) + j - 1 < COLS:  # Ellenőrizzük, hogy az oszlop a pályán belül van-e
                        palya[int(self.y) + i - 1][int(self.x) + j - 1] = GREEN  # Ha mindkettő igaz, akkor kirajzoljuk a cellát


palya = Grid(rows=ROWS, cols=COLS, cell_size=CELL_SIZE)
ellenfel = Jatekos(5, ROWS // 2 - 5, BLUE)  # Bal oldali játékos (ellenfél)
jatekos = Jatekos(COLS - 7, ROWS // 2 - 5, RED)  # Jobb oldali játékos
labda = Labda()  # Mivel a labda automatikusan újrakezdődik, ezért nem szükséges kezdő pozíciót megadni

# A paint_solution.py-hoz hasonló kód, ami az egér mozgását kezeli
def on_mouse_move(pos):
    # Egér mozgás kezelése - játékos ütőjének mozgatása
    _, y = pos
    jatekos.mozgat((y // CELL_SIZE) - (jatekos.y + jatekos.magassag // 2))

# A paint_solution.py-hoz hasonló kód, ami a játék logikáját kezeli
def update():
    # A pálya törlése a következő képkocka előtt
    for sor in range(ROWS):
        for oszlop in range(COLS):
            palya[sor][oszlop] = BLACK

    # Ha a labda az ellenfél ütőjének felezőpontja alatt van, akkor felfelé mozgatjuk az ellenfél ütőjét
    if labda.y < ellenfel.y + ellenfel.magassag // 2:
        ellenfel.mozgat(-1)
    # Ha a labda az ellenfél ütőjének felezőpontja felett van, akkor lefelé mozgatjuk az ellenfél ütőjét
    elif labda.y > ellenfel.y + ellenfel.magassag // 2:
        ellenfel.mozgat(1)

    # Frissítjük a labda pozícióját
    labda.mozgat()

    # Ha a labda már érintkezik az ellenfél ütőjével és az Y pozíciója az ellenfél ütőjének ...
    # alja és teteje között van, akkor a labda visszapattan, azaz a sebesség x iránya megváltozik
    if (labda.x <= ellenfel.x + ellenfel.szelesseg and ellenfel.y <= labda.y <= ellenfel.y + ellenfel.magassag):
        labda.sebesseg_x *= -1

    # Ha a labda már érintkezik a játékos ütőjével és az Y pozíciója a játékos ütőjének ...
    # alja és teteje között van, akkor a labda visszapattan, azaz a sebesség x iránya megváltozik
    if (labda.x >= jatekos.x - 1 and jatekos.y <= labda.y <= jatekos.y + jatekos.magassag):
        labda.sebesseg_x *= -1

    # Ha a labda valamelyik játékos ütőjét elkerülve kiesik a pályáról, akkor a játék újraindul
    if not 0 < labda.x < COLS:
        labda.ujrakezd()

    ellenfel.rajzol(palya)
    jatekos.rajzol(palya)
    labda.rajzol(palya)


palya.show()