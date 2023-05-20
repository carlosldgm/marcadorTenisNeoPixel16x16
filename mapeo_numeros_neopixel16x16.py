# ----------
# |si|sc|sd|
# ----------
# |ii|ic|id|
# ----------
#
#
# ----------
# | ti|td  |
# ----------
# | bi|bd  |
# ----------
numeros = {
    ("si", "0"): [129, 130, 156, 159, 160, 163, 188, 191, 192, 195, 220, 223, 225, 226],
    ("sc", "0"): [135, 136, 150, 153, 166, 169, 182, 185, 198, 201, 214, 217, 231, 232],
    ("sd", "0"): [141, 142, 144, 147, 172, 175, 176, 179, 204, 207, 208, 211, 237, 238],
    ("ii", "0"): [1, 2, 28, 31, 32, 35, 60, 63, 64, 67, 92, 95, 97, 98],
    ("ic", "0"): [7, 8, 22, 25, 38, 41, 54, 57, 70, 73, 86, 89, 103, 104],
    ("id", "0"): [13, 14, 16, 19, 44, 47, 48, 51, 76, 79, 80, 83, 109, 110],
    ("si", "1"): [130, 157, 162, 189, 194, 221, 225, 226],
    ("sc", "1"): [136, 151, 168, 183, 200, 215, 231, 232],
    ("sd", "1"): [142, 145, 174, 177, 206, 209, 237, 238],
    ("ii", "1"): [2, 29, 34, 61, 66, 93, 97, 98],
    ("ic", "1"): [8, 23, 40, 55, 72, 87, 103, 104],
    ("id", "1"): [14, 17, 46, 49, 78, 81, 109, 110],
    ("si", "2"): [129, 130, 131, 159, 160, 190, 194, 220, 224, 225, 226],
    ("sc", "2"): [135, 136, 137, 153, 166, 184, 200, 214, 230, 231, 232],
    ("sd", "2"): [141, 142, 143, 147, 172, 178, 206, 208, 236, 237, 238],
    ("ii", "2"): [1, 2, 3, 31, 32, 62, 66, 92, 96, 97, 98],
    ("ic", "2"): [7, 8, 9, 25, 38, 56, 72, 86, 102, 103, 104],
    ("id", "2"): [13, 14, 15, 19, 44, 50, 78, 80, 108, 109, 110],
    ("si", "3"): [129, 130, 156, 159, 163, 189, 195, 220, 223, 225, 226],
    ("sc", "3"): [135, 136, 150, 153, 169, 183, 201, 214, 217, 231, 232],
    ("sd", "3"): [141, 142, 144, 147, 175, 177, 207, 208, 211, 237, 238],
    ("ii", "3"): [141, 142, 144, 147, 175, 177, 207, 208, 211, 237, 238],
    ("ic", "3"): [7, 8, 22, 25, 41, 55, 73, 86, 89, 103, 104],
    ("id", "3"): [13, 14, 16, 19, 47, 49, 79, 80, 83, 109, 110],
    ("si", "4"): [131, 156, 163, 188, 189, 190, 192, 195, 220, 223, 224, 227],
    ("sc", "4"): [137, 150, 169, 182, 183, 184, 198, 201, 214, 217, 230, 233],
    ("sd", "4"): [143, 144, 175, 176, 177, 178, 204, 207, 208, 211, 236, 239],
    ("ii", "4"): [3, 28, 35, 60, 61, 62, 64, 67, 92, 95, 96, 99],
    ("ic", "4"): [9, 22, 41, 54, 55, 56, 70, 73, 86, 89, 102, 105],
    ("id", "4"): [15, 16, 47, 48, 49, 50, 76, 79, 80, 83, 108, 111],
    ("si", "5"): [129, 130, 156, 159, 163, 189, 190, 192, 223, 225, 226, 227],
    ("sc", "5"): [135, 136, 150, 153, 169, 183, 184, 198, 217, 231, 232, 233],
    ("sd", "5"): [141, 142, 144, 147, 175, 177, 178, 204, 211, 237, 238, 239],
    ("ii", "5"): [1, 2, 28, 31, 35, 61, 62, 64, 95, 97, 98, 99],
    ("ic", "5"): [7, 8, 22, 25, 41, 55, 56, 70, 89, 103, 104, 105],
    ("id", "5"): [13, 14, 16, 19, 47, 49, 50, 76, 83, 109, 110, 111],
    ("si", "6"): [129, 130, 156, 159, 160, 163, 189, 190, 191, 192, 223, 225, 226],
    ("sc", "6"): [135, 136, 150, 153, 166, 169, 183, 184, 185, 198, 217, 231, 232],
    ("sd", "6"): [141, 142, 144, 147, 172, 175, 177, 178, 179, 204, 211, 237, 238],
    ("ii", "6"): [1, 2, 28, 31, 32, 35, 61, 62, 63, 64, 95, 97, 98],
    ("ic", "6"): [7, 8, 22, 25, 38, 41, 55, 56, 57, 70, 89, 103, 104],
    ("id", "6"): [13, 14, 16, 19, 44, 47, 49, 50, 51, 76, 83, 109, 110],
    ("si", "7"): [130, 157, 162, 189, 195, 220, 224, 225, 226],
    ("sc", "7"): [136, 151, 168, 183, 201, 214, 230, 231, 232],
    ("sd", "7"): [142, 145, 174, 177, 207, 208, 236, 237, 238],
    ("ii", "7"): [2, 29, 34, 61, 67, 92, 96, 97, 98],
    ("ic", "7"): [8, 23, 40, 55, 73, 86, 102, 103, 104],
    ("id", "7"): [14, 17, 46, 49, 79, 80, 108, 109, 110],
    ("si", "8"): [129, 130, 156, 159, 160, 163, 189, 190, 192, 195, 220, 223, 225, 226],
    ("sc", "8"): [135, 136, 150, 153, 166, 169, 183, 184, 198, 201, 214, 217, 231, 232],
    ("sd", "8"): [141, 142, 144, 147, 172, 175, 177, 178, 204, 207, 208, 211, 237, 238],
    ("ii", "8"): [1, 2, 28, 31, 32, 35, 61, 62, 64, 67, 92, 95, 97, 98],
    ("ic", "8"): [7, 8, 22, 25, 38, 41, 55, 56, 70, 73, 86, 89, 103, 104],
    ("id", "8"): [13, 14, 16, 19, 44, 47, 49, 50, 76, 79, 80, 83, 109, 110],
    ("si", "9"): [129, 130, 156, 159, 163, 188, 189, 190, 191, 192, 195, 220, 223, 225, 226],
    ("sc", "9"): [135, 136, 150, 153, 169, 182, 183, 184, 185, 198, 201, 214, 217, 231, 232],
    ("sd", "9"): [141, 142, 144, 147, 175, 176, 177, 178, 179, 204, 207, 208, 211, 237, 238],
    ("ii", "9"): [1, 2, 28, 31, 35, 60, 61, 62, 63, 64, 67, 92, 95, 97, 98],
    ("ic", "9"): [7, 8, 22, 25, 41, 54, 55, 56, 57, 70, 73, 86, 89, 103, 104],
    ("id", "9"): [13, 14, 16, 19, 47, 48, 49, 50, 51, 76, 79, 80, 83, 109, 110],
    ("ti", "0"): [132, 133, 153, 156, 163, 166, 185, 188, 195, 198, 217, 220, 228, 229],
    ("td", "0"): [137, 138, 148, 151, 168, 171, 180, 183, 200, 203, 212, 215, 233, 234],
    ("bi", "0"): [4, 5, 25, 28, 35, 38, 57, 60, 67, 70, 89, 92, 100, 101],
    ("bd", "0"): [9, 10, 20, 23, 40, 43, 52, 55, 72, 75, 84, 87, 105, 106],
    ("ti", "1"): [133, 154, 165, 186, 197, 218, 228, 229],
    ("td", "1"): [138, 149, 170, 181, 202, 213, 233, 234],
    ("bi", "1"): [5, 26, 37, 58, 69, 90, 100, 101],
    ("bd", "1"): [10, 21, 42, 53, 74, 85, 105, 106],
    ("ti", "2"): [132, 133, 134, 156, 163, 187, 197, 217, 227, 228, 229],
    ("td", "2"): [137, 138, 139, 151, 168, 182, 202, 212, 232, 233, 234],
    ("bi", "2"): [4, 5, 6, 28, 35, 59, 69, 89, 99, 100, 101],
    ("bd", "2"): [9, 10, 11, 23, 40, 54, 74, 84, 104, 105, 106],
    ("ti", "3"): [132, 133, 153, 156, 166, 186, 198, 217, 220, 228, 229],
    ("td", "3"): [137, 138, 148, 151, 171, 181, 203, 212, 215, 233, 234],
    ("bi", "3"): [4, 5, 25, 28, 38, 58, 70, 89, 92, 100, 101],
    ("bd", "3"): [9, 10, 20, 23, 43, 53, 75, 84, 87, 105, 106],
    ("ti", "4"): [134, 153, 166, 185, 186, 187, 195, 198, 217, 220, 227, 230],
    ("td", "4"): [139, 148, 171, 180, 181, 182, 200, 203, 212, 215, 232, 235],
    ("bi", "4"): [6, 25, 38, 57, 58, 59, 67, 70, 89, 92, 99, 102],
    ("bd", "4"): [11, 20, 43, 52, 53, 54, 72, 75, 84, 87, 104, 107],
    ("ti", "5"): [132, 133, 153, 156, 166, 186, 187, 195, 220, 228, 229, 230],
    ("td", "5"): [137, 138, 148, 151, 171, 181, 182, 200, 215, 233, 234, 235],
    ("bi", "5"): [4, 5, 25, 28, 38, 58, 59, 67, 92, 100, 101, 102],
    ("bd", "5"): [9, 10, 20, 23, 43, 53, 54, 72, 87, 105, 106, 107],
    ("ti", "6"): [132, 133, 153, 156, 163, 166, 186, 187, 188, 195, 220, 228, 229],
    ("td", "6"): [137, 138, 148, 151, 168, 171, 181, 182, 183, 200, 215, 233, 234],
    ("bi", "6"): [4, 5, 25, 28, 35, 38, 58, 59, 60, 67, 92, 100, 101],
    ("bd", "6"): [9, 10, 20, 23, 40, 43, 53, 54, 55, 72, 87, 105, 106],
    ("ti", "7"): [133, 154, 165, 186, 198, 217, 227, 228, 229],
    ("td", "7"): [138, 149, 170, 181, 203, 212, 232, 233, 234],
    ("bi", "7"): [5, 26, 37, 58, 70, 89, 99, 100, 101],
    ("bd", "7"): [10, 21, 42, 53, 75, 84, 104, 105, 106],
    ("ti", "8"): [132, 133, 153, 156, 163, 166, 186, 187, 195, 198, 217, 220, 228, 229],
    ("td", "8"): [137, 138, 148, 151, 168, 171, 181, 182, 200, 203, 212, 215, 233, 234],
    ("bi", "8"): [4, 5, 25, 28, 35, 38, 58, 59, 67, 70, 89, 92, 100, 101],
    ("bd", "8"): [9, 10, 20, 23, 40, 43, 53, 54, 72, 75, 84, 87, 105, 106],
    ("ti", "9"): [132, 133, 153, 156, 166, 185, 186, 187, 188, 195, 198, 217, 220, 228, 229],
    ("td", "9"): [137, 138, 148, 151, 171, 180, 181, 182, 183, 200, 203, 212, 215, 233, 234],
    ("bi", "9"): [4, 5, 25, 28, 38, 57, 58, 59, 60, 67, 70, 89, 92, 100, 101],
    ("bd", "9"): [9, 10, 20, 23, 43, 52, 53, 54, 55, 72, 75, 84, 87, 105, 106],
    ("ti", "a"): [131, 134, 153, 156, 163, 166, 185, 186, 187, 188, 195, 198, 217, 220, 228, 229],
    ("td", "d"): [137, 138, 148, 150, 169, 171, 180, 182, 201, 203, 212, 214, 233, 234],
    ("bi", "a"): [3, 6, 25, 28, 35, 38, 57, 58, 59, 60, 67, 70, 89, 92, 100, 101],
    ("bd", "d"): [9, 10, 20, 22, 41, 43, 52, 54, 73, 75, 84, 86, 105, 106],
    ("ti", "A"): [131, 134, 153, 156, 163, 166, 185, 186, 187, 188, 195, 198, 217, 220, 228, 229],
    ("td", "D"): [137, 138, 148, 150, 169, 171, 180, 182, 201, 203, 212, 214, 233, 234],
    ("bi", "A"): [3, 6, 25, 28, 35, 38, 57, 58, 59, 60, 67, 70, 89, 92, 100, 101],
    ("bd", "D"): [9, 10, 20, 22, 41, 43, 52, 54, 73, 75, 84, 86, 105, 106],
    ("ti", ""): [],
    ("td", ""): [],
    ("bi", ""): [],
    ("bd", ""): [],
}


def devuelve_leds_para_digito(cuadrante, digito):
    return numeros[cuadrante, digito]


#print(devuelve_leds_para_digito("ti", "a"))

# #test1: recorre el diccionario mostrando todos los valores
# for clave in numeros:
#     valor = numeros[clave]
#     # Hacer algo con la clave y el valor
#     print("clave: ", clave, " ", valor)
