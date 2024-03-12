class NodoArbol:
    def __init__(self, valor):
        self.valor= valor
        self.izquierda = None
        self.derecha = None

class Arbol:

    # def preorden(NodoArbol):
    #     if (NodoArbol is not None):
    #         print(NodoArbol.valor)       
    #         preorden(NodoArbol.izquierda)
    #         preorden(NodoArbol.derecha)
    
    #crear Nodos
    nodo1 = NodoArbol(1)
    nodo2 = NodoArbol(2)
    nodo3 = NodoArbol(3)

    #conectar Nodos

    nodo1.izquierda = nodo2
    nodo1.derecha = nodo3

    print(nodo1.valor)
    print(nodo1.izquierda.valor)
    print(nodo1.derecha.valor)
    print(nodo1.derecha.derecha) # None porque no tiene asignado nodos hijos