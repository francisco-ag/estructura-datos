import tkinter as tk

def boton_clic():
    print("Botón clickeado")
def boton_texto():
    print("Botón clickeado")
# Crear ventana principal
root = tk.Tk()
root.title("Mi Aplicación Tkinter")

# # Añadir widgets a la ventana
# label = tk.Label(root, text="¡Hola, Tkinter!")

# # Configurar el sistema de gestión de geometría
# label.pack()

boton = tk.Button(root, text="Clic aquí", command=boton_clic)
boton.pack()

# boton = tk.Button(root, text="Mostrar texto", command=boton_texto)
# boton.pack()

entrada = tk.Entry(root)
entrada.pack()

# Ejecutar el bucle principal
root.mainloop()
