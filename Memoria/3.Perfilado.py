import cProfile
import random
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
#lista_desordenada = [3, 6, 8, 10, 1, 2, 1]
numeros_aleatorios = random.sample(range(1, 15001), 10000)
print(numeros_aleatorios)


# Perfilado del Algoritmo InsertionSort
print("INSERTION SORT")
cProfile.run('insertion_sort(numeros_aleatorios)', sort='cumulative')

# Perfilado del Algoritmo QuickSort
print("QUICKSORT")
cProfile.run('quicksort(numeros_aleatorios)', sort='cumulative')


# Perfilado del Algoritmo BubbleSort
print("BUBBLESORT")
cProfile.run('bubble_sort(numeros_aleatorios)', sort='cumulative')

