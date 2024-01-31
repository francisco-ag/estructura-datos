#
# El método grid() 
# organiza los widgets en una cuadrícula. 
# Puedes especificar en qué fila y columna colocar el widget, y también ajustar 
# opciones como sticky para indicar la alineación.
#

import tkinter as tk

root = tk.Tk()
root.title("Ejemplo con grid()")

label = tk.Label(root, text="¡Hola, Tkinter!")
label.grid(row=0, column=0, sticky="nsew")

boton = tk.Button(root, text="Clic aquí")
boton.grid(row=1, column=1, sticky="nsew")

entrada = tk.Entry(root)
entrada.grid(row=2, column=2, sticky="nsew")

root.mainloop()