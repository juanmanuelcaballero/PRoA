a = input("Ingrese usuario: ")
b = input("Ingrese contraseña: ")
if len(a) > 10:
    print("Usuario no valido")
if len(b)< 5:
    print("La contraseña debe contener mas de 5 caracteres")




#------------------------------------


print("¿Desea ingresar un incidente? Si o No: ")
b=input()
if b == "Si":
    print("Ingrese los datos del incidente: ")
    b0=input("Ingrese tipo del incidente: ")
    b1= input("Ingrese fecha: ")
    b2=input("¿Desea ingresar daños a la propiedad? Si o No: ")
    if b2 == "Si":
        p1=input ("Superficie afectada: ")
        p2=input("Tipo de combustible: ")
        p3=input("Pérdida de vivienda: ")
        p3_1= input("Tipo de vivienda: ")
        p4=input("Pérdida de animales: ")
        p4_1=input("Tipo de animales: ")

        print("El tipo de incidente es:", b0, "el dia:", b1, ", la superficie afectada fue:", p1, ", el tipo de combustible fue:", p2,",", p3_1, "fue afectada:", "los animales afectados fueron: ", p4_1)
    elif b2 == "No":
        print("Ok.")
    
elif b == "No": 
    print("OK.")