#Uso de parametros
#Leer el nombre y el apellido de una persona y mostrar su nombre completo

import os
os.system("cls")
os.system("color a5")

def getFullName(fName, sName):
    return f"{fName} {sName}"

def main():
    fName = input("Dime tu nombre: ")
    sName = input("Dime tu apellido: ")
    print(f"El nombre completo es {getFullName(fName, sName)}")

if __name__ == "__main__":
    main()