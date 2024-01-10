#Declaramos 2 vectores 
#Estos vectores serán homogeneos
nombres = []
identificadores = []

suma= []
# Definimos un tamaño para las vectores
# Lo puedes cambiar si quieres, antes de la compilacion
size = 3

# Leemos los datos y los agregamos a la lista
for i in range(size):
    print("Ingrese los datos de la persona", i + 1)
    input_nombre = input("Nombre: ")
    identificación  = int( input("Identificación: "))
    
    
    nombres.append(input_nombre)
    identificadores.append(identificación)

print (nombres)
print (identificadores)

suma.append(nombres)
suma.append(identificadores)
print("Sumando Vectores")
print(suma) #El resultado es un vector heterogeneo

