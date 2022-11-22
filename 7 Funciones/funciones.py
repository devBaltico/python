
"""
def suma():
    numero_uno  = int(input('Ingresa el primer numero entero: ')) # str
    numero_dos  = int(input('Ingresa el segundo numero entero: '))

    resultado = numero_uno + numero_dos

    print(resultado)
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