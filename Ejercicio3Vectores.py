"""
Realizar un programa Java que inicialice un array numérico de 10 elementos y visualizar los
elementos que sean par y la posición en que se encuentra.
"""

import random as r

def contarpares(vector):
    contador = 0
    pos = []
    for k in range(0, len(vector)):
        if vector[k] % 2 == 0:
            contador += 1
            pos.append(k)
    return pos, contador
vector = []
for i in range (0, 10):
    vector.append(r.randint(0,100))
pos, contador = contarpares(vector)
print(f"Hay {contador} pares que están en posiciones {pos}")
