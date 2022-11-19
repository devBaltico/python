diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Usando la palabra "IN" verificamos si el valor "X" esta en el diccionario. El valor que tenemos de vuelta es booleano.
print('x' in diccionario)
"""
valor = diccionario['d']
print(valor)
"""
# Con "get" obtenemos los valores

valor = diccionario.get('x')
# Podemos agregar un mensaje, pero por default devuelve "none"
valor = diccionario.get('x', 'La llave no existe en el diccionario.')
# Setdefault nos permite obtener el valor de una llave
valor = diccionario.setdefault('e', 5)
print(diccionario)  # Verificamos que nuestro valor "5" fue agregado al diccionario

print(valor)
