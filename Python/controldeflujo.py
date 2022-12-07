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
"""
contador = 1

while mientras la condicion sea True:
    ejecuta las acciones(Todo la accion ejecutada dentro de este bloque se llama interaccion)
"""
"""
while contador <= 10:

    # contador += 1
    # if contador % 2 == 0:
    #  print(contador, 'Es un numero par.')
    #print('Conatador vale', contador)

#------ BREAK ---------------------
    if contador == 5:
        print('Rompo el bucle')
        break
"""
# ------- CONTINUE ------------------
"""
contador += 1
while contador <= 10:

  if contador % 2 == 0:
      print(contador, 'Es un numero par.')
      continue

  print('Y ahora incremento al contador', contador)
  contador += 1

  print('Fuera del While')
"""
  # ---------------------------------
"""
contador += 0

while contador <= 10:
    contador += 1

    if contador % 2 == 0:
        print(contador, 'Es un numero par.')
        continue

    print('Estoy aqui, porque contador vale ',contador,' y no dse ha disparado el continue')

print('Fuera del While')
"""
#----------- FOR ---------------------
lista = [1,2,3,4,5,6]
tupla = (1,2,3,4,5,'a','b','c','d')
"""
for valorActual in tupla:
    print(valorActual)
"""
#-----------RANGE --------------------
# (desde 0, hasta 10)
for numero in range (0, 10):
    print(numero)

#------- LEN -------------------------
longitud = len(tupla)
print('La lista tiene', longitud, 'items')

#---------------------------------------
lista2 = ['Hola', 'Mensaje','Rumor']

for palabra in lista2:
    print('Palabra actual:', palabra)

    if palabra == 'Mensaje':
        print('He encontrado la palabra Mensaje')
        break

    #-------------------------------------
    print()
    lista3 = ['Hola', 'Mensaje', 'Rumor']

    if 'Mensaje' in lista3:
        print('Pediste la palabra mensaje')


for number in range(100,0 -1):
    print(number)






