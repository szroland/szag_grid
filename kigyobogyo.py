import random #random szám generáló könyvtár
from grid import Grid, Position # grid függvény behozása #positions: cella kiszínezése
from pynput import keyboard #billentyűk figyelése
from pynput.keyboard import Key

TITLE = "Snake játék"
grid = Grid(30, 30, 20)

snake = [Position(grid.rows // 2, grid.cols // 2)] #kígyó kezdeti helyzete
direction = Position(0, 1) #merre indul

game_over = False
grow_snake = False
move_delay = 0.2 # ennyi idő telik el 2 lépés között
move_timer = 0.0 # eltelt idő

def spawn_apple():
    while True:
        pos = Position(random.randint(0, grid.rows - 1 ), random.randint(0, grid.cols - 1))  #így nem kell átírni ha a grid változik
        overlap = False #kígyó ne ütközzön az almával
        for s in snake:
            if s.row == pos.row and s.col == pos.col: #ha a kígyó és az alma koordinátái megegyeznek
                overlap = True
                break
        if not overlap:
            return pos

apple = spawn_apple() # itt a spawn apple kimenete belekerül az apple változóba, tehát tudjuk hol van az alma

def update(dt): # a kígyó helyzete frissüljön
    global move_timer, apple, grow_snake, game_over # globális, érték nélküli változók, egyelőre csak definiáljuk őket

    if game_over:
        return

    move_timer += dt #a move timer minden egyes lépésnél 1-el nőjön
    if move_timer < move_delay: # ha az eltelt idő kisebb, mint a két lépés között eltelt idő, akkor ne történjen semmi
        return

    move_timer = 0.0 #kinullázzuk, ha lépünk

    head = snake[-1]
    new_head = Position((head.row + direction.row) % grid.rows,(head.col + direction.col) % grid.cols)
    # új pozíciót számolunk a mozgás irányában (ha túllépünk a pálya szélén, a másik oldalon jelenjen meg )

    for segment in snake:
        if segment.row == new_head.row and segment.col == new_head.col:
            print("Game Over!")
            game_over = True
            return                          #ha önmagába fut, vége

    snake.append(new_head)  #új pozíció a kígyóhoz, az új fej a kígyó végére kerül

    if new_head.row == apple.row and new_head.col == apple.col:
        grow_snake = True
        apple = spawn_apple()
    else:
        if grow_snake:
            grow_snake = False
        else:
            snake.pop(0)  # mindig új fejet kap, ha nem nő, akkor a végéről elvesszük az utolsó blokkot, és egy új fejet kap

    for row in range(grid.rows):
        for col in range(grid.cols):
            grid[Position(row, col)] = 0     #minden cellát kinullázunk a régi állapot törlésével

    for segment in snake:
        grid[segment] = 1      # jelenítsük meg a kígyó minden szegmensét

    grid[apple] = 2 # így jelenik meg az alma

def on_key_release(key):
    global direction, game_over

    if key == Key.right and direction != Position(0, -1): #nem fordulhatunk 180 fokot
        direction = Position(0, 1) #itt jobbra megyek az n. oszlopból az (n+1)-edik oszlopba
    elif key == Key.left and direction != Position(0, 1):
        direction = Position(0, -1) #itt balra megyek az n. oszlopból az (n-1)-edik oszlopba
    elif key == Key.up and direction != Position(1, 0):
        direction = Position(-1, 0)
    elif key == Key.down and direction != Position(-1, 0):
        direction = Position(1, 0)
    elif key == Key.space:
        direction = Position(-direction.row, -direction.col)
    elif key == Key.esc:
        game_over = True
        print("Exciting game")
        exit()

listener = keyboard.Listener(on_release=on_key_release) #billentyűfigyelő
listener.start()

grid.on_update = update # az update függvényt megadjuk
grid.show() #elindítjuk a megjelenítést