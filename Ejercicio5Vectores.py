"""
Hacer un programa que realice las siguientes funciones:
 1- Llenar un array con las estaturas de los alumnos de una clase (Previamente
habremos pedido que se introduzca por teclado en número de alumnos de la clase).
 2- Suma de todas las estaturas de la clase.
 3- Calculo de la media de estaturas.
 4- Visualizar cuantos son más altos que la media y cuantos más bajos.

"""

import random

numeroAlumnos = int(input("Dime cuantos alumnos hay: "))

estaturas = []
for i in range(numeroAlumnos):
    numeroAlumnos +=

sumaEstaturas = 0
for i in range(len(estaturas)):
    sumaEstaturas += estaturas[i]

mediaEstaturas = sumaEstaturas/len(estaturas)
numeroBajos = 0
numeroAltos = 0
for estatura in estaturas:
    if estatura > mediaEstaturas:
        numeroAltos += 1
    else:
        numeroBajos += 1

print(estaturas)
print(mediaEstaturas)
print(f"Hay {numeroAltos} más altos que la media y {numeroBajos} más bajos.")

