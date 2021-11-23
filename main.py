import gamelib
import png

ALTO_TABLERO = 20
ANCHO_TABLERO = 20
ANCHO_VENTANA = 700  # x
ALTO_VENTANA = 700  # y
WHITE = 0
BLACK = 1
RED = 2
GREEN = 3
BLUE = 4
CYAN = 5
YELLOW = 6
MAGENTA = 7
COLORES = ("black", "white", "red", "green",
           "blue", "cyan", "yellow", "magenta")


def paint_nuevo(ancho, alto):
    '''inicializa el estado del programa con una imagen vacía de ancho x alto pixels'''
    paint = {}
    paint["numero_color"] = WHITE
    tablero = []
    for i in range(ALTO_TABLERO):
        filas = []
        for j in range(ANCHO_TABLERO):
            filas.append(paint["numero_color"])
        tablero.append(filas)
    
    paint["tablero"] = tablero
    paint["color_str"] = "white"

    return paint

def copiador(paint):
    nuevo_tablero = []
    for i in range(ALTO_TABLERO):
        filas = []
        for j in range(ANCHO_TABLERO):
            filas.append(paint["tablero"][i][j])
        nuevo_tablero.append(filas)

    return nuevo_tablero

def actualizar_juego(paint, x, y):
    nuevo_tablero = copiador(paint)
    
    if x > 50 and x < 650 and y > 45 and y < 645:
        fila = int((x - 50) / 30)
        columna = int((y - 45) / 30)
        nuevo_tablero[fila][columna] = paint["numero_color"]

    paint["tablero"] = nuevo_tablero

def paint_mostrar(paint):
    '''dibuja la interfaz de la aplicación en la ventana'''
    gamelib.draw_begin()
    gamelib.draw_rectangle(0, 0, ANCHO_VENTANA, ALTO_VENTANA, fill="gray")
    pos_inicial_x1 = ANCHO_VENTANA * 7.1428 / 100  # 50
    pos_inicial_y1 = ALTO_VENTANA * 6.4285 / 100  # 45
    pos_inicial_x2 = ANCHO_VENTANA * 11.4285 / 100  # 80
    pos_inicial_y2 = ALTO_VENTANA * 10.7142 / 100  # 75
    for i in range(len(paint["tablero"])):
        for j in range(len(paint["tablero"])):
            gamelib.draw_rectangle(pos_inicial_x1, pos_inicial_y1, pos_inicial_x2, pos_inicial_y2, fill=paint["color_str"])
            pos_inicial_x1 += 30
            pos_inicial_x2 += 30

        pos_inicial_x1 = ANCHO_VENTANA * 7.1428 / 100  # 50
        pos_inicial_x2 = ANCHO_VENTANA * 11.4285 / 100
        pos_inicial_y1 += 30
        pos_inicial_y2 += 30

    pos_inicial_y1 = 195
    pos_inicial_y2 = 225
    indice = 0
    for colores in COLORES:
        gamelib.draw_rectangle(10, pos_inicial_y1, 40,
                               pos_inicial_y2, fill=colores)  # cuadrados
        pos_inicial_y1 += 30
        pos_inicial_y2 += 30
    print(paint["tablero"])
    gamelib.draw_end()

def botones(paint, x, y):
    if x > 10 and x < 40 and y > 200 and y < 230:
        paint["numero_color"] = BLACK
    elif x > 10 and x < 40 and y > 230 and y < 260:
        paint["numero_color"] = WHITE
    elif x > 10 and x < 40 and y > 260 and y < 290:
        paint["numero_color"] = RED 
    elif x > 10 and x < 40 and y > 290 and y < 320:
        paint["numero_color"] = GREEN
    elif x > 10 and x < 40 and y > 320 and y < 350:
        paint["numero_color"] = BLUE 
    elif x > 10 and x < 40 and y > 350 and y < 380:
        paint["numero_color"] = CYAN
    elif x > 10 and x < 40 and y > 380 and y < 410:
        paint["numero_color"] = YELLOW
    elif x > 10 and x < 40 and y > 410 and y < 440:
        paint["numero_color"] = MAGENTA
    else:
        pass 


def main():
    gamelib.title("AlgoPaint")
    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA)

    paint = paint_nuevo(20, 20)

    while gamelib.is_alive():
        paint_mostrar(paint)

        ev = gamelib.wait()
        if not ev:
            break 
        if ev.type == gamelib.EventType.ButtonPress:
            print(f'se ha presionado el botón del mouse: {ev.x} {ev.y}')
            x, y = ev.x, ev.y # averiguamos la posición donde se hizo click
            botones(paint, x, y)
            
            paint = actualizar_juego(paint, x, y)
        """ elif ev.type == gamelib.EventType.Motion:
            print(f'se ha movido el puntero del mouse: {ev.x} {ev.y}')
        elif ev.type == gamelib.EventType.ButtonRelease and ev.mouse_button == 1:
            print(f'se ha soltado el botón del mouse: {ev.x} {ev.y}')
        elif ev.type == gamelib.EventType.KeyPress:
            print(f'se ha presionado la tecla: {ev.key}')"""
        #if ev.type == gamelib.EventType.ButtonPress:
            # El usuario presionó un botón del mouse
        
        
gamelib.init(main)
