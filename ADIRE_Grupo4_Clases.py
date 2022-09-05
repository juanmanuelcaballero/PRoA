"""from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen"""
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

class bomberos(persona):
    def __init__(self, cargo, cuartel, servicio, nombreusuario, contrasenia, iniciarsesion, cargardatos, editardatos, verdatos, cargararticulos, verarticulos, modificararticulos, cargarrodados, modificarrodados, verrodados, cargarregistroeconomico, modificarregistroeconomico, verregistroeconomico, editarcuenta):
        self.cargo = cargo
        self.cuartel = cuartel
        self.servicio = servicio
        self.nombreusuario = nombreusuario
        self.contrasenia = contrasenia
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
    def __init__(self, tipo, lugar, damnificados, horadesalida, fechadesalida, horaderetorno, fechaderetorno, moviles, daños, horadelincidente, horadellegada):
        self.tipo = tipo
        self.lugar = lugar
        self.damnificados = damnificados
        self.horadesalida = horadesalida
        self.fechadesalida = fechadesalida
        self.horaderetorno = horaderetorno
        self.fechaderetorno = fechaderetorno
        self.moviles = moviles
        self.daños = daños
        self.horadelincidente = horadelincidente
        self.horadellegada = horadellegada


class articulos:
    def __init__(self, estado, tipo, cantidad):
        self.estado = estado
        self.tipo = tipo
        self.cantidad = cantidad

class rodados:
    def __init__(self, patente, seguro, numerodepoliza, fechadevencimiento):
        self.patente = patente
        self.seguro = seguro
        self.numerodepoliza = numerodepoliza
        self.fechadevencimiento = fechadevencimiento

class consultas:
    def __init__(self, equipamientoderodado):
        self.equipamientoderodado = equipamientoderodado

class registros_economicos:
    def __init__ (self, ingresos, egresos, fecha, motivoingreso, motivoegreso,nfactura):
        self.ingresos = ingresos
        self.egresos = egresos
        self.fecha = fecha
        self.motivoingreso = motivoingreso
        self.motivoegreso = motivoegreso
        self.nfactura = nfactura
#
class Inicio(Screen):
    pass
KV = '''
MDBoxLayout:
    orientation: "vertical"

    MDTopAppBar:
        title: "asd"

    MDLabel:
        text: "Content"
        halign: "center"
'''

class asd(MDApp):
    def build(self):
        return Builder.load_string(KV)

asd().run()#
