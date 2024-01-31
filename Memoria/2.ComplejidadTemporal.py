import timeit

# Implementación de BubbleSort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Implementación de QuickSort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Lista de números desordenados para la prueba
lista_desordenada = [3, 6, 8, 10, 1, 2, 1]

# Medición del tiempo para BubbleSort
time_bubble_sort = timeit.timeit(stmt='bubble_sort(lista_desordenada.copy())', globals=globals(), number=1000)

print(f"Tiempo promedio de ejecución de BubbleSort: {time_bubble_sort} segundos")

# Medición del tiempo para QuickSort
time_quick_sort = timeit.timeit(stmt='quick_sort(lista_desordenada.copy())', globals=globals(), number=1000)

print(f"Tiempo promedio de ejecución de QuickSort: {time_quick_sort} segundos")
