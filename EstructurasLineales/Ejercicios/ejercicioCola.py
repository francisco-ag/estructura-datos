from collections import deque
# Implementación de un sistema de gestión de tareas pendientes
class SistemaGestiónTareas:
    def __init__(self):
        self.tareas_pendientes = deque()
    def agregar_tarea(self, tarea):
        self.tareas_pendientes.append(tarea)
        print(self.tareas_pendientes)
    def procesar_tareas(self):
        while self.tareas_pendientes:
            tarea = self.tareas_pendientes.popleft()
            print("Procesando tarea:", tarea)

# Ejemplo de uso
sistema = SistemaGestiónTareas()
sistema.agregar_tarea("Bañarse")
sistema.agregar_tarea("Desayunar")
sistema.agregar_tarea("Tender cama")
sistema.procesar_tareas()
