from collections import deque

class Laberinto:
    def __init__(self, laberinto):
        self.laberinto = laberinto
        self.filas = len(laberinto)
        self.columnas = len(laberinto[0])

    def es_valido(self, fila, columna):
        return 0 <= fila < self.filas and 0 <= columna < self.columnas and self.laberinto[fila][columna] != 1

    def encontrar_camino(self, inicio, fin):
        fila_inicio, columna_inicio = inicio
        fila_fin, columna_fin = fin
        visitados = set()
        cola = deque([(fila_inicio, columna_inicio, [])])

        while cola:
            fila, columna, camino = cola.popleft()
            if (fila, columna) == (fila_fin, columna_fin):
                return camino + [(fila, columna)]
            if (fila, columna) in visitados:
                continue
            visitados.add((fila, columna))
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nueva_fila, nueva_columna = fila + dx, columna + dy
                if self.es_valido(nueva_fila, nueva_columna):
                    cola.append((nueva_fila, nueva_columna, camino + [(fila, columna)]))
        return None


laberinto = [
    [0, 0, 0, 0, 1],
    [1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

lab = Laberinto(laberinto)
inicio = (0, 0)
fin = (4, 4)
camino = lab.encontrar_camino(inicio, fin)
if camino:
    print("Camino encontrado:")
    for fila, columna in camino:
        print(fila, columna)
else:
    print("No se encontró un camino válido.")
