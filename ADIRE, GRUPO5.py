from xml.dom.minidom import DOMImplementation


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
"""
Lbomberos=[persona1,persona2,persona3,persona4]
for i in Lbomberos:
    print("i qsy matenme joda")"""


#print("Bomberos en servicio: ")
#print (persona1)
#print (persona2)
#print (persona3)
#print (persona4)
#print (persona5)
#print (persona6)
#print (persona7)
#print (persona8)
#print (persona9)
#print (persona10)


class Rodados:
    def __init__(self, patente, seguro, numeroPoliza, fechaVencimiento):
        self.patente = patente
        self.seguro = seguro
        self.numeroPoliza = numeroPoliza
        self.fechaVencimiento = fechaVencimiento
    def __str__(self):
        return f"{self.patente} {self.seguro} {self.numeroPoliza} {self.fechaVencimiento}"

rodado1= Rodados("jrl 354", "sancor", 54769875, "17/4/2023")
rodado2= Rodados("lor 999", "sancor", 65432875, "17/4/2023")
rodado1= Rodados("sqm 654", "sancor", 54769567, "17/4/2023")

#print(rodado1)


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
    def __str__(self):
        return f"{self.lugar} {self.tipo} {self.damnificados} {self.dotacion} {self.fecha_salida} {self.hora_salida} {self.fecha_retorno} {self.hora_retorno} {self.moviles} {self.danios} {self.hora_de_llegada_al_accidente} {self.hora_de_incidente}"



dotacionL =[]
dotacionL.append("La dotacion que acudió al incidente fue conformada por los bomberos: ")
dotacionL.append("Messi")
dotacionL.append("Lungo")
dotacionL.append("Vazquez")
dotacionL.append("Lopez")
dotacionL.append("Gimenez")

#incidente1= Incidentes(" Incidente en el Pozo Verde\n","Hubo un Accidente vehicular\n","Juanita Perez muere no te lo vas a creer\n",dotacionL,"15/9/2022\n","11:53\n","15/9/2022\n","13:02\n",rodado1, "Fractura del femur, Vidrios rotos\n","12:00\n","11:50\n")
incidenteL=[]

print ("cargue el incidente")
lugar =input ("lugar: ")
tipo = input ("tipo: ")
damnificados =input ("damnificados: " )
dotacion=input ("dotacion: " )
fecha_salida=input ("fecha de salida: " )
hora_salida=input ("hora de salida: " )
fecha_retorno=input ("fecha de retono: " )
hora_retorno=input ("hora de retorno: " )
moviles=input ("moviles: " )
danios=input ("danios : " )
hora_de_llegada_al_incidente=input ("hora de llegada al aciddente: " )
hora_de_incidente=input ("hora de incidente: " )


incidenteL.append("Lugar: ")
incidenteL.append(lugar)

incidenteL.append("Tipo: ")
incidenteL.append(tipo)

incidenteL.append("damnificados: ")
incidenteL.append(damnificados)

incidenteL.append("dotacion: ")
incidenteL.append(dotacion)

incidenteL.append("fecha de salida: ")
incidenteL.append(fecha_salida)

incidenteL.append("hora de salida: ")
incidenteL.append(hora_salida)

incidenteL.append("fecha de retorno: ")
incidenteL.append(fecha_retorno)

incidenteL.append("hora de retorno: ")
incidenteL.append(hora_retorno)

incidenteL.append("moviles: ")
incidenteL.append(moviles)

incidenteL.append("daños: ")
incidenteL.append(danios)

incidenteL.append("hora de llegada al incidente: ")
incidenteL.append(hora_de_llegada_al_incidente)

incidenteL.append("hora_de_incidente: ")
incidenteL.append(hora_de_incidente)

for incidente1 in incidenteL:
    print (incidente1)


print("-------")
print("-------")
print("-------")
print("Cargar datos:")
l=[]
print("-------")
print("-------")
print("-------")
print("Ingrese los siguientes datos para ingresar un nuevo bombero al sistema: ")
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
for bomberos1 in l:
    print(bomberos1)



lr=[]
print("-------")
print("-------")
print("-------")
print("Ingrese los siguientes datos para ingresar un nuevo rodado al sistema: ")
patente=input("Patente:")
seguro=input("Seguro:")
fechaVencimiento=input("Fecha de vencimiento: ")
numPoliza=int(input("Numero de poliza: "))
lr.append(patente)
lr.append(seguro)
lr.append(fechaVencimiento)
lr.append(numPoliza)
for coche in lr:
    print(coche)
