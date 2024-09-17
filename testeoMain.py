# import logica_marcador_tenis as lmt
from pickle import FALSE

import logica_marcador_tenis as lmt
import mapeo_numeros_neopixel16x16 as mn
import time
import simula_matriz_16x16 as sm
import jsonUtils as ju


def _obtener_marcador():
    result = marcador.obtener_marcador()
    #print(result)
    return result


def sumar_punto(jugador):
    # marcador.actualizar_marcador(jugador)
    suma_resta_punto_full(jugador)


def restar_punto(jugador):
    # marcador.actualizar_marcador(jugador, -1)
    suma_resta_punto_full(jugador, -1)

"""
def _obtener_points_jugador(jugador, result):
    # result = _obtener_marcador()
    points_jugador = result[jugador]['points']
    # print("puntos jugador " + jugador + " " + str(points_jugador))
    return points_jugador


def _obtener_games_jugador(jugador, result):
    games_jugador = result[jugador]['games']
    # print("games jugador " + jugador + " " + str(games_jugador))
    return games_jugador


def _obtener_set_actual():
    result = _obtener_marcador()
    set_actual = str(result['set_actual'])
    #print("set actual " + set_actual)
    return set_actual
"""

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
    set_actual = 3 #SACAR
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

#poner el valor de Show a False si no quiero mostrar los points en el emulador de la matriz led
def _muestra_points_en_matriz(show = True):
    if show:
        result = _obtener_marcador()
        points_j1 = ju.obtener_points_jugador("j1", result)
        points_j2 = ju.obtener_points_jugador("j2", result)

        if points_j1 != "":
            led_iz_point_j1, led_de_point_j1 = _devuelve_leds_para_enviar_a_matriz_de_un_punto(points_j1, "j1")
            sm.pinta_puntos_matriz(led_iz_point_j1, led_de_point_j1)
        if points_j2 != "":
            led_iz_point_j2, led_de_point_j2 = _devuelve_leds_para_enviar_a_matriz_de_un_punto(points_j2, "j2")
            sm.pinta_puntos_matriz(led_iz_point_j2, led_de_point_j2)
        # time.sleep(0.2)
        sm.limpia_matriz()

#poner el valor de Show a False si no quiero mostrar los games en el emulador de la matriz led
def _muestra_games_en_matriz(show = True):
    if show:
        result = _obtener_marcador()
        games_j1 = ju.obtener_games_jugador("j1", result)
        games_j2 = ju.obtener_games_jugador("j2", result)
        if games_j1 == 0 and games_j2 == 0:
            return
        set_actual = ju.obtener_set_actual(result)  # "1"  # Aca sacar set_actual del json
        led_iz_game_j1, led_de_game_j1 = _devuelve_leds_para_enviar_a_matriz_de_un_game(games_j1, "j1", set_actual)
        # enciende los leds del digito iz del j1
        sm.pinta_puntos_matriz(led_iz_game_j1, led_de_game_j1)
        # sm.limpia_matriz()

        led_iz_game_j2, led_de_game_j2 = _devuelve_leds_para_enviar_a_matriz_de_un_game(games_j2, "j2", set_actual)
        # enciende los leds del digito iz del j2
        sm.pinta_puntos_matriz(led_iz_game_j2, led_de_game_j2)
        time.sleep(1)
        sm.limpia_matriz()


def _limpia_matriz():
    sm.limpia_matriz()


def suma_resta_punto_full(jugador, SUMA_RESTA=1):
    result_prev = _obtener_marcador()
    games_prev = ju.obtener_games_jugador(jugador, result_prev)
    sets_prev = ju.obtener_set_actual(result_prev)
    marcador.actualizar_marcador(jugador, SUMA_RESTA)  # actualiza punto
    result_post = _obtener_marcador()
    games_post = ju.obtener_games_jugador(jugador, result_post)
    sets_post = ju.obtener_set_actual(result_post)

    if games_prev != games_post:
        _muestra_games_en_matriz() #si quiero que muestre games en matriz pasar True como parametro
    else:
        _muestra_points_en_matriz()

    print(result_post)


def resetear_marcador():
    marcador.resetear_marcador()


def j1_gana_game():
    # el j1 gana un punto
    sumar_punto("j1")  # 15-0

    # el j1 gana un punto
    sumar_punto("j1")  # 30-0

    # el j1 gana un punto
    sumar_punto("j1")  # 40-0

    # el j1 gana un punto
    sumar_punto("j1")  # juego


# -----------PRUEBA PARTIDO-------------------
marcador = lmt.MarcadorTenis()
_muestra_points_en_matriz(False)

#1-0
sumar_punto("j1")  # 15-0
sumar_punto("j1")  # 30-0
sumar_punto("j1")  # 40-0
sumar_punto("j1")  # juego

#1-1
sumar_punto("j2")  # 0-15
sumar_punto("j2")  # 0-30
sumar_punto("j2")  # 0-40
sumar_punto("j1")  # 15-40
sumar_punto("j2")  # juego

#2-1
sumar_punto("j2")  # 0-15
sumar_punto("j2")  # 0-30
sumar_punto("j1")  # 15-30
sumar_punto("j1")  # 30-30
sumar_punto("j1")  # 40-30
sumar_punto("j1")  # juego

#2-2
sumar_punto("j2")  # 0-15
sumar_punto("j2")  # 0-30
sumar_punto("j2")  # 0-40
sumar_punto("j1")  # 15-40
sumar_punto("j2")  # juego

#3-2
sumar_punto("j1")  # 15-0
sumar_punto("j1")  # 30-0
sumar_punto("j1")  # 40-0
sumar_punto("j1")  # juego

#3-3
sumar_punto("j2")  # 0-15
sumar_punto("j1")  # 15-15
sumar_punto("j2")  # 15-30
sumar_punto("j2")  # 15-40
sumar_punto("j1")  # 30-40
sumar_punto("j2")  # juego

#4-3
sumar_punto("j1")  # 15-0
sumar_punto("j2")  # 15-15
sumar_punto("j1")  # 30-15
sumar_punto("j1")  # 40-15
sumar_punto("j1")  # juego

#4-4
sumar_punto("j2")  # 0-15
sumar_punto("j1")  # 15-15
sumar_punto("j2")  # 15-30
sumar_punto("j1")  # 30-30
sumar_punto("j2")  # 30-40
sumar_punto("j1")  # 40-40
sumar_punto("j2")  # 40-A
sumar_punto("j2")  # juego

#5-4
sumar_punto("j2")  # 0-15
sumar_punto("j2")  # 0-30
sumar_punto("j1")  # 15-30
sumar_punto("j1")  # 30-30
sumar_punto("j1")  # 40-30
sumar_punto("j1")  # juego

#5-5
sumar_punto("j2")  # 0-15
sumar_punto("j2")  # 0-30
sumar_punto("j1")  # 15-30
sumar_punto("j2")  # 15-40
sumar_punto("j2")  # juego

#6-5
sumar_punto("j2")  # 0-15
sumar_punto("j1")  # 15-15
sumar_punto("j1")  # 30-15
sumar_punto("j1")  # 40-15
sumar_punto("j1")  # juego

#6-6
sumar_punto("j2")  # 0-15
sumar_punto("j1")  # 15-15
sumar_punto("j2")  # 15-30
sumar_punto("j2")  # 15-40
sumar_punto("j2")  # juego

#TIE BRAKE
sumar_punto("j1")  # 1-0
sumar_punto("j1")  # 2-0
sumar_punto("j1")  # 3-0
sumar_punto("j1")  # 4-0
sumar_punto("j1")  # 5-0
sumar_punto("j2")  # 5-1
sumar_punto("j2")  # 5-2
sumar_punto("j1")  # 6-2
sumar_punto("j1")  # 7-2 SET


#_muestra_games_en_matriz()