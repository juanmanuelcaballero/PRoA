class persona():
    def __init__(self,nombre,apellido,DNI,fecha_de_nacimiento,ID):
        self.nombre=nombre
        self.apellido=apellido
        self.DNI=DNI
        self.fecha_de_nacimiento
        self.ID=ID
class bombero():
    def __init__(self,cargo,cuartel,usuario,contraseña):
        self.cargo=cargo
        self.cuartel=cuartel
        self.usuario=usuario
        self.contraseña=contraseña
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
class articulos(self):
    def __init__(self,tipo,estado)
    self.tipo= tipo
    self.estado = estado
class rodados(articulos):
    def __init__(self,patente,numero_de_piliza,seguro,fecha_de_vencimiento):
        self.patente= patente
        self.numero_de_poliza= numero_de_poliza
        self.seguro= seguro
        self.fechadevencimieto= fecha_de_vencimineto
class registros_economicos (self):
    def __init__(self,ingresos,egresos,numero_factura,fecha,motivo_de_ingreso,motivo_de_egreso):
        self.ingresos=ingresos
        self.egresos=egresos
        self.numero_factura=numero_factura
        self.fecha=fecha
        self.motivo_de_ingreso=motivo_de_ingreso
        self.motivo_de_egreso=motivo_de_egreso
