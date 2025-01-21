"""
Realizar un programa Java que cargue un vector con las notas de los 40 alumnos de una clase
y visualice el número de alumnos aprobados, el número de alumnos suspensos y la nota media
de la clase, y el número de calificaciones superiores a la media.

"""
import random

notas = [random.randint(0,10) for i in range(40)]
aprobados = 0
suspensos = 0
sumanotas = 0
sobremedia = 0

for i in range(len(notas)):
    if notas[i] < 5:
        suspensos += 1
    else:
        aprobados += 1
    sumanotas += notas[i]

notamedia = sumanotas / len(notas)

print(f"El número de alumnos aprobados es: {aprobados}")
print(f"El número de alumnos suspensos es: {suspensos}")
print(f"La nota media de la clase es de: {notamedia}")



for i in range(len(notas)):
    if notas[i] > notamedia:
        sobremedia += 1

print(f"El número de calificaciones superiores a la media es: {sobremedia}")