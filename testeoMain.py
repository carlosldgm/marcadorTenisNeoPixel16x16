import logica_marcador_tenis as lmt
import jsonUtils as ju
import despliega_valores_emulador_neopixel16x16 as dve


def _obtener_marcador():
    result = marcador.obtener_marcador()
    return result


def sumar_punto(jugador):
    suma_resta_punto_full(jugador)


def restar_punto(jugador):
    suma_resta_punto_full(jugador, -1)


def suma_resta_punto_full(jugador, SUMA_RESTA=1):
    result_prev = _obtener_marcador()
    games_prev = ju.obtener_games_jugador(jugador, result_prev)
    sets_prev = ju.obtener_set_actual(result_prev)
    marcador.actualizar_marcador(jugador, SUMA_RESTA)  # actualiza punto
    result_post = _obtener_marcador()
    games_post = ju.obtener_games_jugador(jugador, result_post)
    sets_post = ju.obtener_set_actual(result_post)

    if games_prev != games_post:
        dve.muestra_games_en_matriz(result_post) #si quiero que muestre games en matriz pasar True como parametro
    else:
        dve.muestra_points_en_matriz(result_post)

    print(result_post)


def resetear_marcador():
    marcador.resetear_marcador()

# -----------PRUEBA PARTIDO-------------------
marcador = lmt.MarcadorTenis()
result = _obtener_marcador()
dve.muestra_points_en_matriz(result,False)

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