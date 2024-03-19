
class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario: 
    def __init__(self):

        self.raiz = None
    
    # Operaciones
        
    # Insertar un nuevo Nodo 
    def insertar(self, valor):
        if self.raiz is None :
            self.raiz = NodoArbol(valor)
        else: 
            self.insertar_recursivo(self.raiz, valor)
    
    def insertar_recursivo( self, nodo, valor):
        if valor < nodo.valor : 
            if nodo.izquierda is None : 
                nodo.izquierda = NodoArbol(valor)
            else:
                self.insertar_recursivo(nodo.izquierda, valor)
        elif valor > nodo.valor :
            if nodo.derecha is None:
                nodo.derecha = NodoArbol(valor) 
            else:
                self.insertar_recursivo(nodo.derecha, valor)

    # Buscar
    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo, valor):
        if nodo is None:
            return False
        if valor == nodo.valor:
            return True
        elif valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierda, valor)
        else:
            return self._buscar_recursivo(nodo.derecha, valor)
    
    #eliminar
    def eliminar(self, valor):
        self.raiz = self._eliminar_recursivo(self.raiz, valor)

    def _eliminar_recursivo(self, nodo, valor):
        if nodo is None:
            return nodo
        if valor < nodo.valor:
            nodo.izquierda = self._eliminar_recursivo(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, valor)
        else:
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda
            else:
                nodo.valor = self._encontrar_minimo(nodo.derecha)
                nodo.derecha = self._eliminar_recursivo(nodo.derecha, nodo.valor)
        return nodo

    def _encontrar_minimo(self, nodo):

        minimo = nodo.valor
        while nodo.izquierda is not None:
            minimo = nodo.izquierda.valor
            nodo = nodo.izquierda
        return minimo
    

# Ejemplo de uso
arbol = ArbolBinario()
arbol.insertar(10)
arbol.insertar(5)
arbol.insertar(15)
arbol.insertar(3)
arbol.insertar(7)
arbol.insertar(12)
arbol.insertar(17)

print("Búsqueda:", arbol.buscar(7))  
print("Búsqueda:", arbol.buscar(20))  

print("Eliminando nodo 10...")
arbol.eliminar(10)
print("Búsqueda:", arbol.buscar(10)) 