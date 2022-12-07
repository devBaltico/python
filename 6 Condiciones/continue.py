#-------------------------------------------------

want_exit = 'n'
valid_options = 0

while want_exit == 'n':
    print('Hola que tal')
    want_exit = input('¿Quieres salir? [s/n]')
    if want_exit not in 'sn':
        want_exit = 'n'
        continue
    valid_options += 1
    print(f'{valid_options} respuestas validas')
    print('Chao')

#--------------------------------------------------
