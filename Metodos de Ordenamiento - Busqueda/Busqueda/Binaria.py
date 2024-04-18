def busqueda_binaria(lista, elemento):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == elemento:
            return medio
        elif lista[medio] < elemento:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

# Uso de la función
lista = [1, 2, 4, 5, 7, 8, 9]
indice = busqueda_binaria(lista, 5)
print("El elemento se encontró en el índice:", indice)
