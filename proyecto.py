NO SE QUE HICE LOCAS PERO ES UN CODIGO RANDOM NOMAS
import sqlite3

# Conectar a la base de datos (se crea si no existe)
conn = sqlite3.connect('evento.db')
cursor = conn.cursor()

# Crear la tabla de asistentes
cursor.execute('''CREATE TABLE IF NOT EXISTS asistentes (
                    id INTEGER PRIMARY KEY,
                    nombre TEXT,
                    contacto TEXT,
                    confirmacion BOOLEAN)''')

# Crear la tabla de actividades
cursor.execute('''CREATE TABLE IF NOT EXISTS actividades (
                    id INTEGER PRIMARY KEY,
                    nombre TEXT,
                    horario TEXT,
                    ubicacion TEXT,
                    recursos TEXT)''')

# Guardar cambios y cerrar conexión
conn.commit()
conn.close()

import tkinter as tk
from tkinter import messagebox
import sqlite3

# Función para agregar o actualizar registros de asistentes
def agregar_asistente():
    nombre = entry_nombre.get()
    contacto = entry_contacto.get()
    confirmacion = var_confirmacion.get()

    # Verificar que todos los campos estén llenos
    if not nombre or not contacto:
        messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
        return

    # Conectar a la base de datos
    conn = sqlite3.connect('evento.db')
    cursor = conn.cursor()

    # Insertar o actualizar el registro
    cursor.execute('INSERT INTO asistentes (nombre, contacto, confirmacion) VALUES (?, ?, ?)', 
                   (nombre, contacto, confirmacion))

    conn.commit()
    conn.close()

    # Limpiar los campos después de guardar
    entry_nombre.delete(0, tk.END)
    entry_contacto.delete(0, tk.END)
    var_confirmacion.set(False)

    messagebox.showinfo("Éxito", "Asistente agregado exitosamente.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Formulario de Gestión de Evento")

# Etiquetas y campos de entrada
tk.Label(ventana, text="Nombre del asistente:").grid(row=0, column=0, padx=10, pady=10)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1, padx=10, pady=10)

tk.Label(ventana, text="Contacto del asistente:").grid(row=1, column=0, padx=10, pady=10)
entry_contacto = tk.Entry(ventana)
entry_contacto.grid(row=1, column=1, padx=10, pady=10)

tk.Label(ventana, text="Confirmación de asistencia:").grid(row=2, column=0, padx=10, pady=10)
var_confirmacion = tk.BooleanVar()
tk.Checkbutton(ventana, variable=var_confirmacion).grid(row=2, column=1, padx=10, pady=10)

# Botón para agregar al asistente
tk.Button(ventana, text="Agregar Asistente", command=agregar_asistente).grid(row=3, column=0, columnspan=2, pady=20)

# Ejecutar la interfaz
ventana.mainloop()
