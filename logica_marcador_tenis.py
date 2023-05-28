class MarcadorTenis:
    def __init__(self):
        self.points_jugador1 = 0
        self.points_jugador2 = 0
        self.games_jugador1 = 0
        self.games_jugador2 = 0
        self.sets_jugador1 = 0
        self.sets_jugador2 = 0
        self.tiebreak = False  # Variable para verificar si hay un tie break activo
        self.tiebreak_points_jugador1 = 0  # Puntos del jugador 1 en el tie break
        self.tiebreak_points_jugador2 = 0  # Puntos del jugador 2 en el tie break
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
            self.points_jugador1 = 0
            self.points_jugador2 = 0
            self.actualizar_games(ganador_punto)

    def actualizar_puntos_tiebreak(self, ganador_punto):
        if ganador_punto == "j1":
            self.tiebreak_points_jugador1 += 1
        else:
            self.tiebreak_points_jugador2 += 1

        if self._hay_ganador_tiebreak():
            if self.tiebreak_points_jugador1 > self.tiebreak_points_jugador2:
                print("j1 gana tiebrake")
            else:
                print("j2 gana tiebrake")
            print("Tiebrake: " + str(self.tiebreak_points_jugador1) + " - " + str(self.tiebreak_points_jugador2))
            self.tiebreak = False
            self.points_jugador1 = 0
            self.points_jugador2 = 0
            self.actualizar_games(ganador_punto)

    def _hay_ganador_game(self):
        if (
                self.points_jugador1 >= 4 and
                self.points_jugador1 - self.points_jugador2 >= 2
        ) or (
                self.points_jugador2 >= 4 and
                self.points_jugador2 - self.points_jugador1 >= 2
        ):
            return True
        return False

    def _hay_ganador_tiebreak(self):
        if (
                self.tiebreak_points_jugador1 >= 7 and
                self.tiebreak_points_jugador1 - self.tiebreak_points_jugador2 >= 2
        ) or (
                self.tiebreak_points_jugador2 >= 7 and
                self.tiebreak_points_jugador2 - self.tiebreak_points_jugador1 >= 2
        ):
            self.tiebrake_end = True
            return True
        return False

    def actualizar_games(self, ganador_punto):
        if self.tiebreak:
            self.actualizar_games_tiebreak(ganador_punto)
        else:
            if ganador_punto == "j1":
                self.games_jugador1 += 1
            else:
                self.games_jugador2 += 1
            print("games: " + str(self.games_jugador1) + " - " + str(self.games_jugador2))
            if self._hay_ganador_set():
                if self.games_jugador1 > self.games_jugador2:
                    self.sets_jugador1 += 1
                    print("¡El jugador 1 gana el set!")
                    print("Sets:", self.sets_jugador1, self.sets_jugador2)
                else:
                    self.sets_jugador2 += 1
                    print("¡El jugador 2 gana el set!")
                    print("Sets:", self.sets_jugador1, self.sets_jugador2)
                    self.resetear_marcador()

    def actualizar_games_tiebreak(self, ganador_punto):
        if ganador_punto == "j1":
            self.tiebreak_points_jugador1 += 1
        else:
            self.tiebreak_points_jugador2 += 1

        if self._hay_ganador_tiebreak():
            self.tiebreak = False
            self.points_jugador1 = 0
            self.points_jugador2 = 0
            if ganador_punto == "j1":
                self.games_jugador1 += 1
            else:
                self.games_jugador2 += 1

            if self._hay_ganador_set():
                if self.games_jugador1 > self.games_jugador2:
                    self.sets_jugador1 += 1
                    print("¡El jugador 1 gana el set!")
                    print("Sets:", self.sets_jugador1, self.sets_jugador2)
                else:
                    self.sets_jugador2 += 1
                    print("¡El jugador 2 gana el set!")
                    print("Sets:", self.sets_jugador1, self.sets_jugador2)
                self.resetear_marcador()

    def iniciar_tiebreak(self):
        self.tiebreak = True
        self.tiebreak_points_jugador1 = 0
        self.tiebreak_points_jugador2 = 0

    def resetear_marcador(self):
        self.points_jugador1 = 0
        self.points_jugador2 = 0
        self.games_jugador1 = 0
        self.games_jugador2 = 0
        self.tiebreak_points_jugador1 = 0
        self.tiebreak_points_jugador2 = 0

    def _imprimir_games(self):
        print("Games:", self.games_jugador1, self.games_jugador2)
        print()

    def _hay_ganador_set(self):
        if self.tiebrake_end:
            self.set_actual += 1
            return True
        if self.games_jugador1 == 6 and self.games_jugador2 == 6:
            self.iniciar_tiebreak()
            return False  # Empate a 6 juegos, se debe jugar un tie break
        elif (
                self.games_jugador1 >= 6 and
                self.games_jugador1 - self.games_jugador2 >= 2
        ) or (
                self.games_jugador2 >= 6 and
                self.games_jugador2 - self.games_jugador1 >= 2
        ):
            self.set_actual += 1
            return True
        return False

    def obtener_estado_jugadores(self):
        if not self.tiebreak:
            if self.points_jugador1 >= 4 or self.points_jugador2 >= 4:
                if self.points_jugador1 - self.points_jugador2 == 1:
                    puntos_j1 = self.puntajes[4]  # AD j1
                    puntos_j2 = ""
                elif self.points_jugador2 - self.points_jugador1 == 1:
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
