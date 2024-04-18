# Implementar una funcion de busqueda secuencial
# Que busque dentro de una lista de objetos de la clase Persona
# Buscará por nombre


class Persona: 
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad 
    
    def __repr__(self):
        return f"{self.nombre} ({self.edad} años)"

def busqueda_secuencial_personas(lista_personas, nombre_buscar):

    for persona in lista_personas:
        if persona.nombre == nombre_buscar :
            return persona
    return None 

# Definir lista de Personas 

lista_personas = [
    Persona("Francisco",25),
    Persona("Willmar",18),
    Persona("Pedro",21),
    Persona("Irving",19),
]

# Realizar la busqueda 

nombre_buscar = "Rafa"      

persona_encontrada = busqueda_secuencial_personas(lista_personas, nombre_buscar)


if persona_encontrada: 
    print(f"Persona Encontrada : {persona_encontrada}")
else:
    print(f"{nombre_buscar} No está en la lista")

