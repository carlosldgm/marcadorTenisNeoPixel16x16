import logica_marcador_tenis as lmt
import jsonUtils as ju
import despliega_valores_matriz_neopixel16x16 as dvm

from machine import Pin
import bluetooth
from BLE import BLEUART


def _obtener_marcador_jugadores():
    result = marcador.obtener_marcador()
    print(result)
    return result


def sumar_punto(jugador):
    suma_resta_punto_full(jugador)


def restar_punto(jugador):
    suma_resta_punto_full(jugador, -1)


def suma_resta_punto_full(jugador, SUMA_RESTA=1):
    result_prev = _obtener_marcador()
    games_j1_prev = ju.obtener_games_jugador(jugador, result_prev)
    sets_j1_prev = ju.obtener_set_actual(result_prev)
    marcador.actualizar_marcador(jugador, SUMA_RESTA)  # actualiza punto
    result_post = _obtener_marcador()
    games_j1_post = ju.obtener_games_jugador(jugador, result_post)
    sets_j1_post = ju.obtener_set_actual(result_post)

    if games_j1_prev != games_j1_post:
        dvm.muestra_games_en_matriz(result_post)
    else:
        dvm.muestra_points_en_matriz(result_post)


def _obtener_marcador():
    result = marcador.obtener_marcador()
    return result


def resetear_marcador():
    marcador.resetear_marcador()


# -----------Logica Principal-------------------
#Crea una instancia de la clase que maneja la logica del marcador
marcador = lmt.MarcadorTenis()
result = _obtener_marcador()
dvm.muestra_points_en_matriz(result)

# logica de bluetooth
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

        if rx_recibe == "!B318":
            led.value(0)
            restar_punto("j1")

        if rx_recibe == "!B219":
            led.value(1)
            sumar_punto("j2")

        if rx_recibe == "!B417":
            led.value(0)
            restar_punto("j2")

        if rx_recibe == "!B615":
            led.value(0)
            resetear_marcador()

        dvm.muestra_points_en_matriz(result)


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
