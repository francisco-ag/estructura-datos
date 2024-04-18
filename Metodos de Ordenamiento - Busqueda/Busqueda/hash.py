# Creación de un diccionario (hash table)
hash_table = {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid'}

# Acceder a un elemento
print(hash_table['nombre'])  # Juan

# Insertar un nuevo elemento
hash_table['profesion'] = 'Ingeniero'

# Buscar un elemento
if 'edad' in hash_table:
    print("Edad encontrada:", hash_table['edad'])

# Tratar de acceder a una clave que no existe
print(hash_table.get('salario', 'No encontrado'))
