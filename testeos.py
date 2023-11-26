import logica_marcador_tenis as lmt

# -----------------TESTEO---------------------------
marcador = lmt.MarcadorTenis()
marcador.obtener_marcador()


def _j2_gana_game_con_ventajas():
    for i in range(3):
        marcador.actualizar_marcador("j2")
        result = marcador.obtener_marcador()
        _imprime_points(result)
    for i in range(3):
        marcador.actualizar_marcador("j1")
        result = marcador.obtener_marcador()
        _imprime_points(result)
    # ad j1
    marcador.actualizar_marcador("j1")
    result = marcador.obtener_marcador()
    _imprime_points(result)
    # deuce j1 j2
    marcador.actualizar_marcador("j2")
    result = marcador.obtener_marcador()
    _imprime_points(result)
    # ad j1
    marcador.actualizar_marcador("j1")
    result = marcador.obtener_marcador()
    _imprime_points(result)
    # game j1
    marcador.actualizar_marcador("j1")
    result = marcador.obtener_marcador()
    _imprime_points(result)


# GANA GAME J2
def _j2_gana_game_con_ventajas():
    for i in range(3):
        marcador.actualizar_marcador("j1")
        result = marcador.obtener_marcador()
        _imprime_points(result)
    for i in range(3):
        marcador.actualizar_marcador("j2")
        result = marcador.obtener_marcador()
        _imprime_points(result)
    # ad j1
    marcador.actualizar_marcador("j1")
    result = marcador.obtener_marcador()
    _imprime_points(result)
    # deuce j1 j2
    marcador.actualizar_marcador("j2")
    result = marcador.obtener_marcador()
    _imprime_points(result)
    # ad j2
    marcador.actualizar_marcador("j2")
    result = marcador.obtener_marcador()
    _imprime_points(result)
    # game j2
    marcador.actualizar_marcador("j2")
    result = marcador.obtener_marcador()
    _imprime_points(result)


def _j1_gana_point():
    marcador.actualizar_marcador("j1")
    result = marcador.obtener_marcador()
    _imprime_points(result)


def _j2_gana_point():
    marcador.actualizar_marcador("j2")
    result = marcador.obtener_marcador()
    _imprime_points(result)


def _imprime_points(result):
    games_jugador1 = result['j1']['points']
    games_jugador2 = result['j2']['points']
    print(result)
    print(str(games_jugador1) + " - " + str(games_jugador2))


def _test_set_con_tiebrake():
    _j1_gana_point()  # 15
    _j1_gana_point()  # 30
    _j1_gana_point()  # 40
    _j1_gana_point()  # juego 1-0
    _j1_gana_point()  # 15
    _j1_gana_point()  # 30
    _j1_gana_point()  # 40
    _j1_gana_point()  # juego 2-0
    _j1_gana_point()  # 15
    _j1_gana_point()  # 30
    _j1_gana_point()  # 40
    _j1_gana_point()  # juego 3-0
    _j1_gana_point()  # 15
    _j1_gana_point()  # 30
    _j1_gana_point()  # 40
    _j1_gana_point()  # juego 4-0
    _j1_gana_point()  # 15
    _j1_gana_point()  # 30
    _j1_gana_point()  # 40
    _j1_gana_point()  # juego 5-0

    _j2_gana_point()  # 15
    _j2_gana_point()  # 30
    _j2_gana_point()  # 40
    _j2_gana_point()  # juego 1-0
    _j2_gana_point()  # 15
    _j2_gana_point()  # 30
    _j2_gana_point()  # 40
    _j2_gana_point()  # juego 2-0
    _j2_gana_point()  # 15
    _j2_gana_point()  # 30
    _j2_gana_point()  # 40
    _j2_gana_point()  # juego 3-0
    _j2_gana_point()  # 15
    _j2_gana_point()  # 30
    _j2_gana_point()  # 40
    _j2_gana_point()  # juego 4-0
    _j2_gana_point()  # 15
    _j2_gana_point()  # 30
    _j2_gana_point()  # 40
    _j2_gana_point()  # juego 5-0

    _j1_gana_point()  # 15
    _j1_gana_point()  # 30
    _j1_gana_point()  # 40
    _j1_gana_point()  # juego 6-5

    _j2_gana_point()  # 15
    _j2_gana_point()  # 30
    _j2_gana_point()  # 40
    _j2_gana_point()  # juego 6-6

    # tie brake
    _j1_gana_point()  # 1-0
    _j1_gana_point()  # 2-0
    _j1_gana_point()  # 3-0
    _j1_gana_point()  # 4-0
    _j1_gana_point()  # 5-0
    _j1_gana_point()  # 6-0
    _j2_gana_point()  # 6-1
    _j1_gana_point()  # 7-1


_test_set_con_tiebrake()
