class Bomberos:
    def __init__(self, nombre, apellido, DNI, fecha_de_nacimiento, ID, rol, numero_de_telefono, gmail, direccion, cargo, cuartel, usuario, contrasenia):
        self.nombre = nombre
        self.apellido = apellido
        self.DNI = DNI
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.ID = ID
        self.rol = rol
        self.numero_de_telefono = numero_de_telefono
        self.gmail = gmail
        self.direccion = direccion 
        self.cargo = cargo
        self.cuartel = cuartel
        self.usuario = usuario
        self.contrasenia = contrasenia
    def iniciarsesion(self):
        print("iniciar sesion")
    def editarcuenta(self):
        print("editar cuenta")
    def cargarIncidente(self):
        print("cargar incidente")
    def editarIncidente(self):
        print("editar incidente")
    def verIncidente(self):
        print("ver incidente")
    def cargarInventario(self):
        print("cargar inventario")
    def editarInventario(self):
        print("editar inventario")
    def verInventario(self):
        print("ver inventario")
    def cargarRodados(self):
        print("cargar rodados")
    def editarRodados(self):
        print("editar rodados")
    def verRodados(self):
        print("ver rodados")
    def cargarRegisEconomico(self):
        print("cargar registro economico")
    def editarRegisEconomico(self):
        print("editar registro economico")
    def verRegisEconomico(self):
        print("ver registro economico")
    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.DNI} {self.fecha_de_nacimiento} {self.ID} {self.rol} {self.numero_de_telefono} {self.gmail} {self.direccion} {self.cargo} {self.cuartel} {self.usuario} {self.contrasenia}"

persona1= Bomberos("Leonel", "Messi", 46722652, "18/8/1982", 12345, "cabo", 455672, "messileonelAgmail.com", "islas malvinas 23", "sub jefe", "31/7", "lmessi", "Argentina2019")
persona2= Bomberos("Pepe", "Martinez", 46722532, "5/12/2000", 23456, "cadete", 405405, "pepemartinezAgmail.com", "salta 103", "cadete", "31/7", "pmartinez", "Argentina2019")
persona3= Bomberos("Diego", "Lungo", 97432652, "5/6/1985", 34567, "secretario", 485672, "dlungoAgmail.com", "cristo grande 65", "jefe", "31/7", "dlungo", "Argentina2019")
persona4= Bomberos("Claudio", "Cochi", 10132652, "5/11/1888", 45678, "cadete", 555672, "ccochiAgmail.com", "walter docsawer", "jefe", "31/7", "dlungo", "Argentina2019")
persona5= Bomberos("Paco", "Lopez", 45672652, "17/12/1987", 56789, "oficial", 676672, "pacolopez666Agmail.com", "Peru 48", "bombero", "31/7", "plopez", "Argentina2019")
persona6= Bomberos("Uriel", "Monina", 4672666, "6/6/1996", 67891, "cabo", 666666, "urieldiaboloAgmail.com", "ruta 5 km 666", "bombero", "31/7", "umonina", "Argentina2019")
persona7= Bomberos("Natalia", "Gimenez", 55722697, "28/12/2000", 78912, "cadete", 541496, "ngimenezAgmail.com", "lago hermoso 859", "bombera", "31/7", "ngimenez", "Argentina2019")
persona8= Bomberos("Gombal", "Waterson", 33322652, "24/8/1999", 89123, "cabo", 556672, "gombalwatersonAgmail.com", "islas malvinas 17", "bombero", "31/7", "gwaterson", "Argentina2019")
persona9= Bomberos("Arturo", "Vasquez", 44422652, "30/2/1898", 91234, "cabo", 765672, "arvasquezAgmail.com", "Jujuy 69", "bombero", "31/7", "avasquez", "Argentina2019")
persona10= Bomberos("Josefo", "Perez", 55522652, "24/6/2006", 94563, "cadete", 876672, "josefoAgmail.com", "islas malvinas 18", "bombero", "31/7", "jperez", "Argentina2019")



class Incidentes:
    def __init__(self,lugar,tipo,damnificados,dotacion,fecha_salida,hora_salida,fecha_retorno,hora_retorno,moviles,danios,hora_de_llegada_al_accidente,hora_de_incidente):
        self.lugar = lugar
        self.tipo = tipo
        self.damnificados = damnificados
        self.dotacion = dotacion
        self.fecha_salida = fecha_salida
        self.hora_salida = hora_salida
        self.fecha_retorno = fecha_retorno
        self.hora_retorno = hora_retorno
        self.moviles = moviles
        self.danios = danios
        self.hora_de_llegada_al_accidente = hora_de_llegada_al_accidente
        self.hora_de_incidente = hora_de_incidente

class Rodados:
    def __init__(self, patente, seguro, numero_de_poliza, fechavencimiento):
        self.patente = patente
        self.seguro = seguro
        self.numero_de_poliza = numero_de_poliza
        self.fechavencimiento = fechavencimiento

rodado1= ("jrl 354", "sancor", 54769875, "17/4/2023")
rodado2= ("lor 999", "sancor", 65432875, "17/4/2023")
rodado1= ("sqm 654", "sancor", 54769567, "17/4/2023")


print (persona1)
print (persona2)
print (persona3)
print (persona4)
print (persona5)
print (persona6)
print (persona7)
print (persona8)
print (persona9)
print (persona10)


#creo lista
l=[]


#asigno valores a las variables
print("-------")
print("-------")
print("-------")
print("Ingrese los siguientes datos: ")
nombre=input("Nombre:")
apellido=input("Apellido:")
DNI=int(input("DNI: "))
fechanacimiento=input("Fecha de nacimiento: ")
ID=int(input("ID: "))
rol=input("Rol: ")
numtelefono=int(input("Numero de telefono: "))
gmail=input("Gmail: ")
direccion=input("Direccion: ")
cargo=input("Cargo:")
cuartel=input("Cuartel: ")
usuario=input("Usuario: ")
contrasenia=input("Contraseña: ")


#ingreso las variables a la lista
l.append(nombre)
l.append(apellido)
l.append(DNI)
l.append(fechanacimiento)
l.append(ID)
l.append(rol)
l.append(numtelefono)
l.append(gmail)
l.append(direccion)
l.append(cargo)
l.append(cuartel)
l.append(usuario)
l.append(contrasenia)

#imprimo la lista ysi
print(l)

#ignoren esto, solo lo puse porque quiero preguntar si esta bien o es cualquier verdura lol
#l2= []
#l2.append(Bomberos("Leonel", "Messi", 46722652, "18/8/1982", 12345, "cabo", 455672, "messileonelAgmail.com", "islas malvinas 23", "sub jefe", "31/7", "lmessi", "Argentina2019"))
#print(l2)
