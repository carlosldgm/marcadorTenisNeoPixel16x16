import time
from traceback import format_exception

import mapeo_numeros_neopixel16x16 as mn
import jsonUtils as ju
import emula_matriz_16x16 as sm

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

#poner el valor de Show a False si no quiero mostrar los points en el emulador de la matriz led
def muestra_points_en_matriz(result, show = True):
    if show:
        #result = _obtener_marcador()
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
def muestra_games_en_matriz(result, show = True):
    if show:
        #result = _obtener_marcador()
        games_j1 = ju.obtener_games_jugador("j1", result)
        games_j2 = ju.obtener_games_jugador("j2", result)
        if games_j1 == 0 and games_j2 == 0:
            return
        set_actual = ju.obtener_set_actual(result)


        led_iz_game_j1, led_de_game_j1 = _devuelve_leds_para_enviar_a_matriz_de_un_game(games_j1, "j1", set_actual)
        # enciende los leds del digito iz del j1
        sm.pinta_puntos_matriz(led_iz_game_j1, led_de_game_j1)
        # sm.limpia_matriz()

        led_iz_game_j2, led_de_game_j2 = _devuelve_leds_para_enviar_a_matriz_de_un_game(games_j2, "j2", set_actual)
        # enciende los leds del digito iz del j2
        sm.pinta_puntos_matriz(led_iz_game_j2, led_de_game_j2)

        time.sleep(1)
        sm.limpia_matriz()



def muestra_games_en_matriz_con_sets_anteriores(result, show = True):
    if show:
        set_actual = ju.obtener_set_actual(result)
        if set_actual == "2":
            fin_set1_j1 = ju.obtener_games_final_set_jugador("j1", result, 1)
            fin_set1_j2 = ju.obtener_games_final_set_jugador("j2", result, 1)
            led_iz_game_j1, led_de_game_j1 = _devuelve_leds_para_enviar_a_matriz_de_un_game(fin_set1_j1, "j1", 1)
            sm.pinta_puntos_matriz(led_iz_game_j1, led_de_game_j1)

            led_iz_game_j2, led_de_game_j2 = _devuelve_leds_para_enviar_a_matriz_de_un_game(fin_set1_j2, "j2", 1)
            sm.pinta_puntos_matriz(led_iz_game_j2, led_de_game_j2)
        elif set_actual == "3":
            fin_set2_j1 = ju.obtener_games_final_set_jugador("j1", result, 2)
            fin_set2_j2 = ju.obtener_games_final_set_jugador("j2", result, 2)
            led_iz_game_j1, led_de_game_j1 = _devuelve_leds_para_enviar_a_matriz_de_un_game(fin_set2_j1, "j1", 2)
            sm.pinta_puntos_matriz(led_iz_game_j1, led_de_game_j1)

            led_iz_game_j2, led_de_game_j2 = _devuelve_leds_para_enviar_a_matriz_de_un_game(fin_set2_j2, "j2", 2)
            sm.pinta_puntos_matriz(led_iz_game_j2, led_de_game_j2)

        games_j1 = ju.obtener_games_jugador("j1", result)
        games_j2 = ju.obtener_games_jugador("j2", result)
        if games_j1 == 0 and games_j2 == 0:
            return

        led_iz_game_j1, led_de_game_j1 = _devuelve_leds_para_enviar_a_matriz_de_un_game(games_j1, "j1", set_actual)
        sm.pinta_puntos_matriz(led_iz_game_j1, led_de_game_j1)

        led_iz_game_j2, led_de_game_j2 = _devuelve_leds_para_enviar_a_matriz_de_un_game(games_j2, "j2", set_actual)
        sm.pinta_puntos_matriz(led_iz_game_j2, led_de_game_j2)

        time.sleep(1)
        sm.limpia_matriz()


"""
def muestra_sets_en_matriz(result, show = True):
    if show:
        set_actual = ju.obtener_set_actual(result)
        for i in range(int(set_actual)):
            games_j1 = ju.obtener_games_final_set_jugador("j1", result, i+1)
            games_j2 = ju.obtener_games_final_set_jugador("j2", result, i+1)
            if not(games_j1 == "0" and games_j2 == "0"):
                led_iz_game_j1, led_de_game_j1 = _devuelve_leds_para_enviar_a_matriz_de_un_game(games_j1, "j1", i+1)
                # enciende los leds del digito iz del j1
                sm.pinta_puntos_matriz(led_iz_game_j1, led_de_game_j1)

                led_iz_game_j2, led_de_game_j2 = _devuelve_leds_para_enviar_a_matriz_de_un_game(games_j2, "j2", i+1)
                # enciende los leds del digito iz del j2
                sm.pinta_puntos_matriz(led_iz_game_j2, led_de_game_j2)

        time.sleep(1)
        sm.limpia_matriz()
"""

def _limpia_matriz():
    sm.limpia_matriz()