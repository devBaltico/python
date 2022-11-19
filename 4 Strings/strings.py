"""
# El metodo split devuelve un listado
lenguaje = 'Python JavaScript PHP SASS CSS'

listado_lenguajes = lenguaje.split()  # Por default divide con espacios, podemos dividir
con caracteres /*# etc
print(listado_lenguajes)
"""
# el metodo join devuelve un string
lenguaje = ['Python', 'JavaScript', 'PHP', 'SASS', 'CSS']

# Podemos dividir con cualquier caracter /*- etc.
string_lenguaje = '/ '.join(lenguaje)
print(string_lenguaje)
