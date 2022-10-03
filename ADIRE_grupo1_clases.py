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
persona1=("carla","lopez","los manantiales","2_10_2006","46716890","354678659","11.11.12","lopezcarla@gmail.com","cadete","la cumbrecita","carlafernandez","tu casita sabrosa" )
print("Ingrese una persona:")
persona2=("Micaela", "Rapisarda","Las verbenas","03_03_2003","46578987","6543262839","11.11.15","Micarapisarda@gmail.com","cadete","Villa General Belgrano","MicaelaRapisarda","mica1234")
persona3=("Ana","Fernandez", "los manantiales","2_6_2006","46543234","2567985436","11.11.16","anafernandez@gmail.com","cadete", "Villa Ciudad Parque","AnaFernandez", "ana1234")
persona4=("gabriel","lazarte","julio A. roca", "4_7_2002","46765345","4567989898","11.11.17","gabriellazarte@gmail.com","cadete","la cumbrecita","gabriellazarte","gabriel123")
persona5=("celeste","andrada","los molinos","2_5_1999","56543234","7878787878","11.11.18","celesteandrada@gmail.com","cadete", "la cumbrecita","celesteandrada","celeste123456")
persona6=("Lucila","petillo","los manantiales","8_9_1999","46578876","5656565656","11.11.19","lucilapetillo@gmail.com","cadete","villa general belgrano", "lucilapetillo","lucila1234")
persona7=("mirena","torres","las verbenas","4_8_1990","46578875","4656475656","11.11.20","mirenatorres@gmail.com","cadete","villa cuidada parque","mirenatorres","mirena1234")
persona8=("carmen","felipe","las verbenas","8_9_2000","56686767","4567454545","11.11.21","carmenfelipe@gmail.com","cadete","villa general belgrano","carmenfelipe","carmen1234")
persona9=("martina","praniuk","la cumbrecita","3_7_2000","56567567","5656565656","1.11.21","martinapraniuk@gmail.com","cadete","villa cuidad parque","martinapraniuk","martina1234")
persona10=("virginia","lopez","las verbenas","3_6_2000","46756456","4567767676","11.33.55","virginialopez@gmail.com","cadete","villa general belgrano","virginialopez","virginia234")     
a = input("Nombre: ")
b = input("Apellido: ")
c = input("direccion")
d = input("Fecha de nacimento: ")
e = input("DNI: ")
f = input("Numero de telefono: ")
g = input("ID: ")x
h = input("gmail: ")
i = input("Cargo: ")
j = input("Cuartel: ")
k = input("Nombre de usuario: ")
l = input("Contraseña: ")
persona11 = (a,b,c,d,e,f,g,h,i,j,k,l)
print(persona11.nombre, persona11.apellido, "vive en:", persona11.direccion, "nacio:", persona11.fecha_de_nacimiento, "su DNI es:", persona11.DNI, "su numero de telefono es:", persona11.numero_de_telefono, "su direccion ID:", persona11.ID, "su mail es:", persona11.gmail, "su cargo es:", persona11.rango_cargo, "pertenece al cuartel:", persona11.cuartel, "nombre de usuario:", persona11.usuario, "contraseña: NO VICIBLE")
class incidente:
    
    def __init__(self, ubicacion_del_incidente, tipo_de_incidente, damnificado, dotacion, fecha_de_salida, hora_de_salida, fecha_de_retorno, hora_de_retorno, datos_del_informante, moviles, daños, hora_del_incidente, hora_de_llegada, hora_de_llegada_de_la_dotacion_al_lugar_del_incidente):
        self.ubicacion_del_incidente=ubicacion_del_incidente
        self.tipo_de_incidente=tipo_de_incidente
        self.damnificado=damnificado
        self.dotacion=dotacion
        self.fecha_de_salida=fecha_de_salida
        self.hora_de_salida=hora_de_salida
        self.fecha_de_retorno=fecha_de_retorno
        self.hora_de_retorno=hora_de_retorno
        self.hora_de_llegada_de_la_dotacion_al_lugar_del_incidente=hora_de_llegada_de_la_dotacion_al_lugar_del_incidente
a = input("Ubicacion del incidente: ")
b = input("Tipo de incidente: ")
c = input("Damnificado: ")
d = input("Dotacion: ")
e = input("Fecha de salida: ")
f = input("Hora de salida: ")
g = input("Fecha de retorno: ")
h = input("Hora de retorno: ")
i = input("Hora de llegada de la dotacion al lugar del incidente: ")
incidente1 = (a,b,c,d,e,f,g,h,i)
print(incidente1)
class rodado:
    def __init__(self,patente, seguro, numero_de_poliza, fecha_de_vencimiento, tipo, estado):
        self.patente=patente
        self.seguro=seguro
        self:numero_de_poliza=numero_de_poliza
        self.fecha_de_vencimiento=fecha_de_vencimiento
        self.tipo=tipo
        self.estado=estado
rodado1=("123abc","SOS","000001","2050","autobomba","nuevo")
print("")
rodado2=("321cba","SOS","000002","2050","camionforestal","nuevo")
print("")
rodado3=("454ava","SOS","000003","2050","autoescala","nuevo")
print("")

class registros_economicos:
    def __init__(self,ingresos,egresos,fecha,motivo_de_ingreso,motivo_de_egreso,numero_de_factura):
        self.ingresos=ingresos
        self.egresos=egresos
        self.fecha=fecha
        self.motivo_de_ingreso=motivo_de_ingreso
        self.motivo_de_egreso=motivo_de_egreso
        self.numero_de_factura=numero_de_factura
