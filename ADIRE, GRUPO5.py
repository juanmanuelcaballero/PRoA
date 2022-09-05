class Personas:
    def __init__(self, nombre, apellido, DNI, fecha_de_nacimiento, ID, rol, numero_de_telefono, gmail, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.DNI = DNI
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.ID = ID
        self.rol = rol
        self.numero_de_telefono = numero_de_telefono
        self.gmail = gmail
        self.direccion = direccion 
        
class Bomberos(Personas):
    def __init__(self, cargo, cuartel, usuario, contrasenia):
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
#El texto de los prints esta de mas         
class Incidentes:
    def __init__(self,lugar,tipo,damnificados,dotacion,fecha_salida,hora_salida,fecha_retorno,hora_retorno,moviles,danios,hora_de_llegada_al_accidente,hora_de_incidente):
        self.lugar = lugar
        self.tipo = tipo
        self.damnificados = damnificados
        self.dotacion = dotacion
        self.fecha_salida = fecha_salida
        self.hora_salida = hora_salida
        self.fecha_retorno = fecha_retorno
        self.hora_retorno = hora_retoron
        self.moviles = moviles
        self.danios = danios
        self.hora_de_llegada_al_accidente = hora_de_llegada_al_accidente
        self.hora_de_incidente = hora_de_incidente

class Articulo:
    def __init__(self, tipo, estado):
        self.tipo = tipo
        self.estado = estado
class Rodados:
    def __init__(self, patente, seguro, numero_de_poliza, fechavencimiento):
        self.patente = patente
        self.seguro = seguro
        self.numero_de_poliza = numero_de_poliza
        self.fechavencimiento = fechavencimiento
class RegistrosEconomicos:
    def __init__(self, ingresos, egresos, fecha, motivo_de_ingreso, motivo_de_egreso, num_factura):
        self.ingresos = ingresos
        self.egresos = esgreso
        self.fecha = fecha
        self.motivo_de_ingreso = motivo_de_ingreso
        self.motivo_de_egreso = motivo_de_egreso
        self.num_factura = num_factura
        
