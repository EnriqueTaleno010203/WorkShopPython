import os
from math import pi, sqrt

def calcAreaCirc(radio):
    return round(pi * pow(radio, 2), 4)

def menu():
    op = 0
    while(op!=4):
        msn = """1. Calcular el area de un circulo
2. Calcular el cubo de un numero
3. Calcular la raiz cuadrada de un numero
4. Salir
    Digita tu opcion"""
        print(msn)
        op = int(input())
        if(op == 1):
            r = float(input("Dime un numero: "))
            print(f"El area circulo es {calcAreaCirc(r)}")
        elif(op == 2): 
            n = int(input("Dime un mumero: "))
            print(f"El cubo es: {pow(n,3)}")
        elif(op == 3):
            n = int(input("Dime un numero: "))
            print(f"La raiz cuadrada de un numero es: {sqrt(n)}")
        elif(op == 4):
            print("Adios...")
        else:
            print("Opcion invalida...")
        os.system("pause")

def main():
    
    menu()

if __name__== '__main__':
    main()