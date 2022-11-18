nombre = 'Luis Alberto'
Apellido = 'Roa'

"""
# nombre_completo = 'Mr. ' + nombre + ' ' + Apellido + '.'

# los %s seran reeeplandos por los valores en su posicion
# nombre_completo = 'Mr. %s %s %s.' % (nombre, Apellido, 'Escalante')

# Los place holder "{}" seran reemplazados por los valores "nombre y apellido" en su posicion
nombre_completo = 'Mr. {} {} {}.'.format(nombre, Apellido, 'Escalante')

# otra manera de hacerlo colocando nombre a los place holder
nombre_completo = 'Mr. {nombre} {primer_apellido} {segundo_apellido}.'.format(
    nombre=nombre,
    primer_apellido=Apellido,
    segundo_apellido='Escalante'
)

print(nombre_completo)
"""
# Interpolaciones podemos utilzar variables y una expresion booleanos, enteros, decimales
nombre_completo = f'Mr. {nombre} {Apellido} {"Escalante"} {True} {10*30}'
print(nombre_completo)
