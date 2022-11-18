# uno, dos, tres, cuatro = 1, 2, 3, 4

# print(uno)
# print(dos)
# print(tres)
# print(cuatro)

"""
Hagamos lo mismo usando tuplas
Si tenemos más valores agregamos un "*" le decimos a python que los agregue
ejemplo: *resto_valores como podemos ver a partir del 5
* -> lista
_ -> el guion bajo omite valor.
----------------------------------------------------------------------------
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# uno, dos, tres, cuatro, *resto_valores = numeros
uno, dos, tres, cuatro, *_ = numeros  # Guion bajo omite el resto de valores

# De esta forma omitimos algunos valores y colocamos otros
uno, dos, tres, cuatro, *_, nueve, diez = numeros

print(uno)
print(dos)
print(tres)
print(cuatro)
# print(resto_valores)
print(nueve)
print(diez)
"""

"""
Comprimir
"""
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

tupla = (10, 20, 30, 40, 50)

lista_2 = [100, 200, 300, 400, 500]

tupla_2 = (1000, 2000, 3000, 4000, 5000)

resultado = zip(lista, tupla, lista_2, tupla_2)  # -> zip
resultado = tuple(resultado)
print(resultado)
