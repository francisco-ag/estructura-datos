import tkinter as tk
from tkinter import messagebox

class RestauranteApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestión de Restaurante")

        # Componentes de la interfaz
        self.label_empleados = tk.Label(self, text="Empleados:")
        self.lista_empleados = tk.Listbox(self)
        self.btn_agregar_empleado = tk.Button(self, text="Agregar Empleado", command=self.agregar_empleado)
        self.btn_eliminar_empleado = tk.Button(self, text="Eliminar Empleado", command=self.eliminar_empleado)

        # Posicionamiento de componentes
        self.label_empleados.pack()
        self.lista_empleados.pack()
        self.btn_agregar_empleado.pack()
        self.btn_eliminar_empleado.pack()

        # Datos de prueba
        self.lista_empleados.insert(tk.END, "Juan")
        self.lista_empleados.insert(tk.END, "María")
        self.lista_empleados.insert(tk.END, "Carlos")

    def agregar_empleado(self):
        nombre = tk.simpledialog.askstring("Agregar Empleado", "Ingrese el nombre del nuevo empleado:")
        if nombre:
            self.lista_empleados.insert(tk.END, nombre)

    def eliminar_empleado(self):
        seleccion = self.lista_empleados.curselection()
        if seleccion:
            indice = seleccion[0]
            empleado = self.lista_empleados.get(indice)
            confirmacion = messagebox.askyesno("Eliminar Empleado", f"¿Está seguro que desea eliminar a {empleado}?")
            if confirmacion:
                self.lista_empleados.delete(indice)

if __name__ == "__main__":
    app = RestauranteApp()
    app.mainloop()
