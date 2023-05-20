# import logica_marcador_tenis as lmt
import logica_marcador_tenis as lmt
import mapeo_numeros_neopixel16x16 as mn
import machine
import neopixel
import time

marcador = lmt.MarcadorTenis()
marcador.obtener_estado_jugadores()
"""
#AQUI VA LA LOGICA DEL WEB SERVER
...
"""


def _obtener_marcador_jugadores():
    result = marcador.obtener_estado_jugadores()
    print(result)
    return result


def sumar_punto(jugador):
    marcador.actualizar_marcador(jugador)
    #_obtener_marcador_jugadores()


def _obtener_points_jugador(jugador):
    result = _obtener_marcador_jugadores()
    points_jugador = result[jugador]['points']
    print("puntos jugador " + jugador + " " + str(points_jugador))
    return points_jugador


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


def _devuelve_leds_para_enviar_a_matriz_de_un_game(digitos, jugador,set):
    #para j1 los games se mostraran en si sc sd
    #para j2 los games se mostraran en ii ic id
    # ----------
    # |si|sc|sd|
    # ----------
    # |ii|ic|id|
    # ----------
    pos_x_set_j1 = ["si", "sc", "sd"]
    pos_x_set_j2 = ["ii", "ic", "id"]
    digito_iz = digitos[0]
    digito_de = digitos[1]
    if jugador == "j1":
        leds_game_digito_izq = []
        leds_game_digito_der = mn.devuelve_leds_para_digito(pos_x_set_j1[set-1], digito_iz)
    else:
        leds_point_digito_izq = []
        leds_point_digito_der = mn.devuelve_leds_para_digito(pos_x_set_j2[set-1], digito_iz)
    return leds_point_digito_izq, leds_point_digito_der


def _muestra_points_en_matriz():
    pixels = neopixel.NeoPixel(machine.Pin(4), 255)
    result = _obtener_marcador_jugadores()
    points_j1 = _obtener_points_jugador("j1")
    points_j2 = _obtener_points_jugador("j2")
    if points_j1 != "":
        led_iz_point_j1,led_de_point_j1 = _devuelve_leds_para_enviar_a_matriz_de_un_punto(points_j1,"j1")
        #enciende los leds del digito iz del j1
        for i in led_iz_point_j1:
            pixels[i] = (0,0,255)
            pixels.write()
        for i in led_de_point_j1:
            pixels[i] = (0,0,255)
            pixels.write()        
    if points_j2 != "":
        led_iz_point_j2,led_de_point_j2 = _devuelve_leds_para_enviar_a_matriz_de_un_punto(points_j2,"j2")
        #aqui habria que encender esos leds, falta parte neopixel
        for i in led_iz_point_j2:
            pixels[i] = (0,255,0)
            pixels.write()
            
        for i in led_de_point_j2:
            pixels[i] = (0,255,0)
            pixels.write() 

        
         

#-----------PRUEBA PARTIDO-------------------
# resultado inicial
_muestra_points_en_matriz()
time.sleep(1)

#el j1 gana un punto
sumar_punto("j1") #15-0
_muestra_points_en_matriz()

time.sleep(1)
#el j2 gana un punto
sumar_punto("j2") #15-15
_muestra_points_en_matriz()

time.sleep(1)
#el j2 gana un punto
sumar_punto("j2") #15-30
_muestra_points_en_matriz()

time.sleep(1)
#el j2 gana un punto
sumar_punto("j2") #15-40
_muestra_points_en_matriz()

time.sleep(1)
#el j1 gana un punto
sumar_punto("j1") #30-40
_muestra_points_en_matriz()

time.sleep(1)
#el j1 gana un punto
sumar_punto("j1") #40-40
_muestra_points_en_matriz()

time.sleep(1)
#el j1 gana un punto
sumar_punto("j1") #ad-
_muestra_points_en_matriz()