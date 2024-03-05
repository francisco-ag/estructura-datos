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


class ColaCircular():
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def encolar(self, item):
        self.items.insert(0, item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None

    def ver_primero(self):
        return self.items[-1]

    def avanzar_turno(self):
        if not self.esta_vacia():
            self.items.append(self.items.pop(0))

class HistorialOrdenes:
    def __init__(self):
        self.pila_ordenes = []

    def agregar_orden(self, orden):
        self.pila_ordenes.append(orden)

    def deshacer_ultima_orden(self):
        if self.pila_ordenes:
            return self.pila_ordenes.pop()
        else:
            return None

class Orden:
    def __init__(self, plato, cantidad):
        self.plato = plato
        self.cantidad = cantidad

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

        # Definir la cola circular de turnos
        self.cola_turnos = ColaCircular()

        # Definir la pila para el historial de órdenes
        self.historial_ordenes = HistorialOrdenes()


        # Llamar métodos para definir Pestañas
        self.create_empleados_widgets()
        self.create_turnos_widgets()
        self.create_ordenes_widgets()
        self.create_historial_widgets()
        self.create_reservas_widgets()

        


    def create_empleados_widgets(self):
        # Pestaña Empleados
        frame_empleados = ttk.LabelFrame(self.tabEmpleados, text="Gestión de Empleados")
        frame_empleados.pack(padx=10, pady=10, fill="both", expand=True)

        lbl_nombre = tk.Label(frame_empleados, text="Nombre:")
        lbl_nombre.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_nombre = tk.Entry(frame_empleados)
        self.entry_nombre.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        btn_agregar = tk.Button(frame_empleados, text="Agregar Empleado", command=self.agregar_empleado)
        btn_agregar.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.listbox_empleados = tk.Listbox(frame_empleados)
        self.listbox_empleados.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

    def agregar_empleado(self):
        nombre_empleado = self.entry_nombre.get()
        if nombre_empleado:
            self.lista_empleados.agregar_al_principio(nombre_empleado.upper())
            self.actualizar_lista_empleados()
            self.entry_nombre.delete(0, tk.END)
            messagebox.showinfo("Información", "Empleado agregado exitosamente.")
        else:
            messagebox.showerror("Error", "Por favor ingresa el nombre del empleado.")

    def actualizar_lista_empleados(self):
        self.listbox_empleados.delete(0, tk.END)
        empleados = self.lista_empleados.obtener_lista()
        for empleado in empleados:
            self.listbox_empleados.insert(tk.END, empleado)

    def create_turnos_widgets(self):
        # Pestaña Turnos
        frame_turnos = ttk.Frame(self.tabTurnos)
        frame_turnos.pack(fill="both", expand=True)

        lbl_turno = tk.Label(frame_turnos, text="Turno:")
        lbl_turno.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_turno = tk.Entry(frame_turnos)
        self.entry_turno.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        btn_asignar_turno = tk.Button(frame_turnos, 
                                      text="Asignar Turno", 
                                      command=self.asignar_turno)
        btn_asignar_turno.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        btn_avanzar_turno = tk.Button(frame_turnos, text="Avanzar Turno",
                                       command=self.avanzar_turno)
        btn_avanzar_turno.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.listbox_turnos = tk.Listbox(frame_turnos)
        self.listbox_turnos.grid(row=3, column=0, columnspan=2, 
                                 padx=5, pady=5, sticky="nsew")

    def asignar_turno(self):
        turno = self.entry_turno.get()
        if turno:
            empleado = self.lista_empleados.obtener_lista().pop(0)
            self.cola_turnos.encolar((empleado, turno))
            self.actualizar_lista_turnos()
            self.entry_turno.delete(0, tk.END)
            messagebox.showinfo("Información", 
                                f"Turno {turno} asignado a {empleado}.")
        else:
            messagebox.showerror("Error", "Por favor ingresa el turno.")

    def avanzar_turno(self):
        if not self.cola_turnos.esta_vacia():
            empleado, turno = self.cola_turnos.desencolar()
            self.cola_turnos.avanzar_turno()
            self.actualizar_lista_turnos()
            messagebox.showinfo("Información", f"Avanzado al siguiente turno: {turno}.")

    def actualizar_lista_turnos(self):
        self.listbox_turnos.delete(0, tk.END)
        turnos = [f"{empleado}: {turno}" for empleado, turno in self.cola_turnos.items]
        for turno in turnos:
            self.listbox_turnos.insert(tk.END, turno)

    def create_ordenes_widgets(self):
        # Pestaña Órdenes
        frame_ordenes = ttk.LabelFrame(self.tabOrdenes, text="Realizar Orden")
        frame_ordenes.pack(padx=10, pady=10, fill="both", expand=True)

        # Etiquetas y entradas para los detalles de la orden
        lbl_plato = tk.Label(frame_ordenes, text="Plato:")
        lbl_plato.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_plato = tk.Entry(frame_ordenes)
        self.entry_plato.grid(row=0, column=1, padx=5, pady=5)

        lbl_cantidad = tk.Label(frame_ordenes, text="Cantidad:")
        lbl_cantidad.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_cantidad = tk.Entry(frame_ordenes)
        self.entry_cantidad.grid(row=1, column=1, padx=5, pady=5)

        # Botón para realizar la orden
        btn_realizar_orden = tk.Button(frame_ordenes, text="Realizar Orden", command=self.realizar_orden)
        btn_realizar_orden.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    def realizar_orden(self):
        plato = self.entry_plato.get()
        cantidad = self.entry_cantidad.get()

        if plato and cantidad:
            orden = Orden(plato, cantidad)
            self.historial_ordenes.agregar_orden(orden)
            messagebox.showinfo("Orden Realizada", f"Se ha realizado la orden: {cantidad} de {plato}")
            # Limpiar las entradas después de realizar la orden
            self.entry_plato.delete(0, tk.END)
            self.entry_cantidad.delete(0, tk.END)
            self.actualizar_listbox_historial()
        else:
            messagebox.showerror("Error", "Por favor ingresa el plato y la cantidad para realizar la orden.")

    def create_historial_widgets(self):
        # Pestaña Historial
        frame_historial = ttk.LabelFrame(self.tabHistorial, text="Historial Ordenes")
        frame_historial.pack(padx=10, pady=10, fill="both", expand=True)


        # Botón para deshacer la ultima orden
        btn_deshacer_orden = tk.Button(frame_historial, text="Deshacer Última Orden", command=self.deshacer_ultima_orden)
        btn_deshacer_orden.pack(padx=5, pady=5)

         # Listbox para mostrar el historial de órdenes
        self.listbox_historial = tk.Listbox(frame_historial, selectmode="none")
        self.listbox_historial.pack(padx=5, pady=5)
        self.actualizar_listbox_historial()

    def deshacer_ultima_orden(self):
        ultima_orden_deshacer = self.historial_ordenes.deshacer_ultima_orden()
        if ultima_orden_deshacer:
            messagebox.showinfo("Orden Deshecha", f"Se ha deshecho la última orden: {ultima_orden_deshacer.cantidad}  {ultima_orden_deshacer.plato}")
            self.actualizar_listbox_historial()
        else:
            messagebox.showinfo("Historial Vacío", "No hay órdenes para deshacer.")

    def actualizar_listbox_historial(self):
        # Limpiar el Listbox
        self.listbox_historial.delete(0, tk.END)

        # Obtener la pila de órdenes
        pila_ordenes = self.historial_ordenes.pila_ordenes

        # Agregar las órdenes al Listbox
        for orden in reversed(pila_ordenes):
            self.listbox_historial.insert(0, orden.cantidad+"   "+orden.plato)



    def create_reservas_widgets(self):
        # Pestaña Reservas
        pass


if __name__ == "__main__":
    app = RestauranteApp()
    app.minsize(380, 400)
    app.mainloop()
