import pygame
import sys
import random

# Settings
sorok, oszlopok = 21, 21
#páratlannak kell lennie, hogy a grid széle maradjon fal, minden utat rendesen falak vegyenek körbe
cellaM = 30
szel, hossz = cellaM * sorok, cellaM * oszlopok

# színek
feher = (255, 255, 255)
fekete = (0, 0, 0)
kek = (0, 0, 255)
zold = (0, 255, 0)
szurke = (200, 200, 200)
vil_kek = (125, 249, 255)  # húzott csík

# labirintust generáló visszalépés algoritmus
def lab_gen (sorok, oszlopok):
    lab = [[1 for _ in range(oszlopok)] for _ in range(sorok)]

    def uttores(s, o):
        irany = [(0, 2), (0, -2), (2, 0), (-2, 0)]
        # jobbra, balra, le, fel (2 cellánként, hogy falak is maradjanak)
        random.shuffle(irany)
        # irányok megkeverése
        for ds, do in irany:
            uj_s, uj_o= s + ds, o + do
            # ds = delta s(or) (sorváltás), do = delta o(szlop) (oszlopváltás)
            if 1 <= uj_s < sorok - 1 and 1 <= uj_o < oszlopok - 1:
            # griden belül maradjunk és a széleket se szedjük ki
                if lab[uj_s][uj_o] == 1:
                # ha fal még
                    lab[uj_s][uj_o] = 0
                    # cella "kitörése" (falból út lesz)
                    lab[s + ds // 2][o + do // 2] = 0
                    # út törése mostani és következő cella közt
                    uttores(uj_s, uj_o)
                    # ismétlés az új helyről

    lab[1][1] = 0
    uttores(1, 1)

    # cél jobb alul legyen (fixálva)
    lab[sorok - 2][oszlopok - 2] = 2

    return lab

pygame.init()
kijelzo = pygame.display.set_mode((szel, hossz))
pygame.display.set_caption("Labirintus játék")
ora = pygame.time.Clock()

lab = lab_gen(sorok, oszlopok)
kezdoh = [1, 1]
jatekosh = list(kezdoh)
csik = []

# játékmenet
fut = True
while fut:
    kijelzo.fill(feher)
    # labirintus kirajzolása
    for sor in range(sorok):
        for oszl in range(oszlopok):
            x = oszl * cellaM
            y = sor * cellaM
            cella = lab[sor][oszl]
            if (sor, oszl) in csik:
                pygame.draw.rect(kijelzo, vil_kek, (x, y, cellaM, cellaM))
            elif cella == 1:
                pygame.draw.rect(kijelzo, fekete, (x, y, cellaM, cellaM))
            elif cella == 2:
                pygame.draw.rect(kijelzo, zold, (x, y, cellaM, cellaM))
            else:
                pygame.draw.rect(kijelzo, szurke, (x, y, cellaM, cellaM))
            pygame.draw.rect(kijelzo, feher, (x, y, cellaM, cellaM), 1)
    # játékos kirajzolása
    jx = jatekosh[1] * cellaM
    jy = jatekosh[0] * cellaM
    pygame.draw.rect(kijelzo, kek, (jx, jy, cellaM, cellaM))

    pygame.display.flip()
    ora.tick(60)

    # események
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fut = False

        elif event.type == pygame.KEYDOWN:
            uj_sor, uj_oszl = jatekosh[0], jatekosh[1]

            if event.key == pygame.K_UP:
                uj_sor -= 1
            elif event.key == pygame.K_DOWN:
                uj_sor += 1
            elif event.key== pygame.K_LEFT:
                uj_oszl -= 1
            elif event.key == pygame.K_RIGHT:
                uj_oszl += 1

            if 0 <= uj_sor < sorok and 0 <= uj_oszl < oszlopok:
                if lab[uj_sor][uj_oszl] == 1:
                    jatekosh = list(kezdoh)
                    csik = []
                else:
                    jatekosh = [uj_sor, uj_oszl]
                    if (uj_sor, uj_oszl) not in csik:
                        csik.append((uj_sor, uj_oszl))

                if lab[uj_sor][uj_oszl] == 2:
                    print("Nyertél! 🎉")
                    fut = False

pygame.quit()
sys.exit()
