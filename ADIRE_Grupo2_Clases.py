class persona:
    def __init__ (self, nombre, apellido, dni, fnacimiento, ID, numtelefono, gmail, domicilio, rol):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni 
        self.fnacimiento = fnacimiento
        self.ID = ID 
        self.numtelefono = numtelefono
        self.gmail = gmail
        self.domicilio = domicilio
        self.rol = rol


class bomberos:
    def __init__(self, cargo, cuartel, servicio, nombreusuario, contrasena, iniciarsesion, cargardatos, editardatos, verdatos, cargararticulos, verarticulos, modificararticulos, cargarrodados, modificarrodados, verrodados, cargarregistroeconomico, modificarregistroeconomico, verregistroeconomico, editarcuenta):
        self.cargo = cargo
        self.cuartel = cuartel
        self.servicio = servicio
        self.nombreusuario = nombreusuario
        self.contrasena = contrasena
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
        self.horaincinte = horaincidente
        self.horallegada = horallegada


class rodados:
    def __init__(self, patente, seguro, numeropoliza, fechavencimiento):
        self.patente = patente
        self.seguro = seguro
        self.numeropoliza = numeropoliza
        self.fechavencimiento = fechavencimiento

class consultas:
    def __init__(self, equipamientorodado):
        self.equipamientorodado = equipamientorodado

class registros_economicos:
    def __init__ (self, ingresos, egresos, fecha, motivoingreso, motivoegreso,nfactura):
        self.ingresos = ingresos
        self.egresos = egresos
        self.fecha = fecha
        self.motivoingreso = motivoingreso
        self.motivoegreso = motivoegreso
        self.nfactura = nfactura