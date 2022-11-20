"""
Python lee de izq a dere por lo que tomará 'cody' (true) y 'meincodes' (false)
"""
#variable = 'Cody' or 'Meincodes'

"""
# En este caso la variable 'listado' no es tomado en cuenta porque esta vacio.
listado = []
nombre = 'cody'

if listado:
    variable = listado
else:
    variable = nombre
"""
# Otra manera en una sola linea de codigo
listado = []
nombre = 'cody'
variable = listado or nombre

print(variable)
