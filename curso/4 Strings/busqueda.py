titulo_curso = 'Curso Profesional de Python, donde aprenderemos Python'
"""
# titulo_curso.count('o')

contador = titulo_curso.count('e')
print(contador)
"""
# Buscar una palabra colocamos la palabra "python" y el string base "titulo_curso" esto devuelve un valor booleano True
#print('Python' in titulo_curso)
# con "lower" ponemos todas la palabras en minusculas y con
print('Python' in titulo_curso.lower())

# podemos negar con "not"
print('micursogenial' not in titulo_curso.lower())

"""
# Buscar una palabra colocamos la palabra "Curso" y el string base "titulo_curso" esto devuelve un valor booleano True
startswith nos permite ver si un valor esta al inicio del string "Curso"
endswith nos permite ver si un valor esta al final del string "Python"
"""
print(titulo_curso.startswith('Curso'))
print(titulo_curso.endswith('Python'))
