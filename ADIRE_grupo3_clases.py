class persona:
    def __init__(self,nombre,apellido,DNI,fecha_de_nacimiento,ID):
        self.nombre=nombre
        self.apellido=apellido
        self.DNI=DNI
        self.fecha_de_nacimiento
        self.ID=ID
class bombero(persona):
    def __init__(self,cargo,cuartel,usuario,contraseña, mail, telefono):
        super(persona)
        self.cargo=cargo
        self.cuartel=cuartel
        self.usuario=usuario
        self.contraseña=contraseña
        self.mail = mail
        self.telefono = telefono
    def IniciarSesion(self):
        print()
    def CargarIncidente(self):
        print()
    def EditarIncidente(self):
        print()
    def VerIncidente(self):
        print()
    def CargarIncidente(self):
        print()
    def Ver_listado_de_Articulos(self):
        print()
    def Modificar_Listado_de_articulos(self):
        print()
    def Cargar_rodados(self):
        print()
    def Modificar_rodados(self):
        print()
    def Ver_rodados(self):
        print()
    def Cargar_registo_economico(self):
        print()
    def Modificar_registro_economico(self):
        print()
    def Ver_registro_economico(self):
        print()
    def Editar_cuenta(self):
        print()

class Incidentes:
    def __init__(self, lugar, tipo, damnificados, dotacion, fecha_de_salida, hora_del_incidente, hora_de_salida, moviles, fecha_de_retorno, hora_de_retorno, daños, hora_llegada_dotacion):
        self.lugar = lugar
        self.tipo = tipo
        self.damnificados = damnificados
        self.dotacion = dotacion
        self.fecha_de_salida = fecha_de_salida
        self.hora_de_salida = hora_de_salida
        self.moviles = moviles
        self.fecha_de_retorno = fecha_de_retorno
        self.hora_de_retorno = hora_de_retorno
        self.daños = daños
        self.hora_llegada_dotacion = hora_llegada_dotacion
class articulos:
    def __init__(self,tipo,estado):
        self.tipo= tipo
        self.estado = estado
class rodados(articulos):
    def __init__(self,patente,numero_de_piliza,seguro,fecha_de_vencimiento):
        self.patente= patente
        self.numero_de_poliza= numero_de_poliza
        self.seguro= seguro
        self.fechadevencimieto= fecha_de_vencimineto
class registros_economicos:
    def __init__(self,ingresos,egresos,numero_factura,fecha,motivo_de_ingreso,motivo_de_egreso):
        self.ingresos=ingresos
        self.egresos=egresos
        self.numero_factura=numero_factura
        self.fecha=fecha
        self.motivo_de_ingreso=motivo_de_ingreso
        self.motivo_de_egreso=motivo_de_egreso

persona1 = ("Juan.png", "El Pepe", 17394726, "31/7/1923", 1, "Teniente", "San Juan", "JuanMaster", "Juan123", "etesech@bomberos.com.ar", 836592)
persona2 = ("Astas", "Sandalias", 19735285, "1/8/1921", 2, "Sargento", "Mendoza", "TheGasper", "Astas123", "thegasper@bomberos.com.ar", 937602)
persona3 = ("gonzalo.png", "El Pepe", 17394726, "12/3/1923", 3, "Teniente doas", "San Juan", "gonzalomaster", "gonza123", "thegonzamasterpromax@bomberos.com.ar", 8352836592)
persona4 = ("Carlos", "Alberto", 47345675, "15/4/1999", 4, "Cabo", "Barcelona", "CarlitosA", "C45", "Carlos@bomberos.com.ar", 8466836592)
persona5 = ("Francisco", "Guzman", 23456785, "23/8/1994", 5, "Cadete", "Despeñaderos", "FranciscoDEspe", "1234567890", "Fran@bomberos.com.ar", 3546836592)
persona6 = ("Mariana", "Schult", 95966935, "31/12/1962", 6, "Limpieza", "San Luis", "mari935", "Juan321", "XxMarianaxX@bomberos.com.ar", 8352823108)
persona7 = ("Sofi", "Ejea", 27397726, "31/7/1998", 7, "Teniente", "San Miguel", "sofie", "Sofilamaspro", "XxsofixX@bomberos.com.ar", 8352784924)
persona8 = ("Enrique","Peter", 26789123, "13/4/1999", 8, "aguatero", "Cordoba", "peter2", "Peteter123", "josesitoeltravieso@bomberos.com.ar", 123456789)
persona9 = ("Agustin","guzaman", 23456789, "9/5/2000", 9, "coronelII", "Santa Cruz", "Agus", "AguateBokita", "Aguselpicante@bomberos.com.ar", 987543299)
persona10 = ("Agostina","Pate", 45671235, "25/12/1999", 10, "Aguatero Suplente", "Mendoza", "Aguitarefrescante", "refrecanteaguita", "aguaaaaa@bomberos.com.ar", 2345671234)


vehiculo1 = ("123fgh","12/2024", 12345678,"san cristobal seguros")
vehiculo2 = ("845ibe", "01/2027", 65815432, "san cristobal seguros")
vehiculo3 = ("945tds", "08/2031", 53987123, "san cristobal seguros")




sdfgh = input("Ingrese1 para iniciar sesion 2 para registrarse: ")

if sdfgh == "1":
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: \n")

elif sdfgh == "2":
    Mail = input("Mail: ")
    Usuario = input("Nombre de usuario: ")
    Contraseña = input("Contraseña: \n")

else:
    print("Numero incorrecto")

print("ingrese un incidente ")
vasd=input("lugar: ")
wasd=input("tipo: ")
hasd=input("damnificado: ")
pasd=input("dotacion: ")
kasd=input("fecha de salida: ")
yasd=input("hora de incidente:  ")
qasd=input("hora de salida: ")
xasd=input("moviles: ")
zasd=input("fecha de retorno: ")
fasd=input("daños: ")
masd=input("hora  llegada dotacion: ")
lista43=[vasd, wasd, hasd, pasd, kasd, yasd, qasd, xasd, zasd, fasd, masd]
print(lista43 ,"\n")



x = input("Ingrese 1 si es persona, 2 si es vehículo o 3 para dotacion: ")



if x == "1":
    print("Ingrese una persona")
    z = input("Nombre: ")
    e = input("Apellido: ")
    g = input("DNI: ")
    r = input("Fecha de nacimento: ")
    u = input("Cargo: ")
    o = input("Cuartel: ")
    s = input("Nombre de usuario: ")
    a = input("Contraseña: ")
    h = input("Gmail: ")
    w = input("Numero de telefono: ")
    lista1=[z,e,g,r,u,o,s,a,h,w,persona1,persona2,persona3,persona4,persona5,persona6,persona7,persona8,persona9,persona10]
    print(lista1) 

elif x == "2":
    print("Ingrese un vehiculo")
    y = input("numero de matricula: ")
    n = input("fecha de vencimiento: ")
    i = input("numero de poliza: ")
    k = input("seguro: ")
    lista2=[y,n,i,k, vehiculo1, vehiculo2, vehiculo3]
    print(lista2)

elif x == "3":
    ff = input("Ingrese nombre: ")
    ss = input("Ingrese apellido: ")
    df = input("Ingrese DNI: ")
    dfg = input("Ingrese direccion: ")
    sdfg = input("Ingrese ubicacion: ")
    lista3 = [ff, ss, df, dfg, sdfg]
    print(lista3)
    
else:
    print("Número incorrecto")


