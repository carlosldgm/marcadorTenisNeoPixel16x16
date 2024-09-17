def obtener_points_jugador(jugador, result):
    # result = _obtener_marcador()
    points_jugador = result[jugador]['points']
    # print("puntos jugador " + jugador + " " + str(points_jugador))
    return points_jugador


def obtener_games_jugador(jugador, result):
    games_jugador = result[jugador]['games']
    # print("games jugador " + jugador + " " + str(games_jugador))
    return games_jugador


def obtener_set_actual(result):
    #result = _obtener_marcador()
    set_actual = str(result['set_actual'])
    #print("set actual " + set_actual)
    return set_actual