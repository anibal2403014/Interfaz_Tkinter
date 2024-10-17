import tkinter as tk
from tkinter import messagebox, filedialog

# Crear la ventana principal
root = tk.Tk()
root.title("Aplicación To-Do List")
root.geometry("400x500")
root.configure(bg='#2C2C2C')

# Lista para almacenar las tareas
tareas = []

# Función para añadir tareas automáticamente al seleccionar prioridad
def agregar_tarea_auto(*args):
    tarea = entrada_tarea.get()
    prioridad = combo_prioridad.get()
    if tarea != "" and prioridad != "Selecciona prioridad":
        tareas.append((tarea, prioridad))
        actualizar_lista()
        entrada_tarea.delete(0, tk.END)
        combo_prioridad.set("Selecciona prioridad")
    else:
        messagebox.showwarning("Advertencia", "Por favor ingresa una tarea y selecciona una prioridad")

# Función para actualizar la lista de tareas en la pantalla
def actualizar_lista():
    lista_tareas.delete(0, tk.END)
    for tarea, prioridad in tareas:
        color = obtener_color_prioridad(prioridad)
        lista_tareas.insert(tk.END, tarea)
        lista_tareas.itemconfig(tk.END, {'bg': color})

# Función para obtener el color de la prioridad
def obtener_color_prioridad(prioridad):
    if prioridad == "Urgente":
        return 'red'
    elif prioridad == "Importante":
        return 'yellow'
    elif prioridad == "General":
        return 'green'
    else:
        return 'white'

# Función para eliminar tareas seleccionadas
def eliminar_tarea():
    try:
        seleccion = lista_tareas.curselection()[0]
        tareas.pop(seleccion)
        actualizar_lista()
    except IndexError:
        messagebox.showwarning("Advertencia", "Por favor selecciona una tarea para eliminar")

# Función para eliminar todas las tareas
def eliminar_todas_tareas():
    global tareas
    tareas = []
    actualizar_lista()

# Función para exportar tareas a un archivo de texto
def exportar_tareas():
    archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if archivo:
        with open(archivo, 'w') as f:
            for tarea, prioridad in tareas:
                f.write(f"{tarea} ({prioridad})\n")

# Título de la aplicación
titulo = tk.Label(root, text="Lista de Tareas", font=("Arial", 18), bg='#2C2C2C', fg='white')
titulo.pack(pady=10)

# Frame para la entrada de tarea y selección de prioridad
frame_input = tk.Frame(root, bg='#2C2C2C')
frame_input.pack(pady=10)

# Caja de texto para ingresar tareas con placeholder
entrada_tarea = tk.Entry(frame_input, width=20)
entrada_tarea.insert(0, "Escribe tu actividad")  # Placeholder
entrada_tarea.grid(row=0, column=0, padx=5)

# Función para borrar el placeholder al hacer clic
def on_entry_click(event):
    if entrada_tarea.get() == "Escribe tu actividad":
        entrada_tarea.delete(0, tk.END)

# Función para restablecer el placeholder si no se escribe nada
def on_focusout(event):
    if entrada_tarea.get() == "":
        entrada_tarea.insert(0, "Escribe tu actividad")

entrada_tarea.bind('<FocusIn>', on_entry_click)
entrada_tarea.bind('<FocusOut>', on_focusout)

# ComboBox para seleccionar la prioridad con texto "Selecciona prioridad"
prioridades = ["Urgente", "Importante", "General"]
combo_prioridad = tk.StringVar(value="Selecciona prioridad")
prioridad_menu = tk.OptionMenu(frame_input, combo_prioridad, *prioridades)
prioridad_menu.config(width=15)
prioridad_menu.grid(row=0, column=1, padx=5)

# Se vincula el cambio de selección de prioridad a la función agregar tarea automáticamente
combo_prioridad.trace('w', agregar_tarea_auto)

# Lista de tareas con fondo blanco
lista_tareas = tk.Listbox(root, width=35, height=10, bg='white', fg='black')
lista_tareas.pack(pady=10)

# Frame para los botones de eliminar y exportar
frame_botones = tk.Frame(root, bg='#2C2C2C')
frame_botones.pack(pady=10)

# Botón para eliminar tareas seleccionadas
btn_eliminar = tk.Button(frame_botones, text="Eliminar Tarea", command=eliminar_tarea)
btn_eliminar.grid(row=0, column=1, padx=10)

# Botón para eliminar todas las tareas
btn_eliminar_todas = tk.Button(root, text="Eliminar Todas las Tareas", command=eliminar_todas_tareas)
btn_eliminar_todas.pack(pady=5)

# Botón para exportar las tareas
btn_exportar = tk.Button(root, text="Exportar Tareas", command=exportar_tareas)
btn_exportar.pack(pady=5)

# Mantener la ventana abierta
root.mainloop()
