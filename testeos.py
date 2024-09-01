"""
Este archivo tiene el sentido de hacer pruebas de la logica incluida en la clase  logica_marcador_tenis sin
mostrar la matriz de leds ni la logica bluetooth solo la logica que devuelve el json del marcador
"""
import logica_marcador_tenis as lmt

# -----------------TESTEO---------------------------
marcador = lmt.MarcadorTenis()
marcador.obtener_marcador()

def _j1_gana_point():
    marcador.actualizar_marcador("j1")
    result = marcador.obtener_marcador()
    _imprime_points(result)


def _j2_gana_point():
    marcador.actualizar_marcador("j2") #gana punto j2
    result = marcador.obtener_marcador() #recupera el marcador para obtener la actualizacion
    _imprime_points(result)


def _imprime_points(result):
    games_jugador1 = result['j1']['points']
    games_jugador2 = result['j2']['points']
    print(result)
    print(str(games_jugador1) + " - " + str(games_jugador2))


def _test_set_con_tiebrake():
    _j1_gana_point()  # 15-0
    _j1_gana_point()  # 30-0
    _j1_gana_point()  # 40-0
    _j1_gana_point()  # juego 1-0
    _j2_gana_point()  # 0-15
    _j2_gana_point()  # 0-30
    _j2_gana_point()  # 0-40
    _j1_gana_point()  # 15-40
    _j2_gana_point()  # juego 1-1
    _j2_gana_point()  # 0-15
    _j2_gana_point()  # 0-30
    _j1_gana_point()  # 15-30
    _j1_gana_point()  # 30-30
    _j1_gana_point()  # 40-30
    _j1_gana_point()  # juego 2-1
    _j2_gana_point()  # 0-15
    _j2_gana_point()  # 0-30
    _j2_gana_point()  # 0-40
    _j1_gana_point()  # 15-40
    _j2_gana_point()  # juego 2-2
    _j1_gana_point()  # 15-0
    _j1_gana_point()  # 30-0
    _j1_gana_point()  # 40-0
    _j1_gana_point()  # juego 3-2
    _j2_gana_point()  # 0-15
    _j1_gana_point()  # 15-15
    _j2_gana_point()  # 15-30
    _j2_gana_point()  # 15-40
    _j1_gana_point()  # 30-40
    _j2_gana_point()  # juego 3-3
    _j1_gana_point()  # 15-0
    _j2_gana_point()  # 15-15
    _j1_gana_point()  # 30-15
    _j1_gana_point()  # 40-15
    _j1_gana_point()  # juego 4-3
    _j2_gana_point()  # 0-15
    _j1_gana_point()  # 15-15
    _j2_gana_point()  # 15-30
    _j1_gana_point()  # 30-30
    _j2_gana_point()  # 30-40
    _j1_gana_point()  # 40-40
    _j2_gana_point()  # 40-A
    _j2_gana_point()  # juego 4-4
    _j2_gana_point()  # 0-15
    _j2_gana_point()  # 0-30
    _j1_gana_point()  # 15-30
    _j1_gana_point()  # 30-30
    _j1_gana_point()  # 40-30
    _j1_gana_point()  # juego 5-4
    _j2_gana_point()  # 0-15
    _j2_gana_point()  # 0-30
    _j1_gana_point()  # 15-30
    _j2_gana_point()  # 15-40
    _j2_gana_point()  # juego 5-5
    _j2_gana_point()  # 0-15
    _j1_gana_point()  # 15-15
    _j1_gana_point()  # 30-15
    _j1_gana_point()  # 40-15
    _j1_gana_point()  # juego 6-5
    _j2_gana_point()  # 0-15
    _j1_gana_point()  # 15-15
    _j2_gana_point()  # 15-30
    _j2_gana_point()  # 15-40
    _j2_gana_point()  # juego 6-6

    # TIE BRAKE
    _j1_gana_point()  # 1-0
    _j1_gana_point()  # 2-0
    _j1_gana_point()  # 3-0
    _j1_gana_point()  # 4-0
    _j1_gana_point()  # 5-0
    _j2_gana_point()  # 5-1
    _j2_gana_point()  # 5-2
    _j1_gana_point()  # 6-2
    _j1_gana_point()  # 7-2


_test_set_con_tiebrake()
