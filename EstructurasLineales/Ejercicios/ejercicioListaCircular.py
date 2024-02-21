class NodoCancion:
    def __init__(self, nombre_cancion, duracion ):
        self.nombre_cancion = nombre_cancion
        self.duracion = duracion
        self.siguiente = None

class ListaReproduccion:
    def __init__ (self):
        self.cabeza = None 

    def agregar_canciones(self, nombre_cancion, duracion ):
        nueva_cancion = NodoCancion(nombre_cancion, duracion)

        if not self.cabeza:
            nueva_cancion.siguiente = nueva_cancion
            self.cabeza = nueva_cancion
        else :
            nueva_cancion.siguiente = self.cabeza.siguiente
            self.cabeza.siguiente = nueva_cancion
    
    def reproducir_lista(self):

        if not self.cabeza:
            print("Lista Vacía")
            return
        nodo_actual = self.cabeza

        while True:
            print("Reproduciendo: ", nodo_actual.nombre_cancion, 
                  "-Duración: ", nodo_actual.duracion)
            nodo_actual = nodo_actual.siguiente

            if(nodo_actual == self.cabeza):
                break

lista_reproduccion = ListaReproduccion()
lista_reproduccion.agregar_canciones("After Hours","4:00")
lista_reproduccion.agregar_canciones("Hotel California","5:00")
lista_reproduccion.agregar_canciones("Nuestra Aflicción","4:00")

print("Reproduccion inciada : ")
lista_reproduccion.reproducir_lista()

print(lista_reproduccion.cabeza.nombre_cancion)










