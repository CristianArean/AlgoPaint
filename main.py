import gamelib
import png

ALTO_TABLERO = 20
ANCHO_TABLERO = 20
ANCHO_VENTANA = 700
ALTO_VENTANA = 700
BLANCO = 0
def paint_nuevo(ancho, alto):
    '''inicializa el estado del programa con una imagen vacía de ancho x alto pixels'''
    paint = {}
    tablero = []
    for i in range(ALTO_TABLERO):
        filas = []
        for j in range(ANCHO_TABLERO):
            filas.append(BLANCO)
        tablero.append(filas)
    paint["color"] = BLANCO
    paint["tablero"] = tablero

    return paint

def paint_mostrar(paint):
    '''dibuja la interfaz de la aplicación en la ventana'''
    gamelib.draw_begin()
    gamelib.draw_rectangle(50, 45, ANCHO_VENTANA - 50, 645, outline='white', width=1, fill=None)
    pos_inicial_x1 = 50
    pos_inicial_y1= 45
    pos_inicial_x2= 80
    pos_inicial_y2= 75
    for i in paint["tablero"]:
        for j in paint["tablero"]:
            gamelib.draw_rectangle(pos_inicial_x1, pos_inicial_y1, pos_inicial_x2, pos_inicial_y2, fill = "white") 
            pos_inicial_x1 += 30
            pos_inicial_x2 += 30

        pos_inicial_x1 = 50
        pos_inicial_x2= 80
        pos_inicial_y1 += 30
        pos_inicial_y2 += 30

        

    gamelib.draw_end()

def main():
    gamelib.title("AlgoPaint")
    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA)

    paint = paint_nuevo(20, 20)

    while gamelib.is_alive():
        paint_mostrar(paint)

        ev = gamelib.wait()
        if not ev:
            break

        if ev.type == gamelib.EventType.ButtonPress and ev.mouse_button == 1:
            print(f'se ha presionado el botón del mouse: {ev.x} {ev.y}')
        elif ev.type == gamelib.EventType.Motion:
            print(f'se ha movido el puntero del mouse: {ev.x} {ev.y}')
        elif ev.type == gamelib.EventType.ButtonRelease and ev.mouse_button == 1:
            print(f'se ha soltado el botón del mouse: {ev.x} {ev.y}')
        elif ev.type == gamelib.EventType.KeyPress:
            print(f'se ha presionado la tecla: {ev.key}')

gamelib.init(main)
