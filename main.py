from tda import Pila
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
COLORES = ("black", "white", "red", "green",
           "blue", "cyan", "yellow", "magenta")
MENSAJE_ELIJA_COLOR = "ingrese en formato r, g, b el color que quiere ingresar"
MENSAJE_NO_ELIGIO_COLOR = "No se eligió ningun color"
MENSAJE_EN_DONDE_GUARDAR_ARCHIVO = "en que ruta quiere guardar el archivo?"
MENSAJE_RUTA = "Ingrese ruta del archivo"
MENSAJE_EXCEPCION_NUEVO_COLOR = "Hubo un problema con el color ingresado, asegurese de escribirlo correctamente"
ELIJA_NOMBRE_ARCHIVO = "Ingrese un nombre para el archivo"
MENSAJE_DE_GUARDADO_SATISFACTORIO = "la imagen se guardo correctamente"
# 50 #primer pixel en que arranca el tablero
POS_INICIAL_X1 = ANCHO_VENTANA * 7.1428 / 100  # 50
POS_INICIAL_Y1 = ALTO_VENTANA * 6.4285 / 100  # 45
# 80 pixel en el que termina el primer cuadrado
POS_INICIAL_X2 = ANCHO_VENTANA * 11.4285 / 100
POS_INICIAL_Y2 = ALTO_VENTANA * 10.7142 / 100  # 75
LADO_CUADRADO = POS_INICIAL_X2 - POS_INICIAL_X1  # 30
X1_COLORES = ANCHO_VENTANA * 1.429 / 100
Y1_COLORES = ALTO_VENTANA * 27.857 / 100
X2_COLORES = ANCHO_VENTANA * 5.714 / 100
Y2_COLORES = ALTO_VENTANA * 32.143 / 100
IMG_LAPIZ = "lapiz.gif"
BOTE_DE_PINTURA = "bote_de_pintura.gif"
IMG_GIF = "signo_mas.gif"
IMG_DESHACER = "deshacer.gif"
IMG_REHACER = "rehacer.gif"
MENSAJE_DESHACER = "No hay elementos para deshacer"
MENSAJE_REHACER = "No hay elementos para rehacer"
MSG_CARGA_CORRECTA = "Se cargo correctamente"
CARGAR_PPM = "CARGAR PPM"
GUARDAR_PPM = "GUARDAR PPM"
GUARDAR_PNG = "GUARDAR PNG"

def paint_nuevo():
    '''inicializa el estado del programa con una imagen vacía de ancho x alto pixels'''
    paint = {}
    paint["numero_color"] = WHITE
    tablero = []
    paint["deshacer"] = Pila()
    paint["rehacer"] = Pila()
    paint["modo"] = "lapiz"
    for _ in range(ALTO_TABLERO):
        filas = []
        for _ in range(ANCHO_TABLERO):
            filas.append(paint["numero_color"])
        tablero.append(filas)

    paint["tablero"] = tablero

    return paint


def copiador(paint):
    nuevo_tablero = []
    for i in range(ALTO_TABLERO):
        filas = []
        for j in range(ANCHO_TABLERO):
            filas.append(paint["tablero"][i][j])
        nuevo_tablero.append(filas)

    return nuevo_tablero


def copiador_dicc(dicc):
    nuevo_dicc = {}
    for clave, valor in dicc.items():
        nuevo_dicc[clave] = valor

    return nuevo_dicc


def esta_vacia(paint):
    for i in range(len(paint["tablero"])):
        for j in range(len(paint["tablero"][0])):
            if paint["tablero"][i][j] != 0:
                return False
        return True


def paint_actualizar(paint, x, y):
    nuevo_paint = copiador_dicc(paint)
    nuevo_paint_aux = copiador_dicc(paint)

    # dato para posterior escalabilidad: ese numero que se suma, 30 en este caso, es la cantidad de pixeles que tiene un cuadrado en un lado
    if x > X1_COLORES and x < X2_COLORES and y > Y1_COLORES and y < Y2_COLORES:
        nuevo_paint["numero_color"] = BLACK

    elif x > X1_COLORES and x < X2_COLORES and y > (Y1_COLORES + (LADO_CUADRADO)) and y < (Y2_COLORES + (LADO_CUADRADO)):
        nuevo_paint["numero_color"] = WHITE

    elif x > X1_COLORES and x < X2_COLORES and y > (Y1_COLORES + 2 * (LADO_CUADRADO)) and y < (Y2_COLORES + 2 * (LADO_CUADRADO)):
        nuevo_paint["numero_color"] = RED

    elif x > X1_COLORES and x < X2_COLORES and y > (Y1_COLORES + 3 * (LADO_CUADRADO)) and y < (Y2_COLORES + 3 * (LADO_CUADRADO)):
        nuevo_paint["numero_color"] = GREEN

    elif x > X1_COLORES and x < X2_COLORES and y > (Y1_COLORES + 4 * (LADO_CUADRADO)) and y < (Y2_COLORES + 4 * (LADO_CUADRADO)):
        nuevo_paint["numero_color"] = BLUE

    elif x > X1_COLORES and x < X2_COLORES and y > (Y1_COLORES + 5 * (LADO_CUADRADO)) and y < (Y2_COLORES + 5 * (LADO_CUADRADO)):
        nuevo_paint["numero_color"] = CYAN

    elif x > X1_COLORES and x < X2_COLORES and y > (Y1_COLORES + 6 * (LADO_CUADRADO)) and y < (Y2_COLORES + 6 * (LADO_CUADRADO)):
        nuevo_paint["numero_color"] = YELLOW

    elif x > X1_COLORES and x < X2_COLORES and y > (Y1_COLORES + 7 * (LADO_CUADRADO)) and y < (Y2_COLORES + 7 * (LADO_CUADRADO)):
        nuevo_paint["numero_color"] = MAGENTA

    elif x > X1_COLORES and x < X2_COLORES and y > (Y1_COLORES + 8 * (LADO_CUADRADO)) and y < (Y2_COLORES + 8 * (LADO_CUADRADO)):
        nuevo_color(nuevo_paint)
    elif x > X1_COLORES and x < X2_COLORES and y > (Y1_COLORES + 9 * (LADO_CUADRADO)) and y < (Y2_COLORES + 9 * (LADO_CUADRADO)):
        #deshacer
        if paint["deshacer"].esta_vacia():
            gamelib.say(MENSAJE_DESHACER)
        else:
            nuevo_paint["rehacer"].apilar(nuevo_paint["tablero"])
            nuevo_paint["tablero"] = nuevo_paint["deshacer"].desapilar()

    elif x > X1_COLORES and x < X2_COLORES and y > (Y1_COLORES + 10 * (LADO_CUADRADO)) and y < (Y2_COLORES + 10 * (LADO_CUADRADO)):
        #rehacer
        if paint["rehacer"].esta_vacia():
            gamelib.say(MENSAJE_REHACER)
        else:
            nuevo_paint["deshacer"].apilar(nuevo_paint["tablero"])
            nuevo_paint["tablero"] = nuevo_paint["rehacer"].desapilar()
    
    elif x > X1_COLORES and x < X2_COLORES and y > (Y1_COLORES + 11 * (LADO_CUADRADO)) and y < (Y2_COLORES + 11 * (LADO_CUADRADO)):
        if nuevo_paint["modo"] == "lapiz":
            nuevo_paint["modo"] = "balde"
        elif nuevo_paint["modo"] == "balde":
            nuevo_paint["modo"] = "lapiz"
            
    elif x > POS_INICIAL_X1 and y > (ALTO_VENTANA * 92.857 / 100) and x < (ANCHO_VENTANA * 27.143 / 100) and y < (ALTO_VENTANA * 97.143 / 100):
        ruta = gamelib.input(MENSAJE_RUTA)
        if ruta == "" or ruta == None:
            return paint
        tablero = cargar_archivo(ruta)
        nuevo_paint["tablero"] = tablero
        gamelib.say(MSG_CARGA_CORRECTA)

    elif x > (ANCHO_VENTANA * 31.429 / 100) and y > (ALTO_VENTANA * 92.857 / 100) and x < ANCHO_VENTANA * 51.429 / 100 and y < (ALTO_VENTANA * 97.143 / 100):
        guardar_ppm(nuevo_paint)

    elif x > (ANCHO_VENTANA * 55.714 / 100) and y > (ALTO_VENTANA * 92.857 / 100) and x < (ANCHO_VENTANA * 75.714 / 100) + LADO_CUADRADO + 140 and y < (ALTO_VENTANA * 97.143 / 100):
        guardar_png(nuevo_paint)

    elif x > POS_INICIAL_X1 and x < ANCHO_VENTANA * 92.857 / 100 and y > POS_INICIAL_Y1 and y < (ALTO_VENTANA * 92.143 / 100):
        nuevo_paint_aux = copiador(paint)
        nuevo_paint["deshacer"].apilar(nuevo_paint_aux)
        filas = int((y - POS_INICIAL_X1) / LADO_CUADRADO)
        columnas = int((x - POS_INICIAL_Y1) / LADO_CUADRADO)
        if nuevo_paint["modo"] == "lapiz":
            nuevo_paint["tablero"][filas][columnas] = nuevo_paint["numero_color"]
        elif nuevo_paint["modo"] == "balde":
            color_previo = nuevo_paint["tablero"][filas][columnas]
            if color_previo == nuevo_paint["numero_color"]: #esto soluciona un bug que hacia que de muchas recursiones
                return nuevo_paint
            nuevo_paint = balde_pintura(nuevo_paint, filas, columnas, color_previo)
    return nuevo_paint



def paint_mostrar(paint):
    '''dibuja la interfaz de la aplicación en la ventana'''
    gamelib.draw_begin()
    gamelib.draw_rectangle(0, 0, ANCHO_VENTANA, ALTO_VENTANA, fill="gray")

    pos_inicial_x1 = POS_INICIAL_X1
    pos_inicial_y1 = POS_INICIAL_Y1
    pos_inicial_x2 = POS_INICIAL_X2
    pos_inicial_y2 = POS_INICIAL_Y2

    for i in range(len(paint["tablero"])):
        for j in range(len(paint["tablero"])):
            gamelib.draw_rectangle(pos_inicial_x1, pos_inicial_y1, pos_inicial_x2, pos_inicial_y2,
                                   fill=f'#{paint["tablero"][i][j][0]:02x}{paint["tablero"][i][j][1]:02x}{paint["tablero"][i][j][2]:02x}')

            pos_inicial_x1 += LADO_CUADRADO
            pos_inicial_x2 += LADO_CUADRADO

        pos_inicial_x1 = ANCHO_VENTANA * 7.1428 / 100  # 50
        pos_inicial_x2 = ANCHO_VENTANA * 11.4285 / 100

        pos_inicial_y1 += LADO_CUADRADO
        pos_inicial_y2 += LADO_CUADRADO

    x1_colores = X1_COLORES
    y1_colores = Y1_COLORES
    x2_colores = X2_COLORES
    y2_colores = Y2_COLORES

    for colores in COLORES:
        gamelib.draw_rectangle(x1_colores, y1_colores, x2_colores,
                               y2_colores, fill=colores)  # cuadrados
        y1_colores += LADO_CUADRADO
        y2_colores += LADO_CUADRADO

    gamelib.draw_image(IMG_GIF, x1_colores, y1_colores)
    gamelib.draw_image(IMG_DESHACER, x1_colores, y1_colores + LADO_CUADRADO)
    gamelib.draw_image(IMG_REHACER, x1_colores, y1_colores + 2 * LADO_CUADRADO)
    
    if paint["modo"] == "lapiz":
        gamelib.draw_image(BOTE_DE_PINTURA, x1_colores,
                        y1_colores + 3 * LADO_CUADRADO)
    elif paint["modo"] == "balde":
        gamelib.draw_image(IMG_LAPIZ, x1_colores,
                        y1_colores + 3 * LADO_CUADRADO)
        

    # boton de guardado
    pos_inicial_x = ANCHO_VENTANA * 7.1428 / 100  # 50
    pos_inicial_y = ALTO_VENTANA * 92.857 / 100  # 650
    pos_final_x = ANCHO_VENTANA * 27.143 / 100  # 190
    pos_final_y = ALTO_VENTANA * 97.143 / 100  # 680
    pos_y_medio = (pos_final_y + pos_inicial_y) / 2

    gamelib.draw_rectangle(pos_inicial_x, pos_inicial_y, pos_final_x,
                           pos_final_y, fill="silver")  # cantidad de botones
    gamelib.draw_text(CARGAR_PPM, ANCHO_VENTANA * 17.143 /
                      100, pos_y_medio, bold=True)  # cantidad de botones
    gamelib.draw_rectangle(ANCHO_VENTANA * 31.429 / 100, pos_inicial_y, ANCHO_VENTANA * 51.429 / 100,
                           pos_final_y, fill="silver")
    gamelib.draw_text(GUARDAR_PPM, ANCHO_VENTANA * 41.329 / 100, pos_y_medio,
                      bold=True)  # cantidad de botones
    gamelib.draw_rectangle(ANCHO_VENTANA * 55.714 / 100, pos_inicial_y,
                           ANCHO_VENTANA * 75.714 / 100, pos_final_y, fill="silver")
    gamelib.draw_text(GUARDAR_PNG, ANCHO_VENTANA * 65.714 / 100, pos_y_medio,
                      bold=True)  # cantidad de botones

    gamelib.draw_end()


def str_a_tablero(cadena):
    tablero = []
    indice_global = 0

    for i in range(ALTO_TABLERO):
        fila = []
        while len(fila) < ANCHO_TABLERO:
            if indice_global % 3 == 0:
                lista = cadena[indice_global:indice_global + 3]
                lista = [int(x) for x in lista]
                tupla = tuple(lista)
                fila.append(tupla)
            indice_global += 1
        tablero.append(fila)

    return tablero



def balde_pintura(paint, filas, columnas, color_previo):
    if paint["tablero"][filas][columnas] == color_previo:
        paint["tablero"][filas][columnas] = paint["numero_color"]
        if filas > 0:
            paint = balde_pintura(paint, filas - 1, columnas, color_previo)
        if filas < ALTO_TABLERO - 1:
            paint = balde_pintura(paint, filas + 1, columnas, color_previo)
        if columnas > 0:
            paint = balde_pintura(paint, filas, columnas - 1, color_previo)
        if columnas < ANCHO_TABLERO - 1:
            paint = balde_pintura(paint, filas, columnas + 1, color_previo)
    return paint     



def cargar_archivo(archivo):
    with open(archivo) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines][3]
        lines = lines.split()
    tablero = str_a_tablero(lines)
    return tablero


def formato(paint):
    paint = paint["tablero"]
    string_final = ""
    maximo = -1
    for i in range(ALTO_TABLERO):
        segundo_string = ""
        for j in range(ANCHO_TABLERO):
            primer_string = ""
            for valores in paint[i][j]:
                if valores > maximo:
                    maximo = valores
                primer_string += str(valores)
                primer_string += " "
            segundo_string += primer_string
        string_final += segundo_string
    return string_final, maximo


def guardar_ppm(paint):
    file, maximo = formato(paint)
    nombre_del_archivo = gamelib.input(ELIJA_NOMBRE_ARCHIVO)
    if nombre_del_archivo == None or nombre_del_archivo == "":
        return paint_mostrar(paint)
    with open(f"{nombre_del_archivo}.ppm", "w") as outf:
        outf.write("P3\n")
        outf.write(f"{ALTO_TABLERO} {ANCHO_TABLERO}\n")
        outf.write(str(maximo) + "\n")
        outf.write(file)
    gamelib.say(MENSAJE_DE_GUARDADO_SATISFACTORIO)


def colores(matriz):
    paleta = []
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if not matriz[i][j] in paleta:
                paleta.append(matriz[i][j])
    return paleta


def guardar_png(paint):
    nombre = gamelib.input(ELIJA_NOMBRE_ARCHIVO)
    if nombre == None or nombre == "":
        return paint_mostrar(paint)
    paleta = colores(paint["tablero"])
    juego_comprimido = []
    for i in range(len(paint["tablero"])):
        filas = []
        for j in range(len(paint["tablero"][i])):
            indice_en_paleta = paleta.index(paint["tablero"][i][j])
            filas.append(indice_en_paleta)
        juego_comprimido.append(filas)

    png.escribir(f"{nombre}.png", paleta, juego_comprimido)


def nuevo_color(paint):
    color_seleccionado = gamelib.input(MENSAJE_ELIJA_COLOR)
    if color_seleccionado == None or color_seleccionado == "":
        gamelib.say(MENSAJE_NO_ELIGIO_COLOR)
        return paint_mostrar(paint)
    try:
        color_seleccionado = color_seleccionado.split(",")
        color_seleccionado = [int(numeros) for numeros in color_seleccionado]
        color_seleccionado = tuple(color_seleccionado)
    except:
        gamelib.say(MENSAJE_EXCEPCION_NUEVO_COLOR)
        return paint_mostrar(paint)
    while len(color_seleccionado) > 3:
        nuevo_color(paint)
    paint["numero_color"] = color_seleccionado


def main():
    gamelib.title("AlgoPaint")
    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA)

    paint = paint_nuevo()

    while gamelib.is_alive():
        paint_mostrar(paint)

        ev = gamelib.wait()
        if not ev:
            break
        if ev.type == gamelib.EventType.ButtonPress and ev.mouse_button == 1:
            x, y = ev.x, ev.y  # averiguamos la posición donde se hizo click
            paint = paint_actualizar(paint, x, y)

        

gamelib.init(main)
