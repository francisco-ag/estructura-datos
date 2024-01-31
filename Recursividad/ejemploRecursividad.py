
# def ejemplo_recursivo(n):
#     #Caso Base
#     if n== 0: 
#         return 0
#     #Llamada Recursiva
#     else:
#         return n + ejemplo_recursivo(n-1)

# resultado = ejemplo_recursivo(5)
# print(f"Resultado:  {resultado}")


#Factorial 

def factorial(n):
    
    if(n==0 or n == 1):
        
        return 1
    else:
        
        return n * factorial(n-1)
resultado = factorial(5)
#print(f"Resultado:  {resultado}")

def fibonacci(n):
    if(n==0) : 
        return 0
    elif n==1 :
        return 1 
    else: 
        return fibonacci(n-1) + fibonacci(n-2)

resultado_fibonacci = fibonacci(9)
print(f"Resultado:  {resultado_fibonacci}")