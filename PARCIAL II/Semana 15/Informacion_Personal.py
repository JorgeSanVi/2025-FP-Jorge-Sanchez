# Diccionario de Informacion Personal
# Paso 1: Creo un diccionario con datos ficticios
informacion_personal = {
    "nombre": "Jose Villa",
    "edad": "22 años",
    "ciudad": "Tena",
    "profesion": "Comerciante"
}
# Verificacion
print(informacion_personal)

# Paso 2: Accedo y modifico valores del diccionario

# Cambio el valor de la clave "ciudad" Quito
informacion_personal["ciudad"] = "Quito"

# Cambio el valor de la clave profesion "Programador"
informacion_personal["profesion"] = "Programador"

# Verificacion
print(informacion_personal)

# Paso 3: Verifico si la clave "telefono" existe
# Si no existe, se agrega un numero ficticio
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0944228899"

# Paso 4: Elimino la clave "edad" ya, que no me es necesaria
del informacion_personal["edad"]

# Verificacion
print(informacion_personal)

# Paso 5: Imprimo el diccionario final
print("Diccionario final despues de todas las operaciones")
print(informacion_personal)
