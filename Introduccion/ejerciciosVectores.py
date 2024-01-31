# Crear un programa que pida 'x' cantidad de numeros 
# y separar los numeros pares en un vector y los nones en otro
# Mostrar ambos vectores

x_numeros = int(input("Ingrese la cantidad de números que desea ingresar: "))

# Inicializar vectores para pares e impares
numeros_pares = []
numeros_impares = []

# Leer los números y separarlos en vectores
for i in range(x_numeros):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)

# Mostrar los vectores de pares e impares
print("\nNúmeros pares:", numeros_pares)
print("Números impares:", numeros_impares)