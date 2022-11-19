diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

"""
Métodos
# keys
# values
# items
"""
#llaves = diccionario.keys()
# podemos hacer una tupla
llaves = tuple(diccionario.keys())
print(llaves)

# Imprimimos los valores
#valores = diccionario.values()
# Podemos convertir este objeto a tupla
valores = tuple(diccionario.values())
print(valores)

elementos = diccionario.items()
elementos = tuple(diccionario.items())
print(elementos)
