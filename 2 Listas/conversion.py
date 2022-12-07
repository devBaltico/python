"""
Para convertir otros tipos de datos en una lista podemos usar la función list():
"""
list('Python')
['P', 'y', 't', 'h', 'o', 'n']
# ----------------------------------------------------------------------------------
# Creando desde vacío
"""
Una forma muy habitual de trabajar con listas es empezar con una vacía e ir añadiendo
elementos poco a poco. Se podría hablar de un patrón creación.
Supongamos un ejemplo en el que queremos construir una lista con los números pares del
[0, 20):
"""
even_numbers = []
for i in range(20):
   if i % 2 == 0:
       even_numbers.append(i)

print(even_numbers)
# Impr: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
