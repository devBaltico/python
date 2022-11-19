diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print(len(diccionario))

# Primera forma
del diccionario['a']
# Segunda forma
valor = diccionario.pop('b')
print(valor)
# Tercera forma
diccionario.clear()

print(diccionario)
print(len(diccionario))
