import os
import random

lista = []
lista2 = []
c = 1

#pedir el ingreso de un numero por pantalla y luego imprimirlo

numero = int(input("Ingrese un numero\n"))
os.system("cls")
print("el numero ingresado es ", numero)

#utilizar el numero anterior para crear una lista que inicie en 1 y termine en el numero

while c <= numero:
    lista.append(c)
    
    c = c +1

print(lista)

#hacer una lista con numeros random y el largo debe ser la misma que el numero ingresado

for i in range(numero):
    lista2.append(random.randint(1, 100))
    
print(lista2)

#ordena los numeros de menor a mayor sin utilizar la funcion sorted o sort de list

for i in range(numero):
    for c in range(numero):
        if lista2[i] < lista2[c]:
            lista2.insert(c, lista2.pop(i))
            print(lista2)
            