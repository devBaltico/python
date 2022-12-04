# Control de flujo de un programa
"""
a = 5
b = 6

resultado = a > b

# print(resultado)


# AND -> True, False
print('t o t', True or True)
print('t o f', True or False)
print('f o t', False or True)
print('f o f', False or False)

print()

# OR -> True, False
print('t o t', True or True)
print('t o f', True or False)
print('f o t', False or True)
print('f o f', False or False)


"""
"""
resultado = (a >= 5 or c > 7)
resultado = (True or False)
resultado = (True)

resultado = ((a >= 5 or c > 7) and (b == 5))
resultado = ((True or False) and (False))
resultado = (True or False)
resultado = (True and False)
resultado = (False)
"""
"""

a = 5
b = 6
c = 7

# a > b
# (a> b) and (c>=b) and (a>c or b >= c)
# (False) and (True) and (False or False)
# False and True and False
# False and False
# False

"""
"""
if condicion:
    acciones en if 1
    acciones en if 2

acciones fuera del if

a = 6
b = 6
c = 7

print()

if a > 6 and b <= 6:
    print('A es mayor o igual que 5 y B es menor o igual que 6')

elif a >= 6:
    print('A es mayor o igual que 6')

"""

# ----------------------------------------------------------------------
contador = 1
"""
while mientras la condicion sea True:
    ejecuta las acciones(Todo la accion ejecutada dentro de este bloque se llama interaccion)
"""

while contador <= 10:

    # contador += 1
    # if contador % 2 == 0:
    #  print(contador, 'Es un numero par.')
    print('Conatador vale', contador)

    if contador == 5:
        print('Rmpo el bucle')
        break

    contador += 1

print('Fuera del while')
