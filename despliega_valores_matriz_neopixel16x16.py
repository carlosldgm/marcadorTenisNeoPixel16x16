import mapeo_numeros_neopixel16x16 as mn
import jsonUtils as ju
import machine
import neopixel
import time

# Crear una única instancia de NeoPixel al inicio del script
pixels = neopixel.NeoPixel(machine.Pin(4), 255)

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


def muestra_points_en_matriz(result):
    _limpia_matriz()
    #result = _obtener_marcador_jugadores()
    points_j1 = ju.obtener_points_jugador("j1", result)
    points_j2 = ju.obtener_points_jugador("j2", result)

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
#    time.sleep(0.8)  # Ajusta el tiempo de espera si es necesario


def muestra_games_en_matriz(result):
    _limpia_matriz()

    games_j1 = ju.obtener_games_jugador("j1", result)
    games_j2 = ju.obtener_games_jugador("j2", result)
    if games_j1 == 0 and games_j2 == 0:
        return
    set_actual = ju.obtener_set_actual(result)
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
#    time.sleep(3)
#    _limpia_matriz()


def _limpia_matriz():
    pixels.fill((0, 0, 0))
    pixels.write()
