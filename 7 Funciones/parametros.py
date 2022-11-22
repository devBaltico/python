# Los valores por default se colocan del lado derecho sin espacios "pi=3.14" en los parametros 
def area_circulo(radio, pi=3.14):
    return pi *(radio ** 2)

#resultado = area_circulo(10, 3.14)

# En este caso no necesito colocar ningun argumento. Coloco el parametro por default arriba "pi=3.14"
#resultado = area_circulo(10)

# Cuando se usa los nombres de los parametros se pueden colocar en cualquier posicion
resultado = area_circulo(pi=3.141592, radio=10)
print(resultado)
