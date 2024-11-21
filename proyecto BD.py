ES LO MISMO DE LA IMAGEN SOLO SE LOS PASO PARA CUANDO YA NOS PONGAMOS A HACER EDITAR POR AQUI
import sqlite3

# Conectar a la base de datos (se crea si no existe)
conn = sqlite3.connect('eventos.db')
cursor = conn.cursor()

# Crear tabla de asistentes con cédula como clave primaria
cursor.execute('''CREATE TABLE IF NOT EXISTS asistentes (
                    cedula TEXT PRIMARY KEY,
                    nombre TEXT,
                    correo TEXT,
                    evento TEXT,
                    confirmacion BOOLEAN)''')

# Crear tabla de actividades (no cambia)
cursor.execute('''CREATE TABLE IF NOT EXISTS actividades (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT,
                    fecha TEXT,
                    hora TEXT,
                    ubicacion TEXT)''')

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()


import tkinter as tk
from tkinter import messagebox
import sqlite3

# Función para agregar o modificar un asistente
def agregar_asistente():
    nombre = entry_nombre.get()
    correo = entry_correo.get()
    cedula = entry_cedula.get()
    evento = combo_evento.get()
    confirmacion = var_confirmacion.get()

    if not nombre or not correo or not cedula or not evento:
        messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
        return

    conn = sqlite3.connect('eventos.db')
    cursor = conn.cursor()
    
    try:
        # Insertar nuevo asistente
        cursor.execute('INSERT INTO asistentes (cedula, nombre, correo, evento, confirmacion) VALUES (?, ?, ?, ?, ?)', 
                       (cedula, nombre, correo, evento, confirmacion))
        conn.commit()
        messagebox.showinfo("Éxito", "Asistente agregado exitosamente.")
    except sqlite3.IntegrityError:
        messagebox.showwarning("Error", "Ya existe un asistente con esa cédula.")

    conn.close()

    # Limpiar los campos
    entry_nombre.delete(0, tk.END)
    entry_correo.delete(0, tk.END)
    entry_cedula.delete(0, tk.END)
    var_confirmacion.set(False)
    combo_evento.set('')

# Función para editar datos del asistente
def editar_asistente():
    cedula = entry_cedula.get()
    nombre = entry_nombre.get()
    correo = entry_correo.get()
    evento = combo_evento.get()
    confirmacion = var_confirmacion.get()

    if not cedula or not nombre or not correo or not evento:
        messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
        return

    conn = sqlite3.connect('eventos.db')
    cursor = conn.cursor()
    
    # Actualizar datos del asistente
    cursor.execute('''UPDATE asistentes SET nombre = ?, correo = ?, evento = ?, confirmacion = ? WHERE cedula = ?''', 
                   (nombre, correo, evento, confirmacion, cedula))

    conn.commit()
    conn.close()

    messagebox.showinfo("Éxito", "Datos del asistente actualizados exitosamente.")

# Función para agregar actividad
def agregar_actividad():
    nombre_actividad = entry_nombre_actividad.get()
    fecha = entry_fecha.get()
    hora = entry_hora.get()
    ubicacion = entry_ubicacion.get()

    if not nombre_actividad or not fecha or not hora or not ubicacion:
        messagebox.showwarning("Advertencia", "Por favor, complete todos los campos de actividad.")
        return

    conn = sqlite3.connect('eventos.db')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO actividades (nombre, fecha, hora, ubicacion) VALUES (?, ?, ?, ?)', 
                   (nombre_actividad, fecha, hora, ubicacion))

    conn.commit()
    conn.close()

    # Limpiar campos de actividad
    entry_nombre_actividad.delete(0, tk.END)
    entry_fecha.delete(0, tk.END)
    entry_hora.delete(0, tk.END)
    entry_ubicacion.delete(0, tk.END)

    messagebox.showinfo("Éxito", "Actividad agregada exitosamente.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Formulario de Gestión de Evento")

# Crear campos para los asistentes
tk.Label(ventana, text="Cédula del Asistente:").grid(row=0, column=0, padx=10, pady=10)
entry_cedula = tk.Entry(ventana)
entry_cedula.grid(row=0, column=1, padx=10, pady=10)

tk.Label(ventana, text="Nombre del Asistente:").grid(row=1, column=0, padx=10, pady=10)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=1, column=1, padx=10, pady=10)

tk.Label(ventana, text="Correo del Asistente:").grid(row=2, column=0, padx=10, pady=10)
entry_correo = tk.Entry(ventana)
entry_correo.grid(row=2, column=1, padx=10, pady=10)

tk.Label(ventana, text="Evento al que asistirá:").grid(row=3, column=0, padx=10, pady=10)
combo_evento = tk.StringVar()
tk.OptionMenu(ventana, combo_evento, "Convención", "Seminario", "Boda", "Festival Cultural").grid(row=3, column=1, padx=10, pady=10)

tk.Label(ventana, text="Confirmación de Asistencia:").grid(row=4, column=0, padx=10, pady=10)
var_confirmacion = tk.BooleanVar()
tk.Checkbutton(ventana, variable=var_confirmacion).grid(row=4, column=1, padx=10, pady=10)

# Botón para agregar asistente
tk.Button(ventana, text="Agregar Asistente", command=agregar_asistente).grid(row=5, column=0, columnspan=2, pady=20)

# Botón para editar asistente
tk.Button(ventana, text="Editar Asistente", command=editar_asistente).grid(row=6, column=0, columnspan=2, pady=20)

# Crear campos para actividades
tk.Label(ventana, text="Nombre de la Actividad:").grid(row=7, column=0, padx=10, pady=10)
entry_nombre_actividad = tk.Entry(ventana)
entry_nombre_actividad.grid(row=7, column=1, padx=10, pady=10)

tk.Label(ventana, text="Fecha de la Actividad (YYYY-MM-DD):").grid(row=8, column=0, padx=10, pady=10)
entry_fecha = tk.Entry(ventana)
entry_fecha.grid(row=8, column=1, padx=10, pady=10)

tk.Label(ventana, text="Hora de la Actividad (HH:MM):").grid(row=9, column=0, padx=10, pady=10)
entry_hora = tk.Entry(ventana)
entry_hora.grid(row=9, column=1, padx=10, pady=10)

tk.Label(ventana, text="Ubicación de la Actividad:").grid(row=10, column=0, padx=10, pady=10)
entry_ubicacion = tk.Entry(ventana)
entry_ubicacion.grid(row=10, column=1, padx=10, pady=10)

# Botón para agregar actividad
tk.Button(ventana, text="Agregar Actividad", command=agregar_actividad).grid(row=11, column=0, columnspan=2, pady=20)

# Ejecutar la ventana
ventana.mainloop()

