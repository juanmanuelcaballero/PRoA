edad = input("Indique su edad: ")
if edad > "0" and edad < "130":
    if edad >= "18":
        print("Sos mayor de edad")
        if edad >= "60":
            print("Sos anciano")
        else:
            print("Sos adulto")
    else:
        print("Sos menor de edad")
        if edad >= "12":
            print("Sos un adolescente")
        else:
            print("Sos un niño")
else:
    print("Ingrese un valor válido")
