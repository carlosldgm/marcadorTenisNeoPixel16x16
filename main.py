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
    """
    obtiene el marcador para poder sacar el game y set antes de sumar el nuevo punto y poder saber despues
    si cambio el valor del set luego de sumar el ultimo punto que debe mostrar el marcador de sets y no de games
    """
    #obtiene el marcador antes de sumar un punto
    result_prev = _obtener_marcador()
    point_prev = ju.obtener_points_jugador(jugador, result_prev)
    games_prev = ju.obtener_games_jugador(jugador, result_prev)
    sets_prev = ju.obtener_set_actual(result_prev)
    if not (point_prev == "0" and SUMA_RESTA == -1):
        marcador.actualizar_marcador(jugador, SUMA_RESTA)
    #obtiene el marcador despues de sumar el punto
    result_post = _obtener_marcador()
    point_post = ju.obtener_points_jugador(jugador, result_post)
    games_post = ju.obtener_games_jugador(jugador, result_post)
    sets_post = ju.obtener_set_actual(result_post)

    if (games_prev != games_post) or (sets_prev != sets_post): #hay que hcer una funcion que muestre todos los games de cada set
        dvm.muestra_games_en_matriz(result_post)
    else:
        dvm.muestra_points_en_matriz(result_post)


def _obtener_marcador():
    result = marcador.obtener_marcador()
    return result


def resetear_marcador():
    marcador.resetear_marcador()


# -----------Logica Principal-------------------
#Crea una instancia de la clase MarcadorTenis que maneja la logica del marcador
marcador = lmt.MarcadorTenis()
result = _obtener_marcador()
dvm.muestra_points_en_matriz(result)

# logica de bluetooth
name = "Marcador-Tenis"
led = Pin(2, Pin.OUT)

#Beauty-R1 con MAC BEE5379B-1E05-2F6B-93C9-D0924BEB2C27
def on_rx():
    if uart.any():  # Verifica si hay datos en el buffer
        try:
            rx_recibe = uart.read().decode().strip()
            uart.write("EspBot dice:" + str(rx_recibe) + "\n")
            print(rx_recibe)

            if rx_recibe == "!B516": #flecha arriba
                led.value(1)
                sumar_punto("j1")

            if rx_recibe == "!B615": #flecha abajo
                led.value(0)
                restar_punto("j1")

            if rx_recibe == "!B219": #2 
                led.value(1)
                sumar_punto("j2")

            if rx_recibe == "!B417": #4
                led.value(0)
                restar_punto("j2")

            if rx_recibe == "!B714": #flecha izq
                led.value(0)
                resetear_marcador()

            #dvm.muestra_points_en_matriz(result)


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


