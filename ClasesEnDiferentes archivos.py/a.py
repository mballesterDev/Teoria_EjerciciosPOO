

class Trabajador:
   
    empresa = "CartonajesUnión"
    sueldo = "básico"
    rango="bajo"
  
    def __init__(self,nombre,edad,anyosEmpresa,domicilo):
        self.nombre = nombre
        self.edad = edad
        self.anyosEmpresa = anyosEmpresa
        self.domicilio = domicilo
        
    def MostrarDatos(self):
       print(f"Tu nombre es {self.nombre}, tienes {self.edad} años, tienes {self.anyosEmpresa} años en la empresa, tu domicilio es {self.domicilio}")

    """Entnces en esta vlase tenemos los atributos creados = empresa sueldo y rango
    y los atributos que cremos con el cosntructor son = nombre, edad, anyosEmpresa y domicilio"""


trababajador001 = Trabajador("Marc", 25, 5, "Calle 1")


