"""
Crear un programa que lea por teclado un número entero y que almacene el mismo en un
array de modo que cada cifra ocupe un elemento del array. Ejemplo: si leo el número
23451, se generará el array: 23451
"""

num = []
numero = input("Introduce un número. (Máximo 10 cifras): ")
escapicua = True

for i in range(len(numero)//2):
    if numero[i] == numero[len(numero) - 1 - i]:
        esCapicua = False

print(escapicua)