"""
contador = 1

while contador <= 10:
    print(contador)

    contador = contador + 1


# Otro ejemplo
numero = 123456789
contador_digitos = 0

while numero >= 1:
    #contador_digitos = contador_digitos + 1
    contador_digitos += 1

    numero = numero / 10
else:
    print('Fin del ciclo while.')

print(contador_digitos)
"""
#-------------------------------------------------
"""
want_exit = 'n'
num_quewstions = 0

while want_exit == 'n':
    print('Hola que tal')
    want_exit = input('¿Quieres salir? [s/n]')
    num_quewstions += 1
    if num_quewstions ==4:
        print('Has llegado al màximo de preguntas')
        break

    else:
        print('Has decidido salir')
    print('Chao')
    """
#--------------------------------------------------
# Bucle infinito para salir ctrl+C
"""
num = 1

while num != 10:
    num +=2
"""
#--------------------------------------------------

while True:
    mark = float(input('Introduzca nueva nota: '))
    if not (0 <= mark <= 10):
        print('Nota fuera de rango')
        break
        print(mark)






















