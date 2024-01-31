#
# El método place() 
# permite posicionar los widgets de forma 
# absoluta en la ventana. 
# Puedes especificar coordenadas x , y
# para determinar la posición del widget. 
#

import tkinter as tk

root = tk.Tk()
root.title("Ejemplo con place()")

label = tk.Label(root, text="¡Hola, Tkinter!")
label.place(x=10, y=10)

boton = tk.Button(root, text="Clic aquí")
boton.place(x=10, y=28)

entrada = tk.Entry(root)
entrada.place(x=10, y=70)

root.mainloop()