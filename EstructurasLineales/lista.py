#Definicion :
# Es una estructura de datos enfocada en la busqueda de 
# un solo elemento, funciona como una coleccion de datos 
# Tiene operaciones CRUD 
#

lista = [10,20,30,40] 
print(lista)
# Insertar datos
lista.insert(1,15)
print(lista)
# Buscar datos
# Busca el dato almacenado y devuelve la posicion del index

posicion = lista.index(30)  #el dato enviado debe de existir dentro de la lista 
#print(posicion)

#Actualizar datos , especificando el index
lista[1] = 17
print(lista)

#Eliminar, un elemento segun el index
del lista[1]
print(lista)



