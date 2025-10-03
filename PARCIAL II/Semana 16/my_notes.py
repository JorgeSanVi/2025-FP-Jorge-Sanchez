# Trabajos con Archivos de texto en Python

# 1 ESCRITURA EN EL ARCHIVO

# Abrimos my_notes.txt en como de escritura ("w")
archivo = open("my_notes.txt" , "w")

# Escribo almenos tres notas personales
archivo.write("Nota 1: Hoy estoy practicando como leer archivos en python.\n")
archivo.write("Nota 2: Aprendi a leer linea por linea con readline().\n")
archivo.write("Nota 3: Recorde la importancia de cerrar los archivos en python.\n")

# Cerramos el archivo luego de escribir
archivo.close()

# 2 LECTURA DEL ARCHIVO

# Abrimos el archivo en modo de lectura ("r")
archivo = open("my_notes.txt", "r")

print("contenido de archivo my_notes.txt:")

# Leemos linea por linea con readline ()
linea = archivo.readline()
while linea:
    print(linea.strip()) # strip elimina saltos de linea extra
    linea = archivo.readline()

# Cerramos el archivo despues de leer
archivo.close()

# 3 CIERRE DE ARCHIVOS

# En cada operacion se usa close() para asegurar el cierre
print("El programa termino correctamente y los archivos se cerraron.")