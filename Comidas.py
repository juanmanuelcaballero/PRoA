print("Vamos a seleccionar una comida del menú")
print("Escribe tu nombre:")

nombre = input()
print('¿Comés carne? Responda solamente "si" o "no"')

carne = input() #Pregunta si el usuario consume carne

if carne=="si":
    print("Selecciona una opción:")
    print("Bife con ensalada")
    print("Milanesa con puré")
    print("Pechuga de pollo con papas fritas")
else:
    print("¿Comés huevos y lácteos?")
    huevos = input()
    if huevos=="si":
        print("Seleccione una opción vegetariana:")
        print("Pizza de muzzarella")
        print("Tortilla de acelga")
        print("Ravioles de verdura y ricota")
    else:
        print("Seleccione una opción vegana:")
        print("Hamburguesas de legumbres con ensalada")
        print("Ensalada de tomate, lechuga y choclo")
        print("Wok de vegetales")
plato = input()

print(nombre," seleccionaste ",plato,". Ya tomamos tu pedido.", sep='')
print(len(nombre))

if len(nombre) >= 6:
    if len(nombre) > 15:
        print('Tu nombre es muuuuuuuy largo')
    else:
        print('Tu nombre es largo')
else:
    print('Tu nombre es corto')


