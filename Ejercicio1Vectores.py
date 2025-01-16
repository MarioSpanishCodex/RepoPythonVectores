"""
Realizar programa Java que permita cargar un vector numérico de 10 elementos desde teclado
y, posteriormente visualice el valor del elemento mayor y cuántas veces se repite en el vector
este valor máximo. Utiliza JOptionPane.
"""

numero =[int(input(f"{i+1}. Introduce un número: \n")) for i in range (10)]
numero.sort()
cont = 1
pos = len(numero)-1
num = numero[pos]

for i in range(len(numero)):
    if numero [i] == num and i < pos:
        cont += 1
    elif i == pos:
        print(f"Cantidad de {numero[i-1]}: {cont}")