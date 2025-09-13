# temperaturas_3d.py
# Registro de temperaturas diarias con matriz 3D y funciones
# Autor: Estudiante de Tecnologías de la Información
# Objetivo: Calcular promedios de temperatura por ciudad y semana usando funciones en Python

# Listas de referencia
CIUDADES = ["Quito", "Guayaquil", "Cuenca"]
SEMANAS = ["Semana 1", "Semana 2", "Semana 3", "Semana 4"]
DIAS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Matriz 3D de temperaturas [ciudad][semana][día]
temperaturas = [
    [   # Quito
        [ {"day": "Lunes", "temp": 78}, {"day": "Martes", "temp": 80}, {"day": "Miércoles", "temp": 82},
          {"day": "Jueves", "temp": 79}, {"day": "Viernes", "temp": 85}, {"day": "Sábado", "temp": 88}, {"day": "Domingo", "temp": 92} ],
        [ {"day": "Lunes", "temp": 76}, {"day": "Martes", "temp": 79}, {"day": "Miércoles", "temp": 83},
          {"day": "Jueves", "temp": 81}, {"day": "Viernes", "temp": 87}, {"day": "Sábado", "temp": 89}, {"day": "Domingo", "temp": 93} ],
        [ {"day": "Lunes", "temp": 77}, {"day": "Martes", "temp": 81}, {"day": "Miércoles", "temp": 85},
          {"day": "Jueves", "temp": 82}, {"day": "Viernes", "temp": 88}, {"day": "Sábado", "temp": 91}, {"day": "Domingo", "temp": 95} ],
        [ {"day": "Lunes", "temp": 75}, {"day": "Martes", "temp": 78}, {"day": "Miércoles", "temp": 80},
          {"day": "Jueves", "temp": 79}, {"day": "Viernes", "temp": 84}, {"day": "Sábado", "temp": 87}, {"day": "Domingo", "temp": 91} ],
    ],
    [   # Guayaquil
        [ {"day": "Lunes", "temp": 62}, {"day": "Martes", "temp": 64}, {"day": "Miércoles", "temp": 68},
          {"day": "Jueves", "temp": 70}, {"day": "Viernes", "temp": 73}, {"day": "Sábado", "temp": 75}, {"day": "Domingo", "temp": 79} ],
        [ {"day": "Lunes", "temp": 63}, {"day": "Martes", "temp": 66}, {"day": "Miércoles", "temp": 70},
          {"day": "Jueves", "temp": 72}, {"day": "Viernes", "temp": 75}, {"day": "Sábado", "temp": 77}, {"day": "Domingo", "temp": 81} ],
        [ {"day": "Lunes", "temp": 61}, {"day": "Martes", "temp": 65}, {"day": "Miércoles", "temp": 68},
          {"day": "Jueves", "temp": 70}, {"day": "Viernes", "temp": 72}, {"day": "Sábado", "temp": 76}, {"day": "Domingo", "temp": 80} ],
        [ {"day": "Lunes", "temp": 64}, {"day": "Martes", "temp": 67}, {"day": "Miércoles", "temp": 69},
          {"day": "Jueves", "temp": 71}, {"day": "Viernes", "temp": 74}, {"day": "Sábado", "temp": 77}, {"day": "Domingo", "temp": 80} ],
    ],
    [   # Cuenca
        [ {"day": "Lunes", "temp": 90}, {"day": "Martes", "temp": 92}, {"day": "Miércoles", "temp": 94},
          {"day": "Jueves", "temp": 91}, {"day": "Viernes", "temp": 88}, {"day": "Sábado", "temp": 85}, {"day": "Domingo", "temp": 82} ],
        [ {"day": "Lunes", "temp": 89}, {"day": "Martes", "temp": 91}, {"day": "Miércoles", "temp": 93},
          {"day": "Jueves", "temp": 90}, {"day": "Viernes", "temp": 87}, {"day": "Sábado", "temp": 84}, {"day": "Domingo", "temp": 81} ],
        [ {"day": "Lunes", "temp": 91}, {"day": "Martes", "temp": 93}, {"day": "Miércoles", "temp": 95},
          {"day": "Jueves", "temp": 92}, {"day": "Viernes", "temp": 89}, {"day": "Sábado", "temp": 86}, {"day": "Domingo", "temp": 83} ],
        [ {"day": "Lunes", "temp": 88}, {"day": "Martes", "temp": 90}, {"day": "Miércoles", "temp": 92},
          {"day": "Jueves", "temp": 89}, {"day": "Viernes", "temp": 86}, {"day": "Sábado", "temp": 83}, {"day": "Domingo", "temp": 80} ],
    ],
]

# ---------------- FUNCIONES ----------------

def promedio_ciudad(data_ciudad):
    """Calcula el promedio general de una ciudad (todas sus semanas)."""
    suma = 0
    n = 0
    for semana in data_ciudad:
        for dia in semana:
            suma += dia["temp"]
            n += 1
    return suma / n if n else 0

def promedios_por_ciudad(data, ciudades):
    """Devuelve un diccionario con el promedio general de cada ciudad."""
    resultado = {}
    for i, ciudad in enumerate(data):
        resultado[ciudades[i]] = promedio_ciudad(ciudad)
    return resultado

def promedios_por_ciudad_y_semana(data, ciudades, semanas):
    """Devuelve un diccionario con los promedios por ciudad y semana."""
    resultado = {}
    for i_c, ciudad in enumerate(data):
        resultado[ciudades[i_c]] = {}
        for i_s, semana in enumerate(ciudad):
            suma = sum(d["temp"] for d in semana)
            resultado[ciudades[i_c]][semanas[i_s]] = suma / len(semana)
    return resultado

def imprimir_tabla(promedios):
    """Imprime una tabla con los promedios generales por ciudad."""
    print("Promedio general por ciudad")
    print("---------------------------")
    print(f"{'Ciudad':<12}{'Promedio (°F)':>15}")
    for ciudad, promedio in promedios.items():
        print(f"{ciudad:<12}{promedio:>15.2f}")

def imprimir_detalle(proms_semana):
    """Imprime los promedios detallados por ciudad y semana."""
    print("\nPromedio por ciudad y por semana")
    print("-------------------------------")
    for ciudad, semanas in proms_semana.items():
        for semana, valor in semanas.items():
            print(f"{ciudad:<12}{semana:<10}{valor:>10.2f} °F")

# ---------------- PROGRAMA PRINCIPAL ----------------

if __name__ == "__main__":
    proms = promedios_por_ciudad(temperaturas, CIUDADES)
    proms_sem = promedios_por_ciudad_y_semana(temperaturas, CIUDADES, SEMANAS)

    imprimir_tabla(proms)
    imprimir_detalle(proms_sem)

