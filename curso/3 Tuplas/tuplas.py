

#cursos = ('Python', 'JavaScript', 'PHP', 'SQL', 'MongoDB')

#primer_curso = cursos[0]
#ultimo_curso = cursos[-1]

# print(primer_curso)
# print(ultimo_curso)

"""
Podemos hacer subtupla
"""
#sub_tupla = cursos[0:3]
# sub_tupla = cursos[:3]  # Teniendo el mismo resultado anterior
# sub_tupla = cursos[:]  # Teniendo todos los datos de la tupla
# print(sub_tupla)

"""
Listas y tuplas
"""
cursos = ('Python', 'JavaScript', 'PHP', 'SQL', 'MongoDB')

curso_tupla = tuple(cursos)

print(curso_tupla)
print(type(curso_tupla))

niveles = ('Basico', 'Intermedio', 'Avanazado')

niveles_lista = list(niveles)

print(niveles_lista)
print(type(niveles_lista))
