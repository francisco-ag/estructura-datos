#Hacer una funcion recursiva para sumar numeros naturales 

def suma_dos_numeros_recursiva(a, b):
    # Caso Base
    if b == 0:
        return a
    # Llamada Recursiva
    else:
        print (a+1, b-1)
        
        return suma_dos_numeros_recursiva(a + 1, b - 1)

# Ejemplo de uso
num1 = 10
num2 = 25
resultado = suma_dos_numeros_recursiva(num1, num2)
print(f"La suma de {num1} y {num2} es: {resultado}")


