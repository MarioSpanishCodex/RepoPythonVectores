"""
Realizar programa Java que permita cargar un vector numérico de 10 elementos desde teclado
y, posteriormente visualice la media de los elementos que se encuentran en las posiciones
pares (0,2,4,….) y la media de los elementos que se encuentran en las posiciones impares(1,
3, 5…..) del vector. La tabla sólo debe ser recorrida una vez

"""

import random as r

lista = []
for i in range(10):
    lista.append(random.randint(0,10))

print(lista)
sumaPares = 0
sumaImpares = 0
for i in range(len(lista)):
    if i % 2 == 0:
        sumaPares += lista[i]
    else:
        sumaImpares += lista[i]

print(f"Media pares: {sumaPares/len(lista)/2}")
print(f"Media impares: {sumaImpares/(len(lista)/2}")