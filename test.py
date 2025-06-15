import os

from main import CLASES, reconocer_jeroglificos

# Diccionario inverso para obtener nombre desde letra
INV_CLASES = {v: k for k, v in CLASES.items()}


def test_simbolos_individuales():
    simbolos_path = "simbolos"
    errores = 0

    for archivo in os.listdir(simbolos_path):
        nombre = os.path.splitext(archivo)[0].lower()
        esperado = CLASES.get(nombre)
        if esperado is None:
            continue  # Archivo no corresponde a un símbolo definido

        ruta_imagen = os.path.join(simbolos_path, archivo)
        resultado = reconocer_jeroglificos(ruta_imagen)

        if len(resultado) != 1:
            print(
                f'- Símbolo "{nombre}": resultado inválido "{resultado}", se esperaba "{esperado}"'
            )
            errores += 1
        elif resultado != esperado:
            simbolo_obtenido = INV_CLASES.get(resultado, "?").capitalize()
            print(
                f'- Símbolo "{nombre}": clasificado como "{resultado}" ({simbolo_obtenido}), se esperaba "{esperado}"'
            )
            errores += 1

    if errores == 0:
        print(
            "\033[92mOK\033[0m: Todos los símbolos fueron clasificados correctamente."
        )
    else:
        print(f"\033[91m{errores} errores detectados.\033[0m")


test_simbolos_individuales()
