class Personas:
    def __init__(self, nombre, apellido, DNI, fechanacimiento, ID, rol, numerotelefono, gmail, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.DNI = DNI
        self.fechanacimiento = fechanacimiento
        self.ID = ID
        self.rol = rol
        self.numerotelefono = numerotelefono
        self.gmail = gmail
        self.direccion = direccion 
        
class Bomberos(Personas):
    def __init__(self, cargo, cuartel, usuario, contrasena):
        self.cargo = cargo
        self.cuartel = cuartel
        self.usuario = usuario
        self.contrasena = contrasena
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
#El texto de los prints esta de mas         
class Incidentes:
    def __init__(self,lugar,tipo,damnificados,dotacion,fechasalida,horasalida,fecharetorno,horaretorno,moviles,danos,horallegadaaccidente,horaincidente):
        self.lugar = lugar
        self.tipo = tipo
        self.damnificados = damnificados
        self.dotacion = dotacion
        self.fechasalida = fechasalida
        self.horasalida = horasalida
        self.fecharetorno = fecharetorno
        self.horaretorno = horaretorno
        self.moviles = moviles
        self.danos = danos
        self.horallegadaaccidente = horallegadaaccidente
        self.horaincidente = horaincidente

class Articulo:
    def __init__(self, tipo, estado):
        self.tipo = tipo
        self.estado = estado
class Rodados:
    def __init__(self, patente, seguro, numeropoliza, fechavencimiento):
        self.patente = patente
        self.seguro = seguro
        self.numeropoliza = numeropoliza
        self.fechavencimiento = fechavencimiento
class RegistrosEconomicos:
    def __init__(self, ingresos, egresos, fecha, motivoingreso, motivoegreso, numfactura):
        self.ingresos = ingresos
        self.egresos = egresos
        self.fecha = fecha
        self.motivoingreso = motivoingreso
        self.motivoegreso = motivoegreso
        self.numfactura = numfactura
        
