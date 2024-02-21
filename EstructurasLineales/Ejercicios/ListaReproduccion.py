
class NodoCancion:
    def __init__(self, titulo, artista):
        self.artista = artista
        self.titulo = titulo
        self.siguiente = None
class ListaReproduccion:
    def __init__(self):
        self.cabeza = None

    def agregar_cancion(self, titulo, artista):
        nueva_cancion = NodoCancion(titulo, artista)

        if not self.cabeza:
            self.cabeza = nueva_cancion
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nueva_cancion

    def reproducir_siguiente(self):
        if self.cabeza:
            print("Reproduciendo:", self.cabeza.titulo, "-", self.cabeza.artista)
            self.cabeza = self.cabeza.siguiente
        else:
            print("La lista de reproducción está vacía.")

    def eliminar_cancion(self, titulo):
        if not self.cabeza:
            print("La lista de reproducción está vacía.")
            return

        if self.cabeza.titulo == titulo:
            self.cabeza = self.cabeza.siguiente
            return

        anterior = self.cabeza
        actual = self.cabeza.siguiente
        while actual:
            if actual.titulo == titulo:
                anterior.siguiente = actual.siguiente
                return
            anterior = actual
            actual = actual.siguiente

        print("La canción", titulo, "no se encontró en la lista de reproducción.")

    def mostrar_lista_reproduccion(self):
        if not self.cabeza:
            print("La lista de reproducción está vacía.")
            return
        print("Lista de Reproducción:")
        actual = self.cabeza
        while actual:
            print("-", actual.titulo, "-", actual.artista)
            actual = actual.siguiente

# Ejemplo de uso
lista = ListaReproduccion()
lista.agregar_cancion("Bohemian Rhapsody", "Queen")
lista.agregar_cancion("Hotel California", "Eagles")
lista.agregar_cancion("Imagine", "John Lennon")
lista.agregar_cancion("Stairway to Heaven", "Led Zeppelin")
lista.mostrar_lista_reproduccion()
lista.reproducir_siguiente()
lista.mostrar_lista_reproduccion()
lista.eliminar_cancion("Imagine")
lista.mostrar_lista_reproduccion()
lista.reproducir_siguiente()
lista.mostrar_lista_reproduccion()
lista.reproducir_siguiente()
lista.mostrar_lista_reproduccion()