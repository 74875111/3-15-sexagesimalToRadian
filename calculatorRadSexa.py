import math


class calculatorRadSexa:
    def __init__(self):
        self.number = float(input("Ingrese numero: "))
    def convert(self):
        print("1. Convertir grados sexagesimales a radianes")
        print("2. Convertir radianes a grados sexagesimales")
        option=input("Elija opción: ")
        if option=="1":
            print(f"Grados sexagesimales a radianes es : {math.radians(self.number)}")
        elif option=="2":
            print(f"Radianes a grados sexagesimales es : {math.degrees(self.number)}")
        else:
            print("Opcion no valida")

