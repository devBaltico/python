"""
Numeros positivos 0       1          2         3
Numeros negativos -4     -3        -2         -1
lista_cursos = ['python', 'php', 'javascript', 'sql', 'css', 'sass']

primer_curso = lista_cursos[0]
print(primer_curso)

segundo_curso = lista_cursos[1]
print(segundo_curso)

tercer_curso = lista_cursos[2]
print(tercer_curso)

cuarto_curso = lista_cursos[3]
print(cuarto_curso)
"""
#----------------------------------------------------/
"""
######################## Indices modificados ##############################
"""
#lista_cursos = ['python', 'php', 'javascript', 'sql']

#lista_cursos[3] = 'Ruby'
# print(lista_cursos)
#----------------------------------------------------/

"""
######################## Sublistas para crearlas [start:end]  ##############################
"""
#                  0        1         2          3      4      5
#lista_cursos = ['python', 'php', 'javascript', 'sql', 'css', 'sass']
#sublista = lista_cursos [1:4]
# sublista = lista_cursos [1:] de esta manera le digo a python que me muestre todas las listas desde el indice 1
# [:end] -> obetenemos los primeros elementos de las lista
# sublista = lista_cursos [1:4:2] de esta forma hacemos saltos de 2 en 2 en la lista.
# sublista = lista_cursos [::-1] de esta forma hacemos que la sublista a la inversa.

# print(sublista)
#----------------------------------------------------/

"""
######################## Modificar listas  ##############################
"""
#lista_cursos = ['python', 'php', 'javascript', 'sql', 'css', 'sass']

# Con "len" contamos cuantos elementos hay en la lista
# print(len(lista_cursos))

# Con "append" agregamos elementos a la lista. Se puede agregar cualquier tipo de datos.
#lista_cursos.append ('MongoDB')
#lista_cursos.append ('Bootstrap')

# print(lista_cursos)
#----------------------------------------------------/

"""
########### Insertar una segunda lista con "extend" a la primera lista. ################
"""
"""
lista_cursos = ['Python', 'PHP', 'javascript', 'Sql', 'CSS', 'SASS']
lista_cursos2 = ['Jquery', 'XAMPP', 'Docker']
print(len(lista_cursos))

lista_cursos.append('MongoDB')
lista_cursos.append('Bootstrap')

lista_cursos.insert(1, 'Ruby')
lista_cursos.insert(3, 'React')
lista_cursos.insert(0, 'Pygame')

lista_cursos.extend(lista_cursos2)

print(lista_cursos)
print(len(lista_cursos))
"""
#----------------------------------------------------/

"""
################################################################################################
Remover un elemento de la lista con "remove", "del" con del selecciono el indice "0". Y "Clear"
elimina todas las listas.
"""
"""
lista_cursos.remove('MongoDB')
del lista_cursos[0]
lista_cursos.clear()

print(len(lista_cursos))
"""
#----------------------------------------------------/

"""
############################# Ordenar listas ########################################
"""
"""
lista = [8, 90, 1, 5, 44, 132, 600, 3, 4]

# Se ordena de menor a mayor.
lista.sort()

# Se ordena a la inversa de mayor a menor.
lista.sort(reverse=True)

print(lista)

# Para ordenar por el elemento menor y el mayor
lista.sort()
print(lista[0])  # min
print(lista[-1])  # max

# min - max otra manera de hacerlo se utiliza uno de los dos
print(min(lista))
print(max(lista))
"""
#----------------------------------------------------/

"""
#######################################################################################
Buscar un elemento en una lista "in" devuelve un valor booleano y con "not" negamos el valor booleano.
"""
"""
lista_numeros = [8, 90, 1, 5, 44, 132, 600, 3, 4]
print(000 in lista_numeros)  # False no esta en la lista
print(90 in lista_numeros)  # True si esta en la lista

# True si esta en la lista (negamos el valor booleano)
print(11 not in lista_numeros)
"""
#----------------------------------------------------/

"""
########################### Indice listas ###########################################
"""
"""
# Ejemplo si tenemos cinco 44 en la lista, nos trae el 1er 44 de la lista.
lista = [8, 63, 44, 90, 1, 5, 44, 132, 600, 3, 4, 44]

print(5 in lista)

index = lista.index(44)
print(index)
"""
#----------------------------------------------------

"""
########################### Repetir elementos ############################################
"""
"""
shopping = ['Agua', 'Huevos', 'Aceite']
shopping * 3

print(shopping)
"""
#----------------------------------------------------

"""
############################ Combinar listas #######################################
Python nos ofrece dos aproximaciones para combinar listas:
Conservando la lista original: Mediante el operador + o +=:
"""
"""
shopping = ['Agua', 'Huevos', 'Aceite']
fruitshop = ['Naranja', 'Manzana', 'Piña']
shopping + fruitshop

print(shopping + fruitshop)

# Modificando la lista original: Mediante la función extend():

shopping = ['Agua', 'Huevos', 'Aceite']
fruitshop = ['Naranja', 'Manzana', 'Piña']

shopping.extend(fruitshop)
print(shopping)
"""
#----------------------------------------------------

"""
Nivel avanzado
La diferencia entre ambos métodos tiene que ver con cuestiones internas de gestión de
memoria y de rendimiento:
"""

shopping = ['Agua', 'Huevos', 'Aceite']
id(shopping)
print(shopping)













