print("¿Desea ingresar un rodado? Si o No")
b=input()
if b == "Si":
    print("Ingrese los datos de los rodados: ")
    a0=input("Ingrese nombre del rodado: ")
    a1= input("Ingrese patente: ")
    a2=input("Ingrese seguro: ")
    a3=input("Ingrese numero de poliza: ")
    a4=input("Ingrese la fecha de vencimiento de poliza: ")
    print("El rodado", a0, "de patente", a1, "con el seguro", a2, "y numero de poliza", a3, "vence el", a4)
elif b == "No": 
    print("OK.")