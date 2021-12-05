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
POS_INICIAL_X1 = ANCHO_VENTANA * 7.1428 / 100
POS_INICIAL_Y1 = ALTO_VENTANA * 6.4285 / 100  # 45
# 80 pixel en el que termina el primer cuadrado
POS_INICIAL_X2 = ANCHO_VENTANA * 11.4285 / 100
POS_INICIAL_Y2 = ALTO_VENTANA * 10.7142 / 100  # 75
LADO_CUADRADO = POS_INICIAL_X2 - POS_INICIAL_X1  # 30
X1_COLORES = 10
Y1_COLORES = 195
X2_COLORES = 40
Y2_COLORES = 225


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


def copiador_dicc(dicc):
    nuevo_dicc = {}
    for clave, valor in dicc.items():
        nuevo_dicc[clave] = valor

    return nuevo_dicc


def paint_actualizar(paint, x, y):
    nuevo_paint = copiador_dicc(paint)
    if x > 10 and x < 40 and y > 200 and y < 230:  # dato para posterior escalabilidad: ese numero que se suma, 30 en este caso, es la cantidad de pixeles que tiene un cuadrado en un lado
        nuevo_paint["numero_color"] = BLACK
    elif x > 10 and x < 40 and y > 230 and y < 260:
        nuevo_paint["numero_color"] = WHITE
    elif x > 10 and x < 40 and y > 260 and y < 290:
        nuevo_paint["numero_color"] = RED
    elif x > 10 and x < 40 and y > 290 and y < 320:
        nuevo_paint["numero_color"] = GREEN
    elif x > 10 and x < 40 and y > 320 and y < 350:
        nuevo_paint["numero_color"] = BLUE
    elif x > 10 and x < 40 and y > 350 and y < 380:
        nuevo_paint["numero_color"] = CYAN
    elif x > 10 and x < 40 and y > 380 and y < 410:
        nuevo_paint["numero_color"] = YELLOW
    elif x > 10 and x < 40 and y > 410 and y < 440:
        nuevo_paint["numero_color"] = MAGENTA
    elif x > 10 and x < 40 and y > 440 and y < 470:
        nuevo_color(nuevo_paint)
    elif x > 50 and y > 650 and x < 190 and y < 680:
        ruta = gamelib.input(MENSAJE_RUTA)

        if ruta == "" or ruta == None:
            return paint

        tablero = cargar_archivo(ruta)
        nuevo_paint["tablero"] = tablero
        gamelib.say("se cargo correctamente")
    elif x > 190 + 30 and y > 650 and x < 360 and y < 680:
        guardar_ppm(nuevo_paint)
    elif x > 390 and y > 650 and x < 360 + 30 + 140 and y < 680:
        guardar_png(nuevo_paint)
    elif x > 50 and x < 650 and y > 45 and y < 645:
        filas = int((y - 50) / LADO_CUADRADO)
        columnas = int((x - 45) / LADO_CUADRADO)
        nuevo_paint["tablero"][filas][columnas] = nuevo_paint["numero_color"]

    return nuevo_paint


def paint_mostrar(paint):
    '''dibuja la interfaz de la aplicación en la ventana'''
    gamelib.draw_begin()
    gamelib.draw_rectangle(0, 0, ANCHO_VENTANA, ALTO_VENTANA, fill="gray")

    pos_inicial_x1 = POS_INICIAL_X1
    pos_inicial_y1 = POS_INICIAL_Y1
    pos_inicial_x2 = POS_INICIAL_X2
    pos_inicial_y2 = POS_INICIAL_Y2
    lado_cuadrado = LADO_CUADRADO
    # print(paint["tablero"])

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
        x1_colores

    gamelib.draw_image('signo_mas.gif', x1_colores, y1_colores)

    # boton de guardado
    pos_inicial_x = 50
    pos_inicial_y = 650
    pos_final_x = 190
    pos_final_y = 680
    # for botones in range(3): #el tres son cantidad de botones

    gamelib.draw_rectangle(pos_inicial_x, pos_inicial_y, pos_final_x,
                           pos_final_y, fill="silver")  # cantidad de botones
    gamelib.draw_text("cargar PPM", 120, 665, bold=True)  # cantidad de botones
    gamelib.draw_rectangle(190 + 30, pos_inicial_y, 360,
                           pos_final_y, fill="silver")
    gamelib.draw_text("guardar PPM", 290, 665,
                      bold=True)  # cantidad de botones
    gamelib.draw_rectangle(360 + 30, pos_inicial_y, 360 +
                           30 + 140, pos_final_y, fill="silver")
    gamelib.draw_text("guardar JPG", 460, 665,
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


def guardar_png(paint):
    ruta = gamelib.input(MENSAJE_EN_DONDE_GUARDAR_ARCHIVO)
    paleta = []
    for i in range(len(paint["tablero"])):
        for j in range(len(paint["tablero"])):
            if not paint["tablero"][i][j] in paleta:
                paleta.append(paint["tablero"][i][j])
    png.escribir(ruta, paleta, paint["tablero"])


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

    paint = paint_nuevo(ALTO_TABLERO, ANCHO_TABLERO)

    while gamelib.is_alive():
        paint_mostrar(paint)

        ev = gamelib.wait()
        if not ev:
            break
        if ev.type == gamelib.EventType.ButtonPress and ev.mouse_button == 1:
            print(f'se ha presionado el botón del mouse: {ev.x} {ev.y}')
            x, y = ev.x, ev.y  # averiguamos la posición donde se hizo click
            #botones(paint, x, y)
            paint = paint_actualizar(paint, x, y)

        elif ev.type == gamelib.EventType.Motion:
            print(f'se ha movido el puntero del mouse: {ev.x} {ev.y}')
        elif ev.type == gamelib.EventType.ButtonRelease and ev.mouse_button == 1:
            print(f'se ha soltado el botón del mouse: {ev.x} {ev.y}')
        elif ev.type == gamelib.EventType.KeyPress:
            print(f'se ha presionado la tecla: {ev.key}')
        # if ev.type == gamelib.EventType.ButtonPress:
            # El usuario presionó un botón del mouse


gamelib.init(main)
