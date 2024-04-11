import os
import heapq

# Función para dividir el archivo en segmentos
def dividir_segmentos(archivo_entrada, segment_size):
    with open(archivo_entrada, 'r') as f:
        temp_buffer = []
        temp_file_count = 0

        for line in f:
            temp_buffer.append(line.strip())
            if len(temp_buffer) >= segment_size:
                temp_buffer.sort()

                with open(f'temp_{temp_file_count}.txt', 'w') as temp_file:
                    temp_file.write('\n'.join(temp_buffer))
                temp_file_count += 1
                temp_buffer = []

        if temp_buffer:
            temp_buffer.sort()
            with open(f'temp_{temp_file_count}.txt', 'w') as temp_file:
                temp_file.write('\n'.join(temp_buffer))

            temp_file_count += 1

    return temp_file_count

# Función para realizar la mezcla de los segmentos
def mezclar_segmentos(num_files, output_file):
    heap = []
    output_buffer = []

    # Abrir todos los archivos temporales
    files = [open(f'temp_{i}.txt', 'r') for i in range(num_files)]

    # Usar heap para guardar los primeros elementos de cada archivo
    for i, file in enumerate(files):
        line = file.readline().strip()
        heapq.heappush(heap, (line, i))

    # Continuar mezclando las líneas hasta que el heap esté vacío
    while heap:
        line, file_index = heapq.heappop(heap)
        output_buffer.append(line)

        # Leer la siguiente línea del archivo correspondiente
        next_line = files[file_index].readline().strip()

        if next_line:
            heapq.heappush(heap, (next_line, file_index))

        if len(output_buffer) >= 1000:
            with open(output_file, 'a') as out_file:
                out_file.write('\n'.join(output_buffer) + '\n')
            output_buffer = []

    # Escribir el buffer de salida restante en el archivo
    if output_buffer:
        with open(output_file, 'a') as out_file:
            out_file.write('\n'.join(output_buffer) + '\n')

    # Cerrar todos los archivos temporales
    for file in files:
        file.close()

    # Eliminar archivos temporales
    for i in range(num_files):
        os.remove(f'temp_{i}.txt')

# Función principal para ordenar el archivo
def ordenar_archivo(archivo_entrada, archivo_salida):
    # Establecer manualmente el tamaño del segmento
    segment_size = 10000

    # Dividir el archivo en segmentos ordenados
    num_files = dividir_segmentos(archivo_entrada, segment_size)

    # Mezclar los segmentos para producir el archivo final ordenado
    mezclar_segmentos(num_files, archivo_salida)

# Ejemplo de uso
archivo_entrada = '/home/francisco/Documents/Lorem.txt'   
archivo_salida = 'datos_ordenados.txt'

ordenar_archivo(archivo_entrada, archivo_salida)
print(f'Se ha ordenado exitosamente el archivo "{archivo_entrada}" y se ha guardado como "{archivo_salida}".')
