"""
Autor: Jorge Sánchez
Descripción breve: ordeno en forma ascendente una fila específica de una matriz 3x3
usando el algoritmo de inserción (Insertion Sort) implementado a mano.
"""

from typing import List

MATRIZ: List[List[int]] = [
    [15, 2, 11],
    [4, 13, 7],
    [9, 1, 10]
]

def insercion(lista: List[int]) -> List[int]:
    # Copio para no tocar el original
    a = lista[:]
    for i in range(1, len(a)):
        clave = a[i]
        j = i - 1
        # Muevo a la derecha los mayores que 'clave'
        while j >= 0 and a[j] > clave:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = clave
    return a

def ordenar_fila(m: List[List[int]], fila_idx: int) -> List[List[int]]:
    if not (0 <= fila_idx < len(m)):
        raise IndexError("Índice de fila fuera de rango")

    print("Matriz original:")
    for fila in m:
        print(fila)

    resultado = [fila[:] for fila in m]
    resultado[fila_idx] = insercion(resultado[fila_idx])

    print(f"\nFila {fila_idx+1} ordenada ascendente:")
    for fila in resultado:
        print(fila)

    return resultado

def main() -> None:
    try:
        fila = int(input("Elige la fila a ordenar (1, 2 o 3): ").strip())
        # Convierto a índice base 0
        ordenar_fila(MATRIZ, fila - 1)
    except ValueError:
        print("Entrada inválida. Escribe 1, 2 o 3.")
    except IndexError as e:
        print(e)

if __name__ == "__main__":
    main()
