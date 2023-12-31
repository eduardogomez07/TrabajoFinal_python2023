import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import json

def option_selected(event):
    selected_option = option_var.get()
    selected_data = data[selected_option]
    name_label.config(text="Nombre: " + selected_data["nombre"])
    profile_image = Image.open(selected_data["foto_perfil.jpg"])  #no funciona todavia
    profile_photo = ImageTk.PhotoImage(profile_image)
    profile_label.config(image=profile_photo)
    profile_label.image = profile_photo

def add_lastname():
    selected_option = option_var.get()
    selected_data = data[selected_option]
    lastname = lastname_entry.get()
    selected_data["apellido"] = lastname
    new_name_label = ttk.Label(window, text="Nombre: " + selected_data["nombre"])
    new_name_label.pack()
    new_lastname_label = ttk.Label(window, text="Apellido: " + selected_data["apellido"])
    new_lastname_label.pack()

    with open('datos_nuevos.json', 'w') as file:
        json.dump(data, file)

# Leer el archivo JSON
with open('datos.json') as file:
    data = json.load(file)

# Crear la ventana
window = tk.Tk()
window.title("Barra desplegable de opciones")
window.geometry("800x800")  # Establecer el tamaño de la ventana

# Variable para almacenar la opción seleccionada
option_var = tk.StringVar()

# Obtener las opciones del archivo JSON
options = list(data.keys())

# Crear la barra desplegable
option_menu = ttk.OptionMenu(window, option_var, options[0], *options, command=option_selected)
option_menu.pack()

# Crear una etiqueta para mostrar el nombre seleccionado
name_label = ttk.Label(window, text="")
name_label.pack()

# Crear una etiqueta para mostrar la edad seleccionada
age_label = ttk.Label(window, text="")
age_label.pack()

# Crear una etiqueta para mostrar la foto de perfil
profile_label = ttk.Label(window)
profile_label.pack()

# Crear un cuadro de texto para ingresar el apellido
lastname_entry = ttk.Entry(window)
lastname_entry.pack()

# Crear un botón para agregar el apellido
add_button = ttk.Button(window, text="Agregar Apellido", command=add_lastname)
add_button.pack()

# Ejecutar la ventana
window.mainloop()
