#Definicion :
# Estructura de datos que almacena los datos
# encimando uno tras de otro 
# Usa el principio LIFO
#

pila = [] #definimos nuestra pila vacia

#PUSH - operacion para agregar elementos

pila.append(18)
pila.append(25)
pila.append(56)
#print(pila)
peek  = pila.pop()
#print("El elemento sacado de la pila fue", peek) 


pilaString = []
pilaString.append('Rafa')
pilaString.append('Irving')
pilaString.append('Pedro')
pilaString.append('Francisco')
print(pilaString) #antes del pop()
pilaString.pop()
print(pilaString) #despues del pop()
cima = pilaString.pop()
print("La cima es", cima) 









