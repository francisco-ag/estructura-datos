# Ejemplo Simple de Deshacer en un editor de texto

class EditorTexto:
    def __init__(self):
        # Aqui definimos la pila
        self.historial = []
    def agregar_texto(self, texto):
        # utilizamos push para agregar texto a la pila
        self.historial.append(texto)
    def deshacer(self):
        # Utilizamos pop pero antes validando que la pila no este vacia 
        if self.historial :
            self.historial.pop()
    def mostrar_texto(self) :
        #print(self.historial)
        return ''.join(self.historial) 

editor = EditorTexto()

editor.agregar_texto("Buen")
editor.agregar_texto(" Día")
editor.agregar_texto(" Francisco")
print(editor.mostrar_texto())
editor.deshacer()
print(editor.mostrar_texto())
editor.deshacer()
print(editor.mostrar_texto())
editor.deshacer()
print(editor.mostrar_texto())
editor.deshacer()
print(editor.mostrar_texto())

