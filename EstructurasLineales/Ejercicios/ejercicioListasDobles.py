
class NodoDoble:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar_al_principio(self, dato):
        nuevo_nodo = NodoDoble(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
            return
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza.anterior = nuevo_nodo
        self.cabeza = nuevo_nodo

    def agregar_al_final(self, dato):
        nuevo_nodo = NodoDoble(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
            return
        nuevo_nodo.anterior = self.cola
        self.cola.siguiente = nuevo_nodo
        self.cola = nuevo_nodo

    def imprimir_lista(self):
        actual = self.cabeza
        print("Cabeza",actual.dato)
        print("Cola", self.cola.dato)
        while actual:
            print(actual.dato, end=" <-> ")
            actual = actual.siguiente
        print("None")

# Ejemplo de uso
lista = ListaDoblementeEnlazada()
lista.agregar_al_principio(3)
lista.imprimir_lista()
lista.agregar_al_principio(2)
lista.imprimir_lista()
lista.agregar_al_final(4)
lista.imprimir_lista()
lista.agregar_al_final(5)
lista.imprimir_lista()
lista.agregar_al_principio(7)
lista.imprimir_lista()