"""
Realizar un programa Java que permita cargar por teclado un vector numérico TB_NUM[100],
posteriormente, introducir un valor desde teclado e intercalar1o en su posición correcta dentro
del vector numérico supuestamente ordenado, y visualice finalmente el vector con el dato
intercalado. El valor antiguo que estaba en la posición en la que se inserta se pierde.
"""

import random
numeros = []
for i in range(1, 101):
    numeros.append(random.randint(1,100))
    numeros.sort()
    print(numeros)


nuevoValor = int(input("Introduce el valor a cambiar donde toque: "))
for i in range (1, 100):
    if nuevoValor >= numeros[i] and nuevoValor <= numeros [i + 1]:
        numeros[i] = nuevoValor
print(numeros)