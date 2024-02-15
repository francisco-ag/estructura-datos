#Ejercicio Cola Circular 

from collections import deque

# Implementación de un simulador de rotación de empleados en turnos
def rotación_empleados(empleados, turnos):

    cola_empleados = deque(empleados)

    for _ in range(turnos):
        empleado_actual = cola_empleados.popleft()
        cola_empleados.append(empleado_actual)
        print("Empleado en turno:", cola_empleados[0])

# Ejemplo de uso
empleados = ["Francisco", "Rafa", "Irving", "Pedro"]
rotación_empleados(empleados, 21)
