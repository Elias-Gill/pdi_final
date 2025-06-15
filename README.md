# Reconocimiento de Jeroglificos

Este script detecta y clasifica jeroglíficos en imágenes binarias utilizando comparación por
similitud visual.

## Funcionamiento

Primero se carga los simbolos de referencia desde la carpeta `simbolos/`, donde cada archivo
representa un jeroglifico conocido.
Estas imagenes se convierten a blanco y negro, se recortan para eliminar el espacio vacío y
luego se redimensionan a un tamaño fijo de 64x64 píxeles.
Cada imagen es identificada con su letra correspondiente.

Luego, al procesar la imagen de entrada, se convierte también a formato binario.
Mediante un etiquetado de componentes conectadas, se aíslan los distintos jeroglíficos
presentes en la imagen.
Cada uno se recorta, se normaliza del mismo modo que los símbolos de referencia, y se compara
con ellos usando una operación XOR para medir diferencias.

Finalmente, se clasifica cada componente por similitud, asignándole la letra del símbolo más
parecido (el que tenga menor diferencia visual).
El resultado es una cadena de letras correspondientes a los jeroglíficos encontrados, ordenadas
alfabéticamente.

## Requisitos

* Python 3
* OpenCV (`opencv-python`)
* NumPy
* SciPy

Instalación rápida:

```bash
pip install numpy opencv-python scipy
```

## Uso

Ejecutar desde consola:

```bash
python main.py
```

El script cargará la imagen `Ejemplo1.png`, detectará los jeroglíficos y mostrará el resultado:

**Nota**:
Las imágenes de la carpeta `simbolos/` deben tener el nombre del símbolo (ej:
`ankh.png`), en minúsculas.
