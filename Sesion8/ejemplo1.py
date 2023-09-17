#Deseo una lista de numeros y quiero calcular la media
from os import system
from statistics import median, mean
numbers = list()

def addNumber(number):
    number.append(number)

def readNumber():
    number = int(input("Ingrese un numero: "))
    addNumber(number)

def showNumbers():
    for number in numbers:
        print(number)

#zzz
def getAverage():
    suma = 0
    for number in numbers:
        suma += number
    avg = suma/len(numbers)
    return avg

#god
def getAvg():
    return mean(numbers)

def menu():
    op = int(input("""
1. Ingresar
2. Mostrar
3. Media
4. Salir
Dime tu Opcion:
"""))
    return op

def main():
    op = 0
    while(op! = 3):
        system("cls")