"""
Python permite recorrer aquellos tipos de datos que sean iterables, es decir, que admitan
iterar2 sobre ellos. Algunos ejemplos de tipos y estructuras de datos que permiten ser iteradas
(recorridas) son: cadenas de texto, listas, diccionarios, ficheros, etc. La sentencia for nos
permite realizar esta acción.
"""
"""
usuarios = ['user1', 'user2', 'user3', 'user4']

for usuario in usuarios:
    print(usuario)
"""
# Romper un bucle for
word = 'Python'
for letter  in word:
    if letter == 't':
       break
print(letter)
#---------------------------------------------------
# Ejercicio contar cuantas vocales
word_vocal = 'Supercalifragilisticoespialidoso'

vocala = word_vocal.count('a')
vocale = word_vocal.count('e')
vocali = word_vocal.count('i')
vocalo = word_vocal.count('o')
vocalu = word_vocal.count('u')

suma = vocala + vocale + vocali+ vocalo + vocalu

print(suma)












