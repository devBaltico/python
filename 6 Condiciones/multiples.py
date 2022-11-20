calificacion = 5

# Se evalua de manera descendente la condicional "elif" va entre "if" y "else"
if calificacion == 10:
    print('Felicidades, aprobostes la materia con la mejor calificacion.')
elif calificacion == 9 or calificacion == 8:
    print('Felicidades, aprobote la materia.')
elif calificacion == 7 or calificacion == 6:
    print('Aprobaste la materia')
else:
    print('Reprobaste la materia.')
