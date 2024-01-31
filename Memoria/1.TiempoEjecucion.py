#Medir tiempo de ejecucion de Algoritmos Python
import time
# Algoritmo 1 - BubbleSort
start_time = time.time()
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
# Ejemplo de uso:
lista_desordenada1 = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(lista_desordenada1)
print("Lista ordenada usando Bubble Sort:", lista_desordenada1)

tiempo_ejecucion_final = float(time.time() - start_time)
print(f"Tiempo de ejecución del Algoritmo 1: {tiempo_ejecucion_final} segundos")

# Algoritmo 2 - QuickSort
start_time2 = time.time()
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Ejemplo de uso:
lista_desordenada2 = [64, 34, 25, 12, 22, 11, 90]
resultado = quicksort(lista_desordenada2)
print("Lista ordenada usando Quick Sort:", resultado)

tiempo_ejecucion_final2 = float(time.time() - start_time2)
print(f"Tiempo de ejecución del Algoritmo 2: {tiempo_ejecucion_final2} segundos")







