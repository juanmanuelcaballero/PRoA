class personal:
    def __init__(self, cargo, cuartel, servicio, nombreusuario, contrasena, nombre, apellido, dni, fnacimiento, ID, numtelefono, gmail, domicilio):
        self.cargo = cargo
        self.cuartel = cuartel
        self.servicio = servicio
        self.nombreusuario = nombreusuario
        self.contrasena = contrasena
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni 
        self.fnacimiento = fnacimiento #muy buen trabajo
        self.ID = ID 
        self.numtelefono = numtelefono
        self.gmail = gmail
        self.domicilio = domicilio

    def iniciarsesion(self):
        pass
    def cargardatos(self):
        pass
    def editardatos(self):
        pass
    def verdatos(self):
        pass 
    def cargararticulos(self):
        pass 
    def verarticulos(self):
        pass 
    def modificararticulos(self):
        pass 
    def cargarrodados(self):
        pass 
    def modificarrodados(self):
        pass 
    def verrodados(self):
        pass 
    def cargarregistroeconomico(self):
        pass 
    def modificarregistroeconomico(self):
        pass 
    def verregistroeconomico(self):
        pass 
    def editarcuenta(self):
        pass 
        
julio = personal("Bombero", "VGB", "SI", "julio Casas", "hola123", "julio", "Casas", "2439283", "27/03/1980", "1", "+54 3546 505050", "juliopro27@gmail.com", "ojo de agua 27")
pedro = personal("Administracion", "Santa Rosa", "SI", "Pedro Suarez", "holaaaa222", "Pedro", "Suarez", "46399201", "12/3/1999", "2", "+54 3546 6663894","pedrosuarez99@gmail.com","Brasil 10")
pamela = personal("Cadete", "VGB", "Si", "Pame Ramirez", "Fiufiu", "Pamela", "Ramirez", "39.567.123", "17/09/1993", "4", "+54 3546 468696", "Pamera@gmail.com", "Ojo de agua 101")
martina = personal("Secretaria", "VGB", "si", "Martu Praniuk", "michichi", "Martina", "Praniuk", "37.665.572", "30/03/2000", "5", "+54 3546 789003", "martu89@gmail.com", "julio A. Roca")
Thomas = personal("Aspirante", "VGB", "Si", "Thom34", "Th0m4ss", "Thomas", "Gonzalez", "43.562.342", "08/03/2002", "78", "+54 3541 378809", "Thom4s8@gmail.com", "Calle Publica S/N")
Owen = personal("Sub oficial", "La cumbrecita", "Si", "owen32", "ochonumeros", "Owen", "Garetto", "23.567.809", "4/04/1984", "9", "+54 3546 789012", "owen32@gmail.com", "malvinas 65")
Matias = personal("Jefe", "VGB", "SI","elMatias28", "mati900297","Matias","Mesas","270986543","25/10/1997", "7","+54 3546 89760599","elmatias98@gmail.com", "El sauce 46")
Luciana = personal("Cadete", "Santa Rosa", "SI","Luciana Rodriguez", "luciana4504","Luciana","Rodriguez","35.467.892","14/9/1999", "8","+54 3546 54 7606","luciana2022@gmail.com", "El Durazno 5")
Jorge = personal("Cadete", "VGB", "SI","Jorge Manolo", "bomberos VGB","Jorge","Manolo","42.162.396","14/9/1999", "9","+54 3546 89 2636","jorgemano@gmail.com", "ojo de agua 1")
Elizabeth = personal("Cabo", "VGB", "SI","Eliz Paredes", "bomberos VGB","Elizabeth","Paredes","36.364.291","20/12/2000", "10","+54 3546 10 9306","Elizabethsi@gmail.com", "Magnolias 23")

class incidente:
    def __init__(self, tipo, lugar, damnificados, horasalida, fechasalida, horaretorno, fecharetorno, moviles, danos, horaincidente, horallegada):
        self.tipo = tipo
        self.lugar = lugar
        self.damnificados = damnificados
        self.horasalida = horasalida
        self.fechasalida = fechasalida
        self.horaretorno = horaretorno
        self.fecharetorno = fecharetorno
        self.moviles = moviles
        self.danos = danos
        self.horaincidente = horaincidente
        self.horallegada = horallegada


class rodados:
    def __init__(self, patente, seguro, numeropoliza, fechavencimiento):
        self.patente = patente
        self.seguro = seguro
        self.numeropoliza = numeropoliza
        self.fechavencimiento = fechavencimiento

nombre1 = rodados ("abc123", "La Caja", "28945749", "09/09/2022")
nombre2 = rodados ("edv546", "La Caja", "23652183", "15/03/2022")
nombre3 = rodados ("coh450", "La Caja", "32419567", "26/11/2023")

class consultas:
    def __init__(self, equipamientorodado):
        self.equipamientorodado = equipamientorodado

class registros_economicos:
    def __init__ (self, ingresos, egresos, fecha, motivoingreso, motivoegreso, nfactura):
        self.ingresos = ingresos
        self.egresos = egresos
        self.fecha = fecha
        self.motivoingreso = motivoingreso
        self.motivoegreso = motivoegreso
        self.nfactura = nfactura

dotacion = [personal, rodados, incidente]
print("Que archivos quieres ver? Opcion 1: Persona, Opcion 2: rodados")
opcion = float(input())
if opcion==1:
    print("Bombero 1:", julio.cargo, julio.cuartel, julio.servicio, julio.nombreusuario, julio.contrasena, julio.nombre, julio.apellido, julio.dni, julio.fnacimiento, julio.ID, julio.numtelefono, julio.gmail, julio.domicilio)
    print("Bombero 2:", pedro.cargo, pedro.cuartel, pedro.servicio, pedro.nombreusuario, pedro.contrasena, pedro.nombre, pedro.apellido, pedro.dni, pedro.fnacimiento, pedro.ID, pedro.numtelefono, pedro.gmail, pedro.domicilio)
    print("Bombero 3:", pamela.cargo, pamela.cuartel, pamela.servicio, pamela.nombreusuario, pamela.contrasena, pamela.nombre, pamela.apellido, pamela.dni, pamela.fnacimiento, pamela.ID, pamela.numtelefono, pamela.gmail, pamela.domicilio)
    print("Bombero 4:", martina.cargo, martina.cuartel, martina.servicio, martina.nombreusuario, martina.contrasena, martina.nombre, martina.apellido, martina.dni, martina.fnacimiento, martina.ID, martina.numtelefono, martina.gmail, martina.domicilio)
    print("Bombero 5:", Thomas.cargo, Thomas.cuartel, Thomas.servicio, Thomas.nombreusuario, Thomas.contrasena, Thomas.nombre, Thomas.apellido, Thomas.dni, Thomas.fnacimiento, Thomas.ID, Thomas.numtelefono, Thomas.gmail, Thomas.domicilio)
    print("Bombero 6:", Owen.cargo, Owen.cuartel, Owen.servicio, Owen.nombreusuario, Owen.contrasena, Owen.nombre, Owen.apellido, Owen.dni, Owen.fnacimiento, Owen.ID, Owen.numtelefono, Owen.gmail, Owen.domicilio)
    print("Bombero 7:", Matias.cargo, Matias.cuartel, Matias.servicio, Matias.nombreusuario, Matias.contrasena, Matias.nombre, Matias.apellido, Matias.dni, Matias.fnacimiento, Matias.ID, Matias.numtelefono, Matias.gmail, Matias.domicilio)
    print("Bombero 8:", Luciana.cargo, Luciana.cuartel, Luciana.servicio, Luciana.nombreusuario, Luciana.contrasena, Luciana.nombre, Luciana.apellido, Luciana.dni, Luciana.fnacimiento, Luciana.ID, Luciana.numtelefono, Luciana.gmail, Luciana.domicilio)
    print("Bombero 9:", Jorge.cargo, Jorge.cuartel, Jorge.servicio, Jorge.nombreusuario, Jorge.contrasena, Jorge.nombre, Jorge.apellido, Jorge.dni, Jorge.fnacimiento, Jorge.ID, Jorge.numtelefono, Jorge.gmail, Jorge.domicilio)
    print("Bombero 10:", Elizabeth.cargo, Elizabeth.cuartel, Elizabeth.servicio, Elizabeth.nombreusuario, Elizabeth.contrasena, Elizabeth.nombre, Elizabeth.apellido, Elizabeth.dni, Elizabeth.fnacimiento, Elizabeth.ID, Elizabeth.numtelefono, Elizabeth.gmail, Elizabeth.domicilio)

else:
    print("vehiculo 1", nombre1.patente, nombre1.fechavencimiento, nombre1.numeropoliza, nombre1.seguro)
    print("vehiculo 2", nombre2.patente, nombre2.fechavencimiento, nombre2.numeropoliza, nombre2.seguro)
    print("vehiculo 3", nombre3.patente, nombre3.fechavencimiento, nombre3.numeropoliza, nombre3.seguro)

print("¿Desea ingresar una dotacion?")
abn= input()
if abn == "si" or "Si" or "SI":
    print("Ingrese los datos de dotacion")
    d1 = input("Nombre/identificacion de la dotacion")
    d2 = input("Nombre de bomberos: ")
    d3 = input("Apellido: ")
    d4 = input("Cargos: ")
    d4_5 = input("Motio")
    d5 = input("Movil: ")
    d5_5 = input("Ubicacion")
    d6 = input("Fecha de salida: ")
    d7 = input("Fecha de llegada: ")
    d8 = input("Hora de salida: ")
    d9 = input("Hora de llegada: ")
    print ("La dotacion", d1, "salió a las", d8, "del dia", d6, "a", d5_5, "por un ", d4_5, "llegando a la ubicacion a las", d9, "del", d7)
    
elif abn == "no" or "No" or "NO": 
    print("OK.")