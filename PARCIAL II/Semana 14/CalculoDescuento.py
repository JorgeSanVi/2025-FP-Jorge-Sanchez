# Archivo: CalculoDescuentoPython.py

# Programa para calcular descuentos en compras

def calcular_descuento(monto_total, porcentaje_descuento=10):
    # Calcula el valor del descuento
    return monto_total * (porcentaje_descuento / 100)

# Primera llamada: usando el descuento por defecto (10%)

monto1 = 200
descuento1 = calcular_descuento(monto1)
print("Compra 1")
print("Monto total:", monto1)
print("Descuento aplicado:", descuento1)
print("Monto final a pagar:", monto1 - descuento1)

print()   # Linea en blanco

# Segunda llamada: usando un porcentaje personalizado (15%)

monto2 = 350
descuento2 = calcular_descuento(monto2, 15)
print("compra2")
print("Monto total:", monto2)
print("Descuento aplicado:", descuento2)
print("Monto final a pagar:", monto2 - descuento2)
