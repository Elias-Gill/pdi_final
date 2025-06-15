# Pasos de transformacion

- Leer imagen binaria (0 = blanco, 1 = negro).
- Detectar componentes conexas usando DFS/BFS o scipy.ndimage.label.
- Extraer cada componente y analizar su forma.
- Clasificar la forma en una de las seis categorías, usando características topológicas:
- Cantidad de agujeros internos (número de componentes blancos internos).
- Estructura general (por ejemplo:
  simetría, conexiones, proporciones).
- Euler number = número de componentes - número de agujeros.
- Asignar letra y guardar.
- Ordenar alfabéticamente y devolver cadena.
