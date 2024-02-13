import time
def palabra_palindromo(palabra):
    # Caso base
    if len(palabra) == 0:
        return palabra
    else:
        return palabra_palindromo(palabra[1:]) + palabra[0]

palabra = "hola"
inicio = time.perf_counter()  # Inicio de la medición
palabra_invertida = palabra_palindromo(palabra)
fin = time.perf_counter()  # Fin de la medición

print(f"La palabra invertida de {palabra} es {palabra_invertida} por lo tanto es un Palindromo.")
print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")