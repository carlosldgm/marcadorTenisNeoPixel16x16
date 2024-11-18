import asyncio
from bleak import BleakScanner, BleakClient


async def scan_bluetooth():
    # Escanea dispositivos Bluetooth y muestra sus MAC y nombres
    devices = await BleakScanner.discover()
    for device in devices:
        print(f"Dispositivo encontrado: {device.name} con MAC {device.address}")
    return devices


async def connect_and_receive(mac_address):
    async with BleakClient(mac_address) as client:
        if client.is_connected:
            print(f"Conectado a {mac_address}")

            # Lista las características disponibles
            for service in client.services:
                print(f"Servicio: {service.uuid}")
                for char in service.characteristics:
                    print(f" - Característica: {char.uuid} (Notificaciones: {char.properties})")

                    # Si la característica soporta notificaciones, se suscribe
                    if "notify" in char.properties:
                        await client.start_notify(char.uuid, notification_handler)
                        print(f"Suscrito a notificaciones de {char.uuid}")

            # Mantén la conexión activa
            await asyncio.sleep(30)  # Ajusta el tiempo necesario


def notification_handler(sender, data):
    # Función que maneja los datos recibidos del dispositivo
    print(f"Notificación recibida de {sender}: {data}")


async def main():
    devices = await scan_bluetooth()

    # Puedes reemplazar con la MAC del control remoto que quieras conectar
    mac_address = "BEE5379B-1E05-2F6B-93C9-D0924BEB2C27"

    await connect_and_receive(mac_address)


# Ejecuta el programa
asyncio.run(main())
