import numpy as np
import matplotlib.pyplot as plt
import time

# Crear una matriz de 16x16 con valores azules
matrix = np.zeros((16, 16, 3), dtype=np.uint8)

def pinta_puntos_matriz(led_iz,led_de):
    print("led_iz")
    print(led_iz)
    print("led_de")
    print(led_de)
    if(len(led_iz)>0):
        for i in led_iz:
            # Calcular las coordenadas (x, y) a partir de la posición en una sola variable
            x = led_iz[i] % 16
            y = led_iz[i] // 16
            matrix[x, y] = [0, 0, 255]  # Componentes RGB del punto azul
    if (len(led_de) > 0):
        for i in led_de:
            x = led_de[i] % 16
            y = led_de[i] // 16
            matrix[x, y] = [0, 0, 255]  # Componentes RGB del punto azul

    plt.show()
    # Mostrar la matriz como una imagen
    plt.imshow(matrix)
    plt.axis('off')
    time.sleep(3)

def limpia_matriz():
    for x in range(16):
        for y in range(16):
            matrix[x, y] = [0, 0, 0]
    plt.show()
    # Mostrar la matriz como una imagen
    plt.imshow(matrix)
    plt.axis('off')

limpia_matriz()