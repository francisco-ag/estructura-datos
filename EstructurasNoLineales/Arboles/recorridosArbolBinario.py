import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import numpy as np

class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def crear_arbol_binario(ax, nodo, x, y, nivel, espacio):
    if nodo is not None:
        texto = str(nodo.valor)
        
        ax.text(x, y, texto, horizontalalignment='center', fontsize=12)
        if nodo.izquierda is not None:
            ax.add_patch(FancyArrowPatch((x, y-0.05), (x-espacio/nivel, y-0.15), arrowstyle='->', mutation_scale=10))
        if nodo.derecha is not None:
            ax.add_patch(FancyArrowPatch((x, y-0.05), (x+espacio/nivel, y-0.15), arrowstyle='->', mutation_scale=10))
        
        crear_arbol_binario(ax, nodo.izquierda, x-espacio/nivel,y-0.2,nivel*2,espacio)
        crear_arbol_binario(ax, nodo.derecha, x+espacio/nivel, y-0.2, nivel*2, espacio)

def dibujar_arbol_binario(raiz):
    fig, ax = plt.subplots(3,1, figsize=(10,15))

    for i, recorrido in enumerate([inorden, preorden, postorden]):    
        ax[i].set_xlim(0, 2)
        ax[i].set_ylim(0, 2)
        crear_arbol_binario(ax[i], raiz, 1, 1.9, 4, 1)
        ax[i].axis('off') 
        ax[i].set_title("Recorrido "+recorrido.__name__.capitalize()) 
    plt.tight_layout()
    plt.show()

def inorden(nodo):
    if nodo is not None:
        inorden(nodo.izquierda)
        print(nodo.valor)
        inorden(nodo.derecha)

def preorden(nodo):
    if nodo is not None: 
        print(nodo.valor)
        preorden(nodo.izquierda)
        preorden(nodo.derecha)

def postorden(nodo):
    if nodo is not None: 
        postorden(nodo.izquierda)
        postorden(nodo.derecha)
        print(nodo.valor)
    
# Crear un árbol binario
raiz = NodoArbol(1)
raiz.izquierda = NodoArbol(2)
raiz.derecha = NodoArbol(3)

dibujar_arbol_binario(raiz)