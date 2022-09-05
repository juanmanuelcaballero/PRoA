class personas:
    def __init__(self, nombre,apellido, direccion, fechanacimiento, DNI, numerotelefono, ID, gmail):
        self.nombre = nombre
        self.apellido =apellido
        self.direccion=direccion
        self.fechanacimiento= fechanacimiento
        self.DNI= DNI
        self.numerotelefono=numerotelefono
        self.ID=ID
        self.gmail=gmail
    

class bombero(persona): #bombero no estaba en clase persona
    def __init__(self, rango_cargo, cuartel, usuario, contraseña):
        self.rango_cargo=rango_cargo
        self.cuartel=cuartel
        self.usuario=usuario
        self.contraseña=contraseña
    def inicio_de_sesion(self):
        print("inicio de sesion")
    def carga_de_incidente(self):
        print("carga de incidente")
    def editar_incidente(self):
        print("editar incidente")
    def ver_incidente(self):
        print("ver incidente")
    def cargar_articulo(self):
        print("cargar articulo")
    def ver_listado_de_articulo(self):
        print("ver listado de articulo")
    def cargar_rodados(self):
        print("cargar rodados")
    def modificar_rodados(self):
        print("modificar rodados")
    def ver_rodados(self):
        print("ver rodados")
    def cargar_registro_economico(self):
        print("cargar registro economico")
    def modificar_registro_economico(self):
        print("modificar registro economico")
    def ver_registro_economico(self):
        print("ver registro economico")
    def modificar_datos_personales(self):
        print("modificar datos personales")
class incidente:
    def __init__(self, ubicacionincidente, tipo, damnificado, dotacion, fechasalida, horasalida, fecharetorno, horaretorno, datosinformante, moviles, daños, horaincidente, horallegada, llegadadotacion):
        self.ubicacionincidente=ubicacionincidente
        self.tipo=tipo
        self.damnificado=damnificado
        self.dotacion=dotacion
        self.fechasalida=fechasalida
        self.horasalida=horasalida
        self.fecharetorno=fecharetorno
        self.horaretorno=horaretorno
        self.llegadadotacion=llegadadotacion
class rodado:
    def __init__(self,patente, seguro, numeropoliza, fechanacimiento, tipo, estado):
        self.patente=patente
        self.seguro=seguro
        self.numeropoliza=numeropoliza
        self.fechanacimiento=fechanacimiento
        self.tipo=tipo
        self.estado=estado

class registros_economicos:
    def __init__(self,ingresos,egresos,fecha,motivoingreso,motivoegreso,numerofactura):
        self.ingresos=ingresos
        self.egresos=egresos
        self.fecha=fecha
        self.motivoingreso=motivoingreso
        self.motivoegreso=motivoegreso
        self.numerofactura=numerofactura
