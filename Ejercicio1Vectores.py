"""
Realizar programa Java que permita cargar un vector numérico de 10 elementos desde teclado
y, posteriormente visualice el valor del elemento mayor y cuántas veces se repite en el vector
este valor máximo. Utiliza JOptionPane.
"""

lista = []

for i in range(10):
    lista.append(int(input(f"Introduce el número {i}: "))

for elemento in lista:
    if elemento > mayor:
        mayor = elemento

print(f"Mayor: {mayor}")
print(f"En la lista aparece el {mayor} la cantidad de {lista.count(mayor)} veces")