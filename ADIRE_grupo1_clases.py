class personas:
    def __init__(self, nombre,apellido, direccion, fecha_de_nacimiento, DNI, numero_de_telefono, ID, gmail,rango_cargo, cuartel, usuario, contraseña):
        self.nombre = nombre
        self.apellido =apellido
        self.direccion=direccion
        self.fecha_de_nacimiento= fecha_de_nacimiento
        self.DNI= DNI
        self.numero_de_telefono=numero_de_telefono
        self.ID=ID
        self.gmail=gmail
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
persona1=("carla","lopez","los manantiales","2_10_2006","46716890","354678659","11.11.12","lopezcarla@gmail.com","cadete","la cumbrecita","carlafernandez","tu casita sabrosa")
print("Ingrese una persona")
a = input("Nombre: ")
b = input("Apellido: ")
c = input("direccion")
d = input("Fecha de nacimento: ")
e = input("DNI: ")
f = input("Numero de telefono: ")
g = input("ID: ")
h = input ("gmail: ")
i = input("Cargo: ")
j = input("Cuartel: ")
k = input("Nombre de usuario: ")
l = input("Contraseña: ")
persona2 = (a,b,c,d,e,f,g,h,i,j,k,l)
print(persona2)
class incidente:
    def __init__(self, ubicacion_del_incidente, tipo, damnificado, dotacion, fecha_de_salida, hora_de_salida, fecha_de_retorno, hora_de_retorno, datos_del_informante, moviles, daños, hora_del_incidente, hora_de_llegada, hora_de_llegada_de_la_dotacion_al_lugar_del_incidente):
        self.ubicacion_del_incidente=ubicacion_del_incidente
        self.tipo=tipo
        self.damnificado=damnificado
        self.dotacion=dotacion
        self.fecha_de_salida=fecha_de_salida
        self.hora_de_salida=hora_de_salida
        self.fecha_de_retorno=fecha_de_retorno
        self.hora_de_retorno=hora_de_retorno
        self.hora_de_llegada_de_la_dotacion_al_lugar_del_incidente=hora_de_llegada_de_la_dotacion_al_lugar_del_incidente

class rodado:
    def __init__(self,patente, seguro, numero_de_poliza, fecha_de_nacimiento, tipo, estado):
        self.patente=patente
        self.seguro=seguro
        self:numero_de_poliza=numero_de_poliza
        self.fecha_de_nacimiento=fecha_de_nacimiento
        self.tipo=tipo
        self.estado=estado
rodado1=("abc123", "sos", "14583965", "2010", "autobomba", "nueva")
class registros_economicos:
    def __init__(self,ingresos,egresos,fecha,motivo_de_ingreso,motivo_de_egreso,numero_de_factura):
        self.ingresos=ingresos
        self.egresos=egresos
        self.fecha=fecha
        self.motivo_de_ingreso=motivo_de_ingreso
        self.motivo_de_egreso=motivo_de_egreso
        self.numero_de_factura=numero_de_factura
