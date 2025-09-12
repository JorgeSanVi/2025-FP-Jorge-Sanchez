# Función: promedios_por_ciudad
# Entrada: diccionario { ciudad: [t_sem1, t_sem2, t_sem3, t_sem4] }
# Salida: diccionario { ciudad: promedio_general }

def promedios_por_ciudad(datos):
    """
    Calcula el promedio de temperaturas por ciudad.
    :param datos: dict[str, list[float]]  ->  semanas por ciudad
    :return: dict[str, float]             ->  promedio por ciudad
    """
    resultados = {}
    for ciudad, semanas in datos.items():
        if not semanas:
            raise ValueError(f"La ciudad '{ciudad}' no tiene datos")
        resultados[ciudad] = sum(semanas) / len(semanas)
    return resultados


# --- Pruebas rápidas (3 ciudades x 4 semanas) ---
if __name__ == "__main__":
    datos = {
        "Quito": [18, 20, 19, 17],
        "Guayaquil": [28, 29, 30, 31],
        "Cuenca": [16, 17, 18, 16]
    }

    r = promedios_por_ciudad(datos)

    # Verificación básica
    esperado = {"Quito": 18.5, "Guayaquil": 29.5, "Cuenca": 16.75}
    for c in esperado:
        assert abs(r[c] - esperado[c]) < 1e-9

    # Salida legible
    print("Promedio de temperaturas por ciudad")
    print("-----------------------------------")
    for ciudad, prom in r.items():
        print(f"{ciudad}: {prom:.2f} °C")
