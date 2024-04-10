class GrafoListaAdyacencia:

    def __init__(self):
        self.lista = {}
    
    def agregar_vertice(self, vertice):
        self.lista[vertice] = []

    def agregar_arista(self, origen , destino):
        self.lista[origen].append(destino)

        #Si el grafo , no es dirigido agregar 
        self.lista[destino].append(origen)

    def imprimir_grafo(self):
        for vertice , adyacentes in self.lista.items():
            print(f"{vertice}: {adyacentes}")

grafo = GrafoListaAdyacencia()
grafo.agregar_vertice(1)
grafo.agregar_vertice(2)
grafo.agregar_vertice(3)
grafo.agregar_vertice(4)
grafo.agregar_arista(1,2)
grafo.agregar_arista(2,3)
grafo.agregar_arista(3,4)

grafo.imprimir_grafo()
