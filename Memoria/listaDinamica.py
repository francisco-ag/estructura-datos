
#Ejemplo de Uso de Memoria Dinámica usando clases

#Definicion de la Clase
class ListaDinamica:
    def __init__(self):
        self.elementos = []

    def agregarElementos(self, elemento):
        self.elementos.append(elemento)

    def mostrarElementos(self):
        print("Elementos de la Lista", self.elementos)

#Metodo para usar clase ListaDinamica
def usoMemoriaDinamica():
    new_lista = ListaDinamica() #Objeto tipo ListaDinamica

    new_lista.agregarElementos(10)
    new_lista.agregarElementos(20)
    new_lista.agregarElementos(30)

    new_lista.mostrarElementos()

if __name__ == "__main__":
    usoMemoriaDinamica()




    






    





