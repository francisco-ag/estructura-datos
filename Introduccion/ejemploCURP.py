print("Ingrese nombre completo de una persona")
input_nombre = input("Nombre: ")

nombreCompleto = input_nombre.split(' ')
print(nombreCompleto) 
if(len(nombreCompleto)==3):
    nombre = nombreCompleto[0]
    apellidoPaterno = nombreCompleto[1]
    apellidoMaterno = nombreCompleto[2]
    curp = apellidoPaterno[0]+apellidoMaterno[0]+nombre[0]
    print(curp.upper())
else:
    print("verifique los datos")
