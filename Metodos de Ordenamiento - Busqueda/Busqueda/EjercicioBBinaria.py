# Realizar una función de búsqueda binaria que maneja listas
# ordenadas de manera descendente 

def busqueda_binaria_descendente(lista, valor_objetivo):
    izquierda, derecha = 0 , len(lista)-1

    while izquierda<= derecha:
        medio = (izquierda + derecha )//2

        if lista[medio] == valor_objetivo:
            return medio
        elif lista[medio]> valor_objetivo:
            izquierda = medio+1
        else:
            derecha = medio-1
    return -1 

# ejemplo de uso

lista_descendente = [9,8,7,6,5,4,3,2,1]

valor_buscar = 6
indice_encontrado = busqueda_binaria_descendente(lista_descendente, valor_buscar)

if indice_encontrado != -1:
    print("El elemento es el no. ", indice_encontrado+1," en la lista")
else:
    print("El elemento no se encontró en la lista")
