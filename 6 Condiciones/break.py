# break y continue

titulo_curso = 'Curso profesional Python'

"""
for caracter in titulo_curso:
    if caracter == 'P':
        break

    print(caracter)
"""

for caracter in titulo_curso:
    if caracter == 'P':
        continue

    print(caracter)

    # -------------------------------------------------
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
    # --------------------------------------------------
