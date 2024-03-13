import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import numpy as np

class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def dibujar_arbol(ax, nodo, x, y, nivel, espacio):
    if nodo is not None:
        texto = str(nodo.valor)
        
        ax.text(x, y, texto, horizontalalignment='center', fontsize=12)
        if nodo.izquierda is not None:
            ax.add_patch(FancyArrowPatch((x, y-0.05), (x-espacio/nivel, y-0.15), arrowstyle='->', mutation_scale=10))
        if nodo.derecha is not None:
            ax.add_patch(FancyArrowPatch((x, y-0.05), (x+espacio/nivel, y-0.15), arrowstyle='->', mutation_scale=10))
        dibujar_arbol(ax, nodo.izquierda, x-espacio/nivel,y-0.2,nivel*2,espacio)
        dibujar_arbol(ax, nodo.derecha, x+espacio/nivel, y-0.2, nivel*2, espacio)
        
def dibujar_arbol_binario(raiz):
    fig, ax = plt.subplots()
    ax.set_xlim(0, 2)
    ax.set_ylim(0, 2)
    dibujar_arbol(ax, raiz, 1, 1.9, 4, 1)
    ax.axis('off')
    plt.show()

# Crear un árbol binario
raiz = NodoArbol(1)
raiz.izquierda = NodoArbol(2)
raiz.derecha = NodoArbol(3)

raiz.derecha.izquierda = NodoArbol(4)
raiz.derecha.derecha = NodoArbol(5)



# Visualizar el árbol binario
dibujar_arbol_binario(raiz)



    



