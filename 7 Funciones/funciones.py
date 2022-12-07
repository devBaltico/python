"""
El concepto de función es básico en prácticamente cualquier lenguaje de programación. Se
trata de una estructura que nos permite agrupar código. Persigue dos objetivos claros:

1. No repetir trozos de código durante nuestro programa.
2. Reutilizar el código para distintas situaciones.

Una función viene definida por su nombre, sus parámetros y su valor de retorno. Esta
parametrización de las funciones las convierte en una poderosa herramienta ajustable a las
circunstancias que tengamos. Al invocarla estaremos solicitando su ejecución y obtendremos
unos resultados.
"""
"""
def suma():
    numero_uno  = int(input('Ingresa el primer numero entero: ')) # str
    numero_dos  = int(input('Ingresa el segundo numero entero: '))

    resultado = numero_uno + numero_dos

    print(resultado)
"""
#-------------------------------------------------------------------------
"""
def suma(n1, n2):
     resultado = n1 + n1
     #print(resultado)
     #return resultado
     return n1 + n2, 'La funcion retorna 2 valores en tupla'
     
numero_uno  = int(input('Ingresa el primer numero entero: ')) # str
numero_dos  = int(input('Ingresa el segundo numero entero: '))
     
resultado, mensaje = suma(numero_uno, numero_dos)
print('El resultado es:', resultado)
print(mensaje)
"""
# -------------------------------------------------------------------
#Hagamos una primera función sencilla que no recibe parámetros
def say_hello():
    print('Hello')

# Invocamos la fuccion
say_hello()
#-------------------------------------------------------------------

# Retornar un valor
def one():
     return 1
one()
#---------------------------------------------------------------

if one() == 1:
    print('It works!')
else:
    print('Something is broken')

