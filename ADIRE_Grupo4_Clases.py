from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
class personal:
    def __init__ (self, nombre, apellido, dni, fnacimiento, numtelefono, gmail, domicilio, rango):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni 
        self.fnacimiento = fnacimiento
        self.numtelefono = numtelefono
        self.gmail = gmail
        self.domicilio = domicilio
        self.rango = rango
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
    def imprimir(self):
        print(self.nombre, self.apellido, self.dni, self.fnacimiento, self.numtelefono, self.gmail, self.domicilio, self.rango)    
        print("")
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
    def __init__(self, patente, seguro, numerodepoliza, fechadevencimiento, equipamiento):
        self.patente = patente
        self.seguro = seguro
        self.numerodepoliza = numerodepoliza
        self.fechadevencimiento = fechadevencimiento
        self.equipamiento = equipamiento
    def imprimir(self):
        print(self.patente, self.seguro, self.numerodepoliza, self.fechadevencimiento, self.equipamiento)
        print("")

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

class Inicio(Screen):
    pass
KV = '''
MDBoxLayout:
    orientation: "vertical"

    MDTopAppBar:
        title: "asd"

    FloatLayout
        Button:
            text: "asddsa"
            halign: "center"
            size_hint: (0.5, 0.5)
        Button:
            text: "dsaasd"
            halign: "center"
            size_hint: (0.2, 0.1)
'''

class asd(MDApp):
    def build(self):
        return Builder.load_string(KV)


a = personal("Caleb", "Wharton", 95966365, "4-10-1979", "+54 221 3101100", "cwharton@yahoo.com", "512, 954", "Aspirante" )
b =personal("Aiden", "Walker",95966366,  "8-10-2000", "+54 221 3174023", "awalker@hotmail.com", "Los manantiales, 444", "Aspirante")
c =personal("Jane", "Su", 95966367, "5-7-1980", " +54 221 3534666", "jsu@outlook.com", "Maracaibo, 678", "Cabo")
d =personal("Jack", "Ross", 95966368, "9-9-1999", " +54 221 4341806", "jackr@yahoo.com",  "hUTLINGHAM, 246", "Cadete" )
e = personal("JJ", "Mayblank", 95966369, "2-5-1998", "+54 221 4372972", "jjm@yahoo.com", "Caraval, 101", "Cadete" )
f =personal("Sue", "MARTINEZ", 95966370, "8-8-1977","+54 221 4380831", "smartinez@yahoo.com", "Cerro Negro, 116", "Cabo" )
g =personal("Scarlett", "Dragna", 95966371, "24-6-2001","+54 221 5021283", "scarlettd@gmail.com",  "Jerusalen, 777", "Aspirante")
h =personal("Carl", "White", 95966372, "5-2-2007", "+54 221 5716293", "cwhite@yahoo.com", "Chile, 234", "Aspirante")
i =personal("Andrew", "Smith", 95966373, "15-9-1994", "+54 221 5856712", "asmith@gmail.com", "Washington DC, 453", "Jefe")
j = personal("Aegan", "Cash", 95966374, "19-03-1997",  "+54 221 6613526", "yositehubieraelegidoati@hotmail.com","Tagus, 0319", "Aspirante")
bomberoslista=[a,b,c,d,e,f,g,h,i,j]
R1 = rodados("RPF-321","Rivadavia","12345678", "5-3-2025", "Vacío")
R2 = rodados("PIF-430","Greenday","87654321", "18-1-2021", "Vacío" )
R3 = rodados("JCJ-232","Sancor","45687312", "29-12-2028", "Vacío" )


valor2=input("¿que quieres persona(1) o rodado(2)? ")
if valor2 == "1":
    print("""Ingrese los sisuientes datos:
    Nombre
    Apellido
    DNI
    Fecha de nacimiento
    Numero de telefono
    Gmail
    Domicilio
    Rango""")
    vari2= []
    for persona in range (9):
        jfdjfjk= input()
        vari2.append(jfdjfjk)
    ae=personal(vari2[0],vari2[1],vari2[2],vari2[3],vari2[4],vari2[5],vari2[6],vari2[7])
else:
    print("""Ingrese los siguientes datos:
    Patente
    Seguro
    Numero de poliza
    Fecha de vencimiento
    Equipamiento""")
    vari=[]
    for rodado in range(5):
        hdifej=input()
        vari.append(hdifej)
    aed=rodados(vari[0],vari[1],vari[2],vari[3],vari[4])

a.imprimir()
b.imprimir()
c.imprimir()
d.imprimir()
e.imprimir()
f.imprimir()
g.imprimir()
h.imprimir()
i.imprimir()
j.imprimir()
try:
    ae.imprimir()
except:
    pass
R1.imprimir()
R2.imprimir()
R3.imprimir()
try:
    aed.imprimir()
except:
    pass
hh=[]
X=True
while X==True:
    print("Ingrese DNI de bomberos para dotación: ")
    DNIdotacion = input()
    try:
        DNIdotacion=int(DNIdotacion)
        hh.append(DNIdotacion)
    except:
        X=False
        break

#for b in bomberoslista:
 #           for i in hh:
        #        if b.dni == i:
         #           break
          #      else:
           #         print("El bombero que llamó no está registrado")                                                      

for q in bomberoslista:
    if q.dni == DNIdotacion:
        break
    else:
        print("El bombero que ingresó no existe")
        break                               


    


