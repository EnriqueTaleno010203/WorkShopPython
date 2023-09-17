#Calcular el IVA de un producto
def calculateVAT(price):
    return price * 0.15

def showTotal(price, vat):
    return price + vat

def main():
    price = int(input("Diga el precio del producto"))
    vat = calculateVAT(price)
    total = showTotal(price, vat)
    print(f"Price {price}")
    print(f"IVA {vat}")
    print(f"Total {total}")

