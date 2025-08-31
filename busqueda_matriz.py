"""
Autor: Jorge Sánchez
Descripción breve: busco un número dentro de una matriz 3x3 y muestro su posición.
Notas: índices mostrados desde 1 para que sea más natural al leer.
"""

from typing import List, Tuple

MATRIZ: List[List[int]] = [
    [12, 5, 9],
    [7, 14, 3],
    [6, 10, 8]
]

def buscar_en_matriz(m: List[List[int]], objetivo: int) -> Tuple[bool, Tuple[int, int]]:
    # Recorro fila por fila y columna por columna
    for f, fila in enumerate(m):
        for c, valor in enumerate(fila):
            if valor == objetivo:
                # Devuelvo True y la posición en base 0
                return True, (f, c)
    return False, (-1, -1)

def main() -> None:
    print("Matriz actual:")
    for fila in MATRIZ:
        print(fila)

    try:
        objetivo = int(input("Ingresa el número a buscar: ").strip())
    except ValueError:
        print("Entrada inválida. Escribe un entero.")
        return

    encontrado, (f, c) = buscar_en_matriz(MATRIZ, objetivo)

    if encontrado:
        # Muestro posiciones en base 1 para lectura humana
        print(f"Encontré {objetivo} en fila {f+1}, columna {c+1}")
    else:
        print(f"{objetivo} no aparece en la matriz")

if __name__ == "__main__":
    main()
