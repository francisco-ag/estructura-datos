

#Ejemplo para comprobar lectura de archivos 
#with open('/home/francisco/Documents/input.txt', 'r') as archivo:
#    for linea in archivo:
#        print(linea.strip())

def merge_sort(arr):
    if len(arr) > 1:
        medio = len(arr) // 2
        izquierda = arr[:medio]
        derecha = arr[medio:]

        merge_sort(izquierda)
        merge_sort(derecha)

        i = j = k = 0

        # Fusionar las sublistas izquierda y derecha
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                arr[k] = izquierda[i]
                i += 1
            else:
                arr[k] = derecha[j]
                j += 1
            k += 1

        # Comprobar si quedan elementos en las sublistas izquierda y derecha
        while i < len(izquierda):
            arr[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            arr[k] = derecha[j]
            j += 1
            k += 1

def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.readlines()
    # Convertir cada línea a un entero y eliminar los caracteres de nueva línea
    return [int(x.strip()) for x in contenido]

def escribir_archivo(lista_ordenada, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        for elemento in lista_ordenada:
            archivo.write(str(elemento) + '\n')

if __name__ == "__main__":
    # Nombre del archivo de entrada y salida
    archivo_entrada = '/home/francisco/Documents/estructura-datos/input.txt'  # Indicar la ubicacion del archivo
    archivo_salida = '/home/francisco/Documents/estructura-datos/output.txt'

    # Leer el archivo de entrada y ordenar los datos
    lista_desordenada = leer_archivo(archivo_entrada)
    merge_sort(lista_desordenada)

    # Escribir la lista ordenada en el archivo de salida
    escribir_archivo(lista_desordenada, archivo_salida)

    print(f"Datos ordenados escritos en '{archivo_salida}'")


