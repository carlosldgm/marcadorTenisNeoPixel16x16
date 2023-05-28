import numpy as np
import matplotlib.pyplot as plt
import time

posicion_p_a_x_y = {
    (0): [15, 0],
    (1): [15, 1],
    (2): [15, 2],
    (3): [15, 3],
    (4): [15, 4],
    (5): [15, 5],
    (6): [15, 6],
    (7): [15, 7],
    (8): [15, 8],
    (9): [15, 9],
    (10): [15, 10],
    (11): [15, 11],
    (12): [15, 12],
    (13): [15, 13],
    (14): [15, 14],
    (15): [15, 15],
    (16): [14, 15],
    (17): [14, 14],
    (18): [14, 13],
    (19): [14, 12],
    (20): [14, 11],
    (21): [14, 10],
    (22): [14, 9],
    (23): [14, 8],
    (24): [14, 7],
    (25): [14, 6],
    (26): [14, 5],
    (27): [14, 4],
    (28): [14, 3],
    (29): [14, 2],
    (30): [14, 1],
    (31): [14, 0],
    (32): [13, 0],
    (33): [13, 1],
    (34): [13, 2],
    (35): [13, 3],
    (36): [13, 4],
    (37): [13, 5],
    (38): [13, 6],
    (39): [13, 7],
    (40): [13, 8],
    (41): [13, 9],
    (42): [13, 10],
    (43): [13, 11],
    (44): [13, 12],
    (45): [13, 13],
    (46): [13, 14],
    (47): [13, 15],
    (48): [12, 15],
    (49): [12, 14],
    (50): [12, 13],
    (51): [12, 12],
    (52): [12, 11],
    (53): [12, 10],
    (54): [12, 9],
    (55): [12, 8],
    (56): [12, 7],
    (57): [12, 6],
    (58): [12, 5],
    (59): [12, 4],
    (60): [12, 3],
    (61): [12, 2],
    (62): [12, 1],
    (63): [12, 0],
    (64): [11, 0],
    (65): [11, 1],
    (66): [11, 2],
    (67): [11, 3],
    (68): [11, 4],
    (69): [11, 5],
    (70): [11, 6],
    (71): [11, 7],
    (72): [11, 8],
    (73): [11, 9],
    (74): [11, 10],
    (75): [11, 11],
    (76): [11, 12],
    (77): [11, 13],
    (78): [11, 14],
    (79): [11, 15],
    (80): [10, 15],
    (81): [10, 14],
    (82): [10, 13],
    (83): [10, 12],
    (84): [10, 11],
    (85): [10, 10],
    (86): [10, 9],
    (87): [10, 8],
    (88): [10, 7],
    (89): [10, 6],
    (90): [10, 5],
    (91): [10, 4],
    (92): [10, 3],
    (93): [10, 2],
    (94): [10, 1],
    (95): [10, 0],
    (96): [9, 0],
    (97): [9, 1],
    (98): [9, 2],
    (99): [9, 3],
    (100): [9, 4],
    (101): [9, 5],
    (102): [9, 6],
    (103): [9, 7],
    (104): [9, 8],
    (105): [9, 9],
    (106): [9, 10],
    (107): [9, 11],
    (108): [9, 12],
    (109): [9, 13],
    (110): [9, 14],
    (111): [9, 15],
    (112): [8, 15],
    (113): [8, 14],
    (114): [8, 13],
    (115): [8, 12],
    (116): [8, 11],
    (117): [8, 10],
    (118): [8, 9],
    (119): [8, 8],
    (120): [8, 7],
    (121): [8, 6],
    (122): [8, 5],
    (123): [8, 4],
    (124): [8, 3],
    (125): [8, 2],
    (126): [8, 1],
    (127): [8, 0],
    (128): [7, 0],
    (129): [7, 1],
    (130): [7, 2],
    (131): [7, 3],
    (132): [7, 4],
    (133): [7, 5],
    (134): [7, 6],
    (135): [7, 7],
    (136): [7, 8],
    (137): [7, 9],
    (138): [7, 10],
    (139): [7, 11],
    (140): [7, 12],
    (141): [7, 13],
    (142): [7, 14],
    (143): [7, 15],
    (144): [6, 15],
    (145): [6, 14],
    (146): [6, 13],
    (147): [6, 12],
    (148): [6, 11],
    (149): [6, 10],
    (150): [6, 9],
    (151): [6, 8],
    (152): [6, 7],
    (153): [6, 6],
    (154): [6, 5],
    (155): [6, 4],
    (156): [6, 3],
    (157): [6, 2],
    (158): [6, 1],
    (159): [6, 0],
    (160): [5, 0],
    (161): [5, 1],
    (162): [5, 2],
    (163): [5, 3],
    (164): [5, 4],
    (165): [5, 5],
    (166): [5, 6],
    (167): [5, 7],
    (168): [5, 8],
    (169): [5, 9],
    (170): [5, 10],
    (171): [5, 11],
    (172): [5, 12],
    (173): [5, 13],
    (174): [5, 14],
    (175): [5, 15],
    (176): [4, 15],
    (177): [4, 14],
    (178): [4, 13],
    (179): [4, 12],
    (180): [4, 11],
    (181): [4, 10],
    (182): [4, 9],
    (183): [4, 8],
    (184): [4, 7],
    (185): [4, 6],
    (186): [4, 5],
    (187): [4, 4],
    (188): [4, 3],
    (189): [4, 2],
    (190): [4, 1],
    (191): [4, 0],
    (192): [3, 0],
    (193): [3, 1],
    (194): [3, 2],
    (195): [3, 3],
    (196): [3, 4],
    (197): [3, 5],
    (198): [3, 6],
    (199): [3, 7],
    (200): [3, 8],
    (201): [3, 9],
    (202): [3, 10],
    (203): [3, 11],
    (204): [3, 12],
    (205): [3, 13],
    (206): [3, 14],
    (207): [3, 15],
    (208): [2, 15],
    (209): [2, 14],
    (210): [2, 13],
    (211): [2, 12],
    (212): [2, 11],
    (213): [2, 10],
    (214): [2, 9],
    (215): [2, 8],
    (216): [2, 7],
    (217): [2, 6],
    (218): [2, 5],
    (219): [2, 4],
    (220): [2, 3],
    (221): [2, 2],
    (222): [2, 1],
    (223): [2, 0],
    (224): [1, 0],
    (225): [1, 1],
    (226): [1, 2],
    (227): [1, 3],
    (228): [1, 4],
    (229): [1, 5],
    (230): [1, 6],
    (231): [1, 7],
    (232): [1, 8],
    (233): [1, 9],
    (234): [1, 10],
    (235): [1, 11],
    (236): [1, 12],
    (237): [1, 13],
    (238): [1, 14],
    (239): [1, 15],
    (240): [0, 15],
    (241): [0, 14],
    (242): [0, 13],
    (243): [0, 12],
    (244): [0, 11],
    (245): [0, 10],
    (246): [0, 9],
    (247): [0, 8],
    (248): [0, 7],
    (249): [0, 6],
    (250): [0, 5],
    (251): [0, 4],
    (252): [0, 3],
    (253): [0, 2],
    (254): [0, 1],
    (255): [0, 0]
}

# Crear una matriz de 16x16 con valores azules
matrix = np.zeros((16, 16, 3), dtype=np.uint8)




#Le llegan los puntos led_iz, led_de en formato matriz neopixel 16 x 16
def pinta_puntos_matriz(led_iz, led_de):

    # Crear una matriz de ceros de 16x16
    #matrix = np.zeros((16, 16))

    # Pasa puntos de formato neopixel a matriz matplotlib los deja en matrix
    for i, val in enumerate(led_iz):
        row = posicion_p_a_x_y[val][0]
        col = posicion_p_a_x_y[val][1]
        matrix[row, col] = 255

    for j, val in enumerate(led_de):
        row = posicion_p_a_x_y[val][0]
        col = posicion_p_a_x_y[val][1]
        matrix[row, col] = 255

    grafica_matriz(matrix)    # Graficar la matriz
    """
    plt.imshow(matrix)  # , cmap='hot', interpolation='nearest')
    # plt.colorbar()
    plt.axis('off')
    #plt.title('Valores LED')
    plt.show()
    #time.sleep(3)
    """

def prueba():
    # Valores LED
    led_iz = [133, 154, 165, 186, 197, 218, 228, 229]  # 1
    led_de = [137, 138, 148, 151, 168, 171, 180, 183, 200, 203, 212, 215, 233, 234]

    # Crear una matriz de ceros de 16x16
    matrix = np.zeros((16, 16))

    # Asignar los valores LED a la matriz
    for i, val in enumerate(led_iz):
        row = posicion_p_a_x_y[val][0]
        col = posicion_p_a_x_y[val][1]
        matrix[row, col] = 255

    for j, val in enumerate(led_de):
        row = posicion_p_a_x_y[val][0]
        col = posicion_p_a_x_y[val][1]
        matrix[row, col] = 255

    # Graficar la matriz
    plt.imshow(matrix)  # , cmap='hot', interpolation='nearest')
    # plt.colorbar()
    plt.axis('off')
    plt.title('Valores LED')
    #plt.show()
    plt.ion()
    plt.pause(5)
    plt.close()

def grafica_matriz(matrix):
    # Graficar la matriz
    plt.imshow(matrix)  # , cmap='hot', interpolation='nearest')
    # plt.colorbar()
    plt.axis('off')
    plt.title('Valores LED')
    #plt.show()
    plt.ion()
    plt.pause(1)




def limpia_matriz():
    #plt.clf()
    for x in range(16):
        for y in range(16):
            matrix[x, y] = [0, 0, 0]
    plt.show()
    # Mostrar la matriz como una imagen
    plt.imshow(matrix)
    plt.axis('off')



#prueba()
#prueba1()