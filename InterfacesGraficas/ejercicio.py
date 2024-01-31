import tkinter as tk 
#designar alias tk

def sumar_numeros():
    try:
        num1 = float(entrada_num1.get())
        num2 = float(entrada_num2.get())
        resultado.set(f"Resultado {num1+num2}")
    except ValueError:
        resultado.set("ERROR: Ingrese numeros validos ")

#Crear ventana principal
root = tk.Tk()
root.title("Calculadora Simple")

entrada_num1    = tk.Entry(root)
entrada_num2    = tk.Entry(root)
resultado   = tk.StringVar()

etiqueta_num1= tk.Label(root, text="Numero 1") 
etiqueta_num2= tk.Label(root, text="Numero 2") 
etiqueta_resultado= tk.Label(root, textvariable=resultado )

#Usar Sistema de Gestion Geometrica preferido
etiqueta_num1.grid(row=0, column=0)
etiqueta_num2.grid(row=1, column=0)
entrada_num1.grid(row=0, column=1)
entrada_num2.grid(row=1, column=1)
etiqueta_resultado.grid(row=2, column=0, columnspan=2)

boton_sumar = tk.Button(root, text="Sumar", command=sumar_numeros)
boton_sumar.grid(row=3, column=0, columnspan=2)

root.mainloop()