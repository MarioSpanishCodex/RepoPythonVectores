"""
A partir de dos vectores numéricos de 15 elementos, denominados vector1 y vector2,
respectivamente, obtener un tercer vector, vector3 cuyos elementos sean la suma de los
elementos de los vectores anteriores. Completar los vectores con números comprendidos entre
0 y 100, generados aleatoriamente. (Sumar arrays o vectores es sumar elemento a elemento y
colocar el resultado en la misma posición del vector resultado).
"""

import random as r

vector1 = []
vector2 = []
vector3 = []

for i in range(15):
    vector1.append(r.randint(0,100))
    vector2.append(r.randint(0,100))
    vector3.append(vector1[i] + vector2[i])

print(vector1)
print(vector2)
print(vector3)