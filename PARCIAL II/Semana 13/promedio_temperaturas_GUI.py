# Tarea Individual: Desarrollo de Función para Calcular Temperaturas Promedio
# Estudiante: Jorge Sánchez
# Semana 13 - Fundamentos de Programación


import tkinter as tk
from tkinter import messagebox

datos = []  # lista para guardar temperaturas

def agregar():
    try:
        valor = float(entrada.get())
        datos.append(valor)
        lista.insert(tk.END, valor)
        entrada.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido")

def eliminar():
    seleccion = lista.curselection()
    if seleccion:  # Si hay algo seleccionado, borra solo ese
        index = seleccion[0]
        lista.delete(index)
        datos.pop(index)
    else:  # Si no selecciona nada, limpia la lista completa
        if datos:
            lista.delete(0, tk.END)
            datos.clear()
        else:
            messagebox.showwarning("Atención", "No hay datos para borrar")

def calcular():
    if datos:
        promedio = sum(datos) / len(datos)
        lbl.config(text=f"🌡 Promedio: {promedio:.2f} °C")
    else:
        messagebox.showwarning("Atención", "No hay datos")

# Ventana
ventana = tk.Tk()
ventana.title("Gestión de Temperaturas")
ventana.geometry("500x400")
ventana.configure(bg="#f4f6f7")  # color de fondo suave

# Etiqueta principal
titulo = tk.Label(
    ventana,
    text="🌞 Promedio de Temperaturas 🌧",
    font=("Arial Rounded MT Bold", 16),
    bg="#f4f6f7",
    fg="#2c3e50"
)
titulo.pack(pady=10)

# Entrada
entrada = tk.Entry(ventana, font=("Arial", 12), justify="center", bg="#eaf2f8")
entrada.pack(pady=5)

# Botones
frame = tk.Frame(ventana, bg="#f4f6f7")
frame.pack(pady=10)

tk.Button(frame, text="➕ Agregar", command=agregar, bg="#58d68d", fg="white", font=("Arial", 11, "bold")).grid(row=0, column=0, padx=10)
tk.Button(frame, text="🗑 Eliminar", command=eliminar, bg="#e74c3c", fg="white", font=("Arial", 11, "bold")).grid(row=0, column=1, padx=10)
tk.Button(frame, text="📊 Calcular", command=calcular, bg="#5dade2", fg="white", font=("Arial", 11, "bold")).grid(row=0, column=2, padx=10)

# Lista
tk.Label(ventana, text="📋 Datos ingresados:", bg="#f4f6f7", fg="#2c3e50", font=("Arial", 12, "bold")).pack(pady=5)
lista = tk.Listbox(
    ventana,
    width=35,
    height=8,
    bg="#fdfefe",
    fg="#2c3e50",
    font=("Arial", 11),
    selectbackground="#3498db",
    selectforeground="white",
    relief="flat",
    highlightthickness=2,
    highlightbackground="#95a5a6",
    highlightcolor="#3498db"
)
lista.pack(pady=5)

# Resultado
lbl = tk.Label(ventana, text="🌡 Promedio: -", font=("Arial", 13, "bold"), bg="#f4f6f7", fg="#1a5276")
lbl.pack(pady=15)

ventana.mainloop()
