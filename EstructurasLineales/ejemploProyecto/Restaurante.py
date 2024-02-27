import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class NodoListaEnlazada():
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None



class ListaEnlazada():
    def __init__(self):
        self.cabeza = None

    def agregar_al_principio(self, dato):
        
        nuevo_nodo = NodoListaEnlazada(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def eliminar(self, dato):
        actual = self.cabeza
        previo = None
        while actual and actual.dato != dato:
            previo = actual
            actual = actual.siguiente
        if actual:
            if previo:
                previo.siguiente = actual.siguiente
            else:
                self.cabeza = actual.siguiente
    
    def mostrar_lista(self):
        actual = self.cabeza    
        while actual:
            print(actual.dato)
            actual = actual.siguiente
    
    def obtener_lista(self):
        lista = []
        actual = self.cabeza
        while actual:
            lista.append(actual.dato)
            actual = actual.siguiente
        return lista

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

        # Definir la lista enlazada de empleados
        self.lista_empleados = ListaEnlazada()

        # Llamar metodos para definir Pestañas
        self.create_empleados_widgets()
        self.create_turnos_widgets()
        self.create_ordenes_widgets()
        self.create_historial_widgets()
        self.create_reservas_widgets()

        

    def create_empleados_widgets(self):

        # Pestaña Empleados
        # Crear un Frame para los widgets de empleados
        frame_empleados = ttk.LabelFrame(self.tabEmpleados, text="Gestión de Empleados")
        frame_empleados.pack(padx=10, pady=10, fill="both", expand=True)

        # Etiqueta y entrada para el nombre del empleado
        lbl_nombre = tk.Label(frame_empleados, text="Nombre:")
        lbl_nombre.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_nombre = tk.Entry(frame_empleados)
        self.entry_nombre.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        # Botón para agregar un nuevo empleado
        btn_agregar = tk.Button(frame_empleados, text="Agregar Empleado", command=self.agregar_empleado)
        btn_agregar.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

         # Crear un Listbox para mostrar los empleados
        self.listbox_empleados = tk.Listbox(frame_empleados)
        self.listbox_empleados.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")


    def agregar_empleado(self):
        # Obtener el nombre del empleado ingresado en la entrada
        nombre_empleado = self.entry_nombre.get()

        # Verificar si se ingresó un nombre
        if nombre_empleado:
            # Crear un nuevo nodo con el nombre del empleado
            #nuevo_empleado = NodoListaEnlazada(nombre_empleado)
            
            # Agregar el nuevo empleado a la lista enlazada de empleados
            self.lista_empleados.agregar_al_principio(nombre_empleado)

            # Actualizar la visualización de la lista de empleados
            self.actualizar_lista_empleados()


            # Limpiar la entrada después de agregar el empleado
            self.entry_nombre.delete(0, tk.END)

            self.lista_empleados.mostrar_lista()

            empleados = []
            empleados.append(self.lista_empleados.mostrar_lista())

            messagebox.showinfo("Infor","Guardado exitosamente")


        else:
            # Mostrar un mensaje de error si no se ingresó un nombre
            messagebox.showerror("Error", "Por favor ingresa el nombre del empleado.")

    def actualizar_lista_empleados(self):
        # Limpiar el contenido actual del Listbox
        self.listbox_empleados.delete(0, tk.END)
        
        # Obtener la lista de empleados y agregarlos al Listbox
        empleados = self.lista_empleados.obtener_lista()
        for empleado in empleados:
            self.listbox_empleados.insert(tk.END, empleado)


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
