#Leer x cantidad de numeros e imprimir la lista ordenada
import os
os.system("cls")
numbers = list()

op = 'si'
while(op.upper() != 'NO'):
    num = int(input("Escribe un numero: "))
    numbers.append(num)
    op = input("Desea ingresar otro si - no: ")

numbers.sort()

print(numbers)

numbers.sort(reverse=True)
print(numbers)