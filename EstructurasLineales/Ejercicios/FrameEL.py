import tkinter as tk

class FrameEL(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.ordenes = []

        self.texto_label = tk.Label(self, 
                 text="Orden actual:")
        self.texto_label.pack()

        self.texto_var = tk.StringVar()
        self.texto_label_actual = tk.Label(
            self, textvariable=self.texto_var)
        self.texto_label_actual.pack()

        self.boton_opcion1 = tk.Button(
            self, 
            text="Opción 1",
            command=self.agregar_opcion1)
        self.boton_opcion1.pack()

        self.boton_opcion2 = tk.Button(
            self, 
            text="Opción 2",
            command=self.agregar_opcion2)
        self.boton_opcion2.pack()

    
    def agregar_opcion1(self):
        texto_nuevo = 'Opcion 1 '
        self.ordenes.append(texto_nuevo)
        self.actualizar_orden()

    def agregar_opcion2(self):
        texto_nuevo = 'Opcion 2 '
        self.ordenes.append(texto_nuevo)
        self.actualizar_orden()


    def actualizar_orden(self):
        texto_actual = ''.join(self.ordenes)
        self.texto_var.set(texto_actual)

root = tk.Tk()
editor_frame = FrameEL(master=root)
editor_frame.pack()
root.mainloop()
