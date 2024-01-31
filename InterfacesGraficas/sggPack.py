
# El método pack() 
# organiza los widgets de forma relativa entre sí. 
# Puedes especificar opciones como side (lado) 
# para indicar en qué lado de la ventana colocar el widget.

import tkinter as tk

root = tk.Tk()
root.title("Ejemplo con pack()")

label = tk.Label(root, text="¡Hola, Tkinter!")
label.pack(side="top", fill="x")

#side recibe como parametros 'left', 'right', 'top', 'bottom'

boton = tk.Button(root, text="Clic aquí")
boton.pack(side="bottom", fill="both")

# entrada = tk.Entry(root)
# entrada.pack(side="top", fill="x")

root.mainloop()
