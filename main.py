import os

import cv2
import numpy as np
import scipy

# Diccionario de etiquetas
CLASES = {
    "ankh": "A",
    "wedjat": "J",
    "djed": "D",
    "scarab": "S",
    "was": "W",
    "akeht": "K",
}


# Recorta la región de interés y la normaliza a un tamaño fijo
def normalizar_componente(comp):
    # recortar la imagen
    x, y = np.where(comp)  # buscar los pixeles distintos del fondo
    recorte = comp[min(x) : max(x) + 1, min(y) : max(y) + 1]

    # reescalar a 64x64 pixeles usando "nearest neighbor"
    return cv2.resize(
        recorte.astype(np.uint8), (64, 64), interpolation=cv2.INTER_NEAREST
    )


# Cargar los simbolos de referencia
path = "simbolos"
simbolos = {}
for nombre_archivo in os.listdir(path):
    nombre = os.path.splitext(nombre_archivo)[0].lower()
    if nombre in CLASES:
        imagen = cv2.imread(os.path.join(path, nombre_archivo), 0)
        _, binaria = cv2.threshold(imagen, 127, 1, cv2.THRESH_BINARY_INV)
        normalizada = normalizar_componente(binaria)
        simbolos[nombre] = normalizada.astype(np.uint8)


# Compara dos binarios usando XOR + conteo de diferencias
def diferencia_binaria(img1, img2):
    xor = cv2.bitwise_xor(img1, img2)
    return np.sum(xor)


# Clasifica un jeroglífico comparándolo con los símbolos
def clasificar(componente):
    componente = normalizar_componente(componente)
    mejor = "?"
    menor_dif = float("inf")
    for nombre, ref in simbolos.items():
        dif = diferencia_binaria(componente, ref)
        if dif < menor_dif:
            menor_dif = dif
            mejor = CLASES[nombre]
    return mejor


# Procesa la imagen principal
def reconocer_jeroglificos(path_imagen):
    # leer la imagen en formato binario e invertido
    _, img = cv2.threshold(cv2.imread(path_imagen, 0), 127, 1, cv2.THRESH_BINARY_INV)

    etiquetada, num = scipy.ndimage.label(img)
    encontrados = []

    # Por cada elemento etiquetado aplicar el reconocimiento
    for i in range(1, num + 1):
        # Extrae solo la imagen con dicha etiqueta
        componente = (etiquetada == i).astype(np.uint8)
        letra = clasificar(componente)
        encontrados.append(letra)

    return "".join(sorted(encontrados))


if __name__ == "__main__":
    path_imagen = "./Ejemplo2.png"  # Cambiar por la imagen a evaluar
    resultado = reconocer_jeroglificos(path_imagen)
    print("Resultado:", resultado)
