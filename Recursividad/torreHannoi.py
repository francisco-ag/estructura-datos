def torres_hanoi(n, origen, destino, auxiliar):
    if n == 1:
        print(f"Mover disco 1 de {origen} a {destino}")
    else:
        torres_hanoi(n-1, origen, auxiliar, destino)
        print(f"Mover disco {n} de {origen} a {destino}")
        torres_hanoi(n-1, auxiliar, destino, origen)
torres_hanoi(3, 'A', 'B', 'C')