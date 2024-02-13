#
# Hacer una interfaz grafica 
# que calcule el CURP (simple) 
# para ello , capturar , nombre, apellido paterno, apellido materno
# Fecha de nacimiento
# Cuando se genere , mostar un mensaje de que se ha generado la curp 
#  



# Import Required Library
from tkinter import *
from tkcalendar import Calendar
from datetime import date
from datetime import datetime

# Create Object
root = Tk()
 
# Set geometry
root.geometry("400x400")
 
# Obtener fecha 
#Día actual
today = date.today()

#Fecha actual
now = datetime.now()

print(today)
print(now)
print(now.day)
print(now.month)
print(now.year)


# Add Calendar
cal = Calendar(root, selectmode = 'day',
               year = 2020, month = 5,
               day = 22)
 
cal.pack(pady = 20)
 
def grad_date():
    date.config(text = "Selected Date is: " + cal.get_date())
 
# Add Button and Label
Button(root, text = "Get Date",
       command = grad_date).pack(pady = 20)
 
date = Label(root, text = "")
date.pack(pady = 20)
 
# Execute Tkinter
root.mainloop()
