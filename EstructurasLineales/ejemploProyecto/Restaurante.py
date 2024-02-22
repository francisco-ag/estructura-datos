import tkinter as tk
from tkinter import ttk

class RestauranteApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Aplicación de Restaurante")
        self.tabControl = ttk.Notebook(self)

        self.tabEmpleados = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tabEmpleados, text="Empleados")

        self.tabTurnos = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tabTurnos, text="Turnos")

        self.tabOrdenes = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tabOrdenes, text="Órdenes")

        self.tabHistorial = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tabHistorial, text="Historial")

        self.tabReservas = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tabReservas, text="Reservas")

        # Acomodar Pestañas
        self.tabControl.pack(expand=1, fill="both")

        # Llamar metodos para definir Pestañas
        self.create_empleados_widgets()     
        self.create_turnos_widgets()
        self.create_ordenes_widgets()
        self.create_historial_widgets()
        self.create_reservas_widgets()

    

        
    def create_empleados_widgets(self):
        # Pestaña Empleados
        print("hola")
        pass
    
    def create_turnos_widgets(self):
        # Aquí crearías los widgets para la pestaña de turnos
        pass

    def create_ordenes_widgets(self):
        # Aquí crearías los widgets para la pestaña de órdenes
        pass

    def create_historial_widgets(self):
        # Aquí crearías los widgets para la pestaña de historial
        pass

    def create_reservas_widgets(self):
        # Aquí crearías los widgets para la pestaña de reservas
        pass
        
if __name__ == "__main__":
    app = RestauranteApp()
    app.minsize(600, 400)
    app.mainloop()
    