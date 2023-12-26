# import logica_marcador_tenis as lmt
import logica_marcador_tenis as lmt
import mapeo_numeros_neopixel16x16 as mn
import machine
import neopixel
import time

from machine import Pin

import bluetooth
from BLE import BLEUART

# Crear una única instancia de NeoPixel al inicio del script
pixels = neopixel.NeoPixel(machine.Pin(4), 255)

marcador = lmt.MarcadorTenis()
marcador.obtener_marcador()


def _obtener_marcador_jugadores():
    result = marcador.obtener_marcador()
    print(result)
    return result


"""
def sumar_punto(jugador):
    print("entre a sumar")
    marcador.actualizar_marcador(jugador)
    
def restar_punto(jugador):
    marcador.actualizar_marcador(jugador, -1)    
"""


def sumar_punto(jugador):
    suma_resta_punto_full(jugador)


def restar_punto(jugador):
    suma_resta_punto_full(jugador, -1)


def suma_resta_punto_full(jugador, SUMA_RESTA=1):
    result_prev = _obtener_marcador()
    games_j1_prev = _obtener_games_jugador(jugador, result_prev)
    sets_j1_prev = _obtener_set_actual()
    marcador.actualizar_marcador(jugador, SUMA_RESTA)  # actualiza punto
    result_post = _obtener_marcador()
    games_j1_post = _obtener_games_jugador(jugador, result_post)
    sets_j1_post = _obtener_set_actual()

    if games_j1_prev != games_j1_post:
        _muestra_games_en_matriz()
    else:
        _muestra_points_en_matriz()


def _obtener_set_actual():
    result = _obtener_marcador()
    set_actual = str(result['set_actual'])
    return set_actual


"""
def _obtener_points_jugador(jugador):
    result = _obtener_marcador_jugadores()
    points_jugador = result[jugador]['points']
    print("puntos jugador " + jugador + " " + str(points_jugador))
    return points_jugador
"""


def _obtener_points_jugador(jugador, result):
    # result = _obtener_marcador()
    points_jugador = result[jugador]['points']
    # print("puntos jugador " + jugador + " " + str(points_jugador))
    return points_jugador


"""
def _obtener_games_jugador(jugador):
    result = _obtener_marcador_jugadores()
    games_jugador = result[jugador]['games']
    print("games jugador " + jugador + " " + str(games_jugador))
    return games_jugador
"""


def _obtener_games_jugador(jugador, result):
    games_jugador = result[jugador]['games']
    return games_jugador


def _devuelve_leds_para_enviar_a_matriz_de_un_punto(digitos, jugador):
    # para j1 los point se mostraran en ti td
    # para j2 los point se mostraran en bi bd
    # ----------
    # | ti|td  |
    # ----------
    # | bi|bd  |
    # ----------
    digito_iz = digitos[0]
    if len(digitos) > 1:  # si vienen dos digitos ej: 15,30, 40, AD
        digito_de = digitos[1]
        if jugador == "j1":
            leds_point_digito_izq = mn.devuelve_leds_para_digito("ti", digito_iz)
            leds_point_digito_der = mn.devuelve_leds_para_digito("td", digito_de)
        else:
            leds_point_digito_izq = mn.devuelve_leds_para_digito("bi", digito_iz)
            leds_point_digito_der = mn.devuelve_leds_para_digito("bd", digito_de)
    else:  # si solo viene un digitos ej: 0,1,2,3,4,5,6,7,8,9
        if jugador == "j1":
            leds_point_digito_izq = []
            leds_point_digito_der = mn.devuelve_leds_para_digito("td", digito_iz)
        else:
            leds_point_digito_izq = []
            leds_point_digito_der = mn.devuelve_leds_para_digito("bd", digito_iz)
    return leds_point_digito_izq, leds_point_digito_der


def _devuelve_leds_para_enviar_a_matriz_de_un_game(digitos, jugador, set_actual):
    # para j1 los games se mostraran en si sc sd
    # para j2 los games se mostraran en ii ic id
    # ----------
    # |si|sc|sd|
    # ----------
    # |ii|ic|id|
    # ----------
    pos_x_set_j1 = ["si", "sc", "sd"]
    pos_x_set_j2 = ["ii", "ic", "id"]

    # ej si digitos es 3 entonces digito_iz = 3 digito_de = []
    # ej si digitos es 12 entonces digito_iz = 1 digito_de = 2
    digitos_str = str(digitos)
    digito_iz = digitos_str[0]

    pos_set_arr = int(set_actual) - 1
    if len(digitos_str) > 1:  # si vienen dos digitos
        digito_de = digitos_str[1]
        if jugador == "j1":
            leds_game_digito_izq = mn.devuelve_leds_para_digito(pos_x_set_j1[pos_set_arr], digito_iz)
            leds_game_digito_der = mn.devuelve_leds_para_digito(pos_x_set_j1[pos_set_arr], digito_de)
        else:
            leds_point_digito_izq = mn.devuelve_leds_para_digito(pos_x_set_j2[pos_set_arr], digito_iz)
            leds_point_digito_der = mn.devuelve_leds_para_digito(pos_x_set_j2[pos_set_arr], digito_iz)
    else:  # si solo viene un digitos ej: 0,1,2,3,4,5,6,7,8,9
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
    points_j1 = _obtener_points_jugador("j1", result)
    points_j2 = _obtener_points_jugador("j2", result)

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
    # pixels = neopixel.NeoPixel(machine.Pin(4), 255)
    result = _obtener_marcador_jugadores()
    games_j1 = _obtener_games_jugador("j1", result)
    games_j2 = _obtener_games_jugador("j2", result)
    if games_j1 == 0 and games_j2 == 0:
        return
    set_actual = _obtener_set_actual()
    led_iz_game_j1, led_de_game_j1 = _devuelve_leds_para_enviar_a_matriz_de_un_game(games_j1, "j1", set_actual)
    # enciende los leds del digito iz del j1
    for i in led_iz_game_j1:
        pixels[i] = (0, 0, 255)
        pixels.write()
    for i in led_de_game_j1:
        pixels[i] = (0, 0, 255)
        pixels.write()

    led_iz_game_j2, led_de_game_j2 = _devuelve_leds_para_enviar_a_matriz_de_un_game(games_j2, "j2", set_actual)
    # aqui habria que encender esos leds, falta parte neopixel
    for i in led_iz_game_j2:
        pixels[i] = (0, 255, 0)
        pixels.write()

    for i in led_de_game_j2:
        pixels[i] = (0, 255, 0)
        pixels.write()
    time.sleep(3)
    _limpia_matriz()


def _limpia_matriz():
    pixels.fill((0, 0, 0))
    pixels.write()


def _obtener_marcador():
    result = marcador.obtener_marcador()
    return result


def resetear_marcador():
    marcador.resetear_marcador()


def _obtener_set_actual():
    result = _obtener_marcador()
    set_actual = str(result['set_actual'])
    print("set actual " + set_actual)
    return set_actual


# -----------PRUEBA PARTIDO-------------------

"""
_muestra_points_en_matriz()



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
"""

# Aqui ira la logica de bluetooth
name = "Marcador-Tenis"
led = Pin(2, Pin.OUT)


def on_rx():
    try:
        rx_recibe = uart.read().decode().strip()
        uart.write("EspBot dice:" + str(rx_recibe) + "\n")
        print(rx_recibe)

        if rx_recibe == "!B516":
            led.value(1)
            sumar_punto("j1")
            _muestra_points_en_matriz()

        if rx_recibe == "!B318":
            led.value(0)
            restar_punto("j1")
            _muestra_points_en_matriz()
            
        if rx_recibe == "!B219":
            led.value(1)
            sumar_punto("j2")
            _muestra_points_en_matriz()

        if rx_recibe == "!B417":
            led.value(0)
            restar_punto("j2")
            _muestra_points_en_matriz()
            
        if rx_recibe == "!B615":
            led.value(0)
            resetear_marcador()
            
        _muestra_points_en_matriz()
            
        
    except Exception as e:
        print("Error al procesar datos: {}".format(e))


try:
    print(name, "Conectado a Bluetooth")
    ble = bluetooth.BLE()
    uart = BLEUART(ble, name)
    uart.irq(handler=on_rx)

except bluetooth.BluetoothError as be:
    print("Error Bluetooth: {}".format(be))
except Exception as e:
    print("Error general: {}".format(e))

