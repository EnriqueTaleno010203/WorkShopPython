#Leer dos numeros e imprimir los numeros entre ellos
import os
os.system("cls||clear")
num1 = int(input("Valor de inicio "))
num2 = int(input("Valor final "))
cont = num1

if(num1 > num2):
    cont = num1 - 1
    while(cont > num2):
        print(cont)
        cont -= 1
else:
    cont = num1 + 1
    while(cont < num2):
        print(cont)
        cont += 1