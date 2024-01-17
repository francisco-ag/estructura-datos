# Crear un programa que almacene nombres en vector
# capturará datos hasta que el valor ingresado, se 'STOP'
# mostrar el vector resultante
# (Sugerencia: usar metodo while )

nombres = []


while True:
    nombre = str(input("Ingresa un nombre: "))
    nombre.upper()
    if nombre == "STOP":
        break
    else:
        nombres.append(nombre)
print("Nombres almacenados: ", nombres)
