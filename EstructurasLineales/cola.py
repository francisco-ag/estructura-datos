#Definicion :
# Estructura de datos que simula una fila
# los elementos salen como fueron llegando
# Usa el principio FIFO
#

from collections import deque

cola = deque()

# encolar
cola.append('Rafa')
cola.append('Irving')
cola.append('Pedro')
cola.append('Willmar')
print(cola)

# desencolar
elemento = cola.popleft()
print(elemento)
