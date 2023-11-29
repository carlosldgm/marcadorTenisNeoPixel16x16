# import logica_marcador_tenis as lmt
import logica_marcador_tenis as lmt
import mapeo_numeros_neopixel16x16 as mn
import machine
import neopixel
import time

# Crear una única instancia de NeoPixel al inicio del script
pixels = neopixel.NeoPixel(machine.Pin(4), 255)

marcador = lmt.MarcadorTenis()
marcador.obtener_marcador()



"""
#AQUI VA LA LOGICA DEL WEB SERVER
...
"""


def _obtener_marcador_jugadores():
    result = marcador.obtener_marcador()
    print(result)
    return result


def sumar_punto(jugador):
    marcador.actualizar_marcador(jugador)
    #_obtener_marcador()


def _obtener_points_jugador(jugador):
    result = _obtener_marcador_jugadores()
    points_jugador = result[jugador]['points']
    print("puntos jugador " + jugador + " " + str(points_jugador))
    return points_jugador

def _obtener_games_jugador(jugador):
    result = _obtener_marcador_jugadores()
    games_jugador = result[jugador]['games']
    print("games jugador " + jugador + " " + str(games_jugador))
    return games_jugador

def _devuelve_leds_para_enviar_a_matriz_de_un_punto(digitos, jugador):
    #para j1 los point se mostraran en ti td
    #para j2 los point se mostraran en bi bd
    # ----------
    # | ti|td  |
    # ----------
    # | bi|bd  |
    # ----------
    digito_iz = digitos[0]
    if len(digitos) >1 : #si vienen dos digitos ej: 15,30, 40, AD
        digito_de = digitos[1]
        if jugador == "j1":
            leds_point_digito_izq = mn.devuelve_leds_para_digito("ti", digito_iz)
            leds_point_digito_der = mn.devuelve_leds_para_digito("td", digito_de)
        else:
            leds_point_digito_izq = mn.devuelve_leds_para_digito("bi", digito_iz)
            leds_point_digito_der = mn.devuelve_leds_para_digito("bd", digito_de)
    else: #si solo viene un digitos ej: 0,1,2,3,4,5,6,7,8,9
        if jugador == "j1":
            leds_point_digito_izq = []
            leds_point_digito_der = mn.devuelve_leds_para_digito("td", digito_iz)
        else:
            leds_point_digito_izq = []
            leds_point_digito_der = mn.devuelve_leds_para_digito("bd", digito_iz)
    return leds_point_digito_izq, leds_point_digito_der


def _devuelve_leds_para_enviar_a_matriz_de_un_game(digitos, jugador,set_actual):
    #para j1 los games se mostraran en si sc sd
    #para j2 los games se mostraran en ii ic id
    # ----------
    # |si|sc|sd|
    # ----------
    # |ii|ic|id|
    # ----------
    pos_x_set_j1 = ["si", "sc", "sd"]
    pos_x_set_j2 = ["ii", "ic", "id"]
    
    #ej si digitos es 3 entonces digito_iz = 3 digito_de = []
    #ej si digitos es 12 entonces digito_iz = 1 digito_de = 2    
    digitos_str = str(digitos)
    digito_iz = digitos_str[0]
       
    pos_set_arr = int(set_actual)-1  
    if len(digitos_str) >1 : #si vienen dos digitos 
        digito_de = digitos_str[1]       
        if jugador == "j1":
            leds_game_digito_izq = mn.devuelve_leds_para_digito(pos_x_set_j1[pos_set_arr], digito_iz)
            leds_game_digito_der = mn.devuelve_leds_para_digito(pos_x_set_j1[pos_set_arr], digito_de)
        else:
            leds_point_digito_izq = mn.devuelve_leds_para_digito(pos_x_set_j2[pos_set_arr], digito_iz)
            leds_point_digito_der = mn.devuelve_leds_para_digito(pos_x_set_j2[pos_set_arr], digito_iz)
    else: #si solo viene un digitos ej: 0,1,2,3,4,5,6,7,8,9
        if jugador == "j1":
            leds_point_digito_izq = []
            leds_point_digito_der = mn.devuelve_leds_para_digito(pos_x_set_j1[pos_set_arr], digito_iz)
        else:
            leds_point_digito_izq = []
            leds_point_digito_der = mn.devuelve_leds_para_digito(pos_x_set_j2[pos_set_arr], digito_iz)

    return leds_point_digito_izq, leds_point_digito_der
    



def _muestra_points_en_matriz():
    _limpia_matriz()
    result = _obtener_marcador_jugadores()
    points_j1 = _obtener_points_jugador("j1")
    points_j2 = _obtener_points_jugador("j2")
    
    if points_j1 != "":
        led_iz_point_j1, led_de_point_j1 = _devuelve_leds_para_enviar_a_matriz_de_un_punto(points_j1, "j1")
        # Enciende los LEDs del dígito izquierdo del j1
        for i in led_iz_point_j1:
            pixels[i] = (0, 0, 255)
        # Enciende los LEDs del dígito derecho del j1
        for i in led_de_point_j1:
            pixels[i] = (0, 0, 255)
    if points_j2 != "":
        led_iz_point_j2, led_de_point_j2 = _devuelve_leds_para_enviar_a_matriz_de_un_punto(points_j2, "j2")
        # Enciende los LEDs del dígito izquierdo del j2
        for i in led_iz_point_j2:
            pixels[i] = (0, 255, 0)
        # Enciende los LEDs del dígito derecho del j2
        for i in led_de_point_j2:
            pixels[i] = (0, 255, 0)
    pixels.write()
    time.sleep(0.8)  # Ajusta el tiempo de espera si es necesario
 

def _muestra_games_en_matriz():
    _limpia_matriz()
    #pixels = neopixel.NeoPixel(machine.Pin(4), 255)
    result = _obtener_marcador_jugadores()
    games_j1 = _obtener_games_jugador("j1")
    games_j2 = _obtener_games_jugador("j2")
    set_actual = "1"
    led_iz_game_j1,led_de_game_j1 = _devuelve_leds_para_enviar_a_matriz_de_un_game(games_j1,"j1",set_actual)
    #enciende los leds del digito iz del j1
    for i in led_iz_game_j1:
        pixels[i] = (0,0,255)
        pixels.write()
    for i in led_de_game_j1:
        pixels[i] = (0,0,255)
        pixels.write()        

    led_iz_game_j2,led_de_game_j2 = _devuelve_leds_para_enviar_a_matriz_de_un_game(games_j2,"j2",set_actual)
    #aqui habria que encender esos leds, falta parte neopixel
    for i in led_iz_game_j2:
        pixels[i] = (0,255,0)
        pixels.write()
        
    for i in led_de_game_j2:
        pixels[i] = (0,255,0)
        pixels.write()         
         

def _limpia_matriz():
    pixels.fill((0, 0, 0))
    pixels.write()    
       
        
#-----------PRUEBA PARTIDO-------------------
# resultado inicial

_muestra_points_en_matriz()
#time.sleep(1)


for y in range(6):        
    #el j1 gana un punto
    sumar_punto("j1") #15-0
    _muestra_points_en_matriz()

    #time.sleep(1)
    #el j2 gana un punto
    sumar_punto("j2") #15-15
    _muestra_points_en_matriz()

    #time.sleep(1)
    #el j2 gana un punto
    sumar_punto("j2") #15-30
    _muestra_points_en_matriz()

    #time.sleep(1)
    #el j2 gana un punto
    sumar_punto("j2") #15-40
    _muestra_points_en_matriz()

    #time.sleep(1)
    #el j1 gana un punto
    sumar_punto("j1") #30-40
    _muestra_points_en_matriz()

    #time.sleep(1)
    #el j1 gana un punto
    sumar_punto("j1") #40-40
    _muestra_points_en_matriz()

    #time.sleep(1)
    #el j1 gana un punto
    sumar_punto("j1") #ad-
    _muestra_points_en_matriz()

    #time.sleep(1)
    #el j1 gana un punto
    sumar_punto("j1") #juego
    _muestra_points_en_matriz()


    _muestra_games_en_matriz()
    time.sleep(2)
