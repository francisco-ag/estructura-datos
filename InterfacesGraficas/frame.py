import tkinter as tk
from tkinter import messagebox

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Uso de Frame")

        # Crear un frame con tamaño específico
        self.frame = tk.Frame(root, width=200, height=150, padx=20, pady=20)
        self.frame.pack(padx=10, pady=10)

        # Widgets dentro del frame
        self.label1 = tk.Label(self.frame, text="Etiqueta 1")
        self.label1.grid(row=0, column=0)

        self.label2 = tk.Label(self.frame, text="Etiqueta 2")
        self.label2.grid(row=0, column=1)

        self.boton = tk.Button(self.frame, text="Botón", command=self.hacer_algo)
        self.boton.grid(row=1, columnspan=2)

        self.resultado   = tk.StringVar()




    def hacer_algo(self):
        print("Haciendo algo...")
        messagebox.showwarning("Mensaje", "Este es un mensaje de error.")


# Crear ventana principal
root = tk.Tk()

# Iniciar la aplicación y pasar la ventana principal
app = App(root)

# Establecer tamaño mínimo de la ventana principal
root.minsize(300, 200)

# Ejecutar el bucle principal
root.mainloop()
