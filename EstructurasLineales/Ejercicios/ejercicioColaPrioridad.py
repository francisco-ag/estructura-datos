import heapq

class SistemaPlanificaciónTareas:
    def __init__(self):
        # Inicializamos la cola 
        self.tareas = []

    def agregar_tarea(self, tarea, prioridad):
        # Encolar tareas
        heapq.heappush(
                self.tareas, 
                # item
                (prioridad, tarea)
            )

    def procesar_tareas(self):
        # Mostrar Tareas encoladas 
        while self.tareas:
            prioridad, tarea = heapq.heappop(self.tareas)
            print("Procesando tarea:", tarea, "(Prioridad:", prioridad, ")")

sistema = SistemaPlanificaciónTareas()
sistema.agregar_tarea("Comer", 4)
sistema.agregar_tarea("Despertar", 2)
sistema.agregar_tarea("Desayunar", 1)
sistema.agregar_tarea("Salir de Casa", 3)
sistema.procesar_tareas()
