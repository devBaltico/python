"""
rango = range(11)  # 0 -10

for valor in rango:
    print(valor)

print(rango)
print(type(rango))
"""
# Otra manera
# for valor in range(21):
#   print(valor)

# Otra manera con rango desde un numero especifico
"""
En esta caso tenemos 3 argumentos el primero el inicio de nuestro rango, el segundo el final de
nuestro rango y por ultimo si queremos saltos (skips) de linea de "2 en 2 o 3 en 3 etc." 
"""
# for valor in range(5, 21, 2):
#   print(valor)

"""
----------------------------------------------
Enumerate
"""
numeros = [10, 20, 30, 40, 50]
# Enumerate nos retorna un objeto iterable que el cual a su vez posee tuplas, estas tuplas almacenan 2 valores
# quen el "indice" y el elemento perse "numero", los indice por default inician en "0"
for indice, numero in enumerate(numeros):
    print(indice, numero)
