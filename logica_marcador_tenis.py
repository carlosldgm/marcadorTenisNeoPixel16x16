class MarcadorTenis:
    def __init__(self):
        self.resetear_marcador()

    def resetear_marcador(self):
        self.points_jugador1 = 0
        self.points_jugador2 = 0
        self.games_jugador1 = 0
        self.games_jugador2 = 0
        self.sets_jugador1 = 0
        self.sets_jugador2 = 0
        self.tiebreak = False
        self.tiebreak_points_jugador1 = 0
        self.tiebreak_points_jugador2 = 0
        self.tiebrake_end = False
        self.set_actual = 1
        self.puntajes = ["0", "15", "30", "40", "AD"]

    def actualizar_marcador(self, ganador_punto):
        if self.tiebreak:
            self.actualizar_puntos_tiebreak(ganador_punto)
        else:
            self.actualizar_puntos(ganador_punto)

    def actualizar_puntos(self, ganador_punto):
        if ganador_punto == "j1":
            self.points_jugador1 += 1
        else:
            self.points_jugador2 += 1

        if self._hay_ganador_game():
            self.resetear_puntos()
            self.actualizar_games(ganador_punto)

    def resetear_puntos(self):
        self.points_jugador1 = 0
        self.points_jugador2 = 0

    def actualizar_puntos_tiebreak(self, ganador_punto):
        if ganador_punto == "j1":
            self.tiebreak_points_jugador1 += 1
        else:
            self.tiebreak_points_jugador2 += 1

        if self._hay_ganador_tiebreak():
            self.finalizar_tiebreak(ganador_punto)
            self.actualizar_games(ganador_punto)

    def finalizar_tiebreak(self, ganador_punto):
        print(f"{ganador_punto} gana tiebreak")
        print(f"Tiebreak: {self.tiebreak_points_jugador1} - {self.tiebreak_points_jugador2}")
        self.tiebreak = False
        self.resetear_puntos()

    def _hay_ganador_game(self):
        return (
            (self.points_jugador1 >= 4 and self.points_jugador1 - self.points_jugador2 >= 2) or
            (self.points_jugador2 >= 4 and self.points_jugador2 - self.points_jugador1 >= 2)
        )

    def _hay_ganador_tiebreak(self):
        return (
            (self.tiebreak_points_jugador1 >= 7 and
             self.tiebreak_points_jugador1 - self.tiebreak_points_jugador2 >= 2) or
            (self.tiebreak_points_jugador2 >= 7 and
             self.tiebreak_points_jugador2 - self.tiebreak_points_jugador1 >= 2)
        )

    def actualizar_games(self, ganador_punto):
        if self.tiebreak:
            self.actualizar_games_tiebreak(ganador_punto)
        else:
            self.actualizar_games_regular(ganador_punto)

    def actualizar_games_regular(self, ganador_punto):
        if ganador_punto == "j1":
            self.games_jugador1 += 1
        else:
            self.games_jugador2 += 1

        print(f"games: {self.games_jugador1} - {self.games_jugador2}")
        if self._hay_ganador_set():
            self.finalizar_set(ganador_punto)

    def actualizar_games_tiebreak(self, ganador_punto):
        self.tiebreak_points_jugador1 += 1 if ganador_punto == "j1" else 0
        self.tiebreak_points_jugador2 += 1 if ganador_punto != "j1" else 0

        if self._hay_ganador_tiebreak():
            self.finalizar_tiebreak(ganador_punto)

    def finalizar_set(self, ganador_punto):
        if self.games_jugador1 > self.games_jugador2:
            self.sets_jugador1 += 1
            print("¡El jugador 1 gana el set!")
        else:
            self.sets_jugador2 += 1
            print("¡El jugador 2 gana el set!")

        print(f"Sets: {self.sets_jugador1} - {self.sets_jugador2}")
        self.resetear_set()
        self.verificar_ganador_partido()

    def resetear_set(self):
        self.games_jugador1 = 0
        self.games_jugador2 = 0
        self.set_actual += 1

    def iniciar_tiebreak(self):
        self.tiebreak = True
        self.tiebreak_points_jugador1 = 0
        self.tiebreak_points_jugador2 = 0

    def _hay_ganador_set(self):
        if self.tiebrake_end:
            return True

        if self.games_jugador1 == 6 and self.games_jugador2 == 6:
            self.iniciar_tiebreak()
            return False

        return (
            (self.games_jugador1 >= 6 and self.games_jugador1 - self.games_jugador2 >= 2) or
            (self.games_jugador2 >= 6 and self.games_jugador2 - self.games_jugador1 >= 2)
        )

    def verificar_ganador_partido(self):
        if self.sets_jugador1 == 2:
            print("¡El jugador 1 gana el partido!")
        elif self.sets_jugador2 == 2:
            print("¡El jugador 2 gana el partido!")

    def obtener_marcador(self):
        if not self.tiebreak:
            if self.points_jugador1 >= 4 or self.points_jugador2 >= 4:  # si ya estamos en la parte de los 40's
                if self.points_jugador1 - self.points_jugador2 == 1:  # hay ventaja para jugador 1
                    puntos_j1 = self.puntajes[4]  # AD j1
                    puntos_j2 = ""
                elif self.points_jugador2 - self.points_jugador1 == 1: # hay ventaja para jugador 2
                    puntos_j2 = self.puntajes[4]  # AD j2
                    puntos_j1 = ""
                else:
                    puntos_j1 = self.puntajes[3]  # 40 - 40
                    puntos_j2 = self.puntajes[3]  # 40 - 40
            else:
                puntos_j1 = self.puntajes[self.points_jugador1]  # no ha pasado los 40 rige (0,15,30,40)
                puntos_j2 = self.puntajes[self.points_jugador2]  # no ha pasado los 40 rige (0,15,30,40)
        else:
            # como es tie brake rige (1,2..hasta ventaja de 2)
            puntos_j1 = self.tiebreak_points_jugador1
            puntos_j2 = self.tiebreak_points_jugador2
        result = {
            "set_actual": {self.set_actual},
            "j1": {
                "points": puntos_j1,
                "games": self.games_jugador1,
                "sets": self.sets_jugador1
            },
            "j2": {
                "points": puntos_j2,
                "games": self.games_jugador2,
                "sets": self.sets_jugador2
            }
        }
        # print(result)
        return result
