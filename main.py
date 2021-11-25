import gamelib
import png

ALTO_TABLERO = 20
ANCHO_TABLERO = 20
ANCHO_VENTANA = 700  # x
ALTO_VENTANA = 700  # y
WHITE = (255, 255, 255) 
BLACK = (0, 0, 0) 
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255) 
COLORES = ("black", "white", "red", "green", "blue", "cyan", "yellow", "magenta")


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
    print(paint["tablero"])

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
        #if paint["tablero"][i][j] == paint["numero_color"]:
            gamelib.draw_rectangle(pos_inicial_x1, pos_inicial_y1, pos_inicial_x2, pos_inicial_y2, fill= f'#{paint["tablero"][i][j][0]:02x}{paint["tablero"][i][j][1]:02x}{paint["tablero"][i][j][2]:02x}')
            

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


    #boton de guardado 
    pos_inicial_x = 50
    pos_inicial_y = 650
    pos_final_x = 190
    pos_final_y = 680
    #for botones in range(3): #el tres son cantidad de botones

    gamelib.draw_rectangle(pos_inicial_x, pos_inicial_y, pos_final_x, pos_final_y, fill = "silver") #cantidad de botones
    gamelib.draw_text("cargar PPM", 120 , 665, bold = True) #cantidad de botones
    gamelib.draw_rectangle(190 + 30, pos_inicial_y, 360, pos_final_y, fill = "silver")
    gamelib.draw_text("guardar PPM", 290 , 665, bold = True) #cantidad de botones
    gamelib.draw_rectangle(360 + 30, pos_inicial_y, 360 + 30 + 140, pos_final_y, fill = "silver")
    gamelib.draw_text("guardar JPG", 460 , 665, bold = True) #cantidad de botones
    

    gamelib.draw_end()

def cargar_archivo(ruta, paint):
    pass

def guardar_ppm(paint):
    pass

def guardar_jpg(paint):
    ruta = gamelib.input("en que ruta quiere guardar el archivo?")
    paleta = []
    for i in range(len(paint["tablero"])):
        for j in range(len(paint(["tablero"]))):
            if not paint["tablero"][i][j] in paleta:
                paleta.append(paint["tablero"][i][j])
    png.escribir(ruta, paleta, paint["tablero"])

def nuevo_color():
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
        if ev.type == gamelib.EventType.ButtonPress and ev.mouse_button == 1:
            print(f'se ha presionado el botón del mouse: {ev.x} {ev.y}')
            x, y = ev.x, ev.y # averiguamos la posición donde se hizo click
            #botones(paint, x, y)
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
            elif x > 50 and y > 650 and x < 190 and y < 680:
                ruta = gamelib.input("Ingrese ruta del archivo")
                cargar_archivo(ruta, paint)
            elif x > 190 + 30 and y > 650 and x < 360 and y < 680:
                guardar_ppm(paint)
            elif x > 390 and y > 650 and x < 360 + 30 + 140 and y < 680:
                guardar_jpg(paint)
            else:
                pass
            
        elif ev.type == gamelib.EventType.Motion:
            print(f'se ha movido el puntero del mouse: {ev.x} {ev.y}')
        elif ev.type == gamelib.EventType.ButtonRelease and ev.mouse_button == 1:
            print(f'se ha soltado el botón del mouse: {ev.x} {ev.y}')
        elif ev.type == gamelib.EventType.KeyPress:
            print(f'se ha presionado la tecla: {ev.key}')
        #if ev.type == gamelib.EventType.ButtonPress:
            # El usuario presionó un botón del mouse
        
        if ev.type == gamelib.EventType.ButtonPress and ev.mouse_button == 1:
            print(f'se ha presionado el botón del mouse: {ev.x} {ev.y}')
            x, y = ev.x, ev.y
            paint = actualizar_juego(paint, x, y)
        
        
gamelib.init(main)
