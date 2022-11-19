# Las llaves "{}" de nota que es un "diccionario"
#elementos = {}

# Las llaver no permiten duplicados y tomara el ultimo valor asignado
elementos = {'a': 1, 'b': 2, 'c': 3, 'a': 4}

"""
# los datos dentro de los corchetes son inmutables en tiempo de ejecucion. Puede almacenar cualquier tipo de dato.
elementos['nombre'] = 'Sacha'  # Crea la llave
# Tupla dentro de los corchetes
elementos[(1, 2, 3)] = 'La llave es una tupla'

# Actualiza el valor que almacena en la llave
elementos['nombre'] = 'Meincodes'
"""

print(elementos)
print(len(elementos))
