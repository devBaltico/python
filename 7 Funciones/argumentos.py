#def promedio(listado):

# Ante poniendo un '*' en el argumento 'listado' tenemos una tupla
def promedio(*listado):
    print(listado)
    print(type(listado))
    return sum(listado) / len(listado)

#resultado = promedio([10, 10, 5, 7, 10,20])
resultado = promedio(10, 10, 5, 7, 10)

print(resultado)