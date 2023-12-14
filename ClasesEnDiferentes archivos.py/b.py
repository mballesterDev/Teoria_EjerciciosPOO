
import a
class TrabajadorAR(a.Trabajador):
    sueldo = "Premium"
    rango = "Alto"
    
    def __init__(self, nombre, edad, anyosEmpresa, domicilo, permisos, empleados): #hay que reeimportar los init anteriores
        self.permisos = permisos
        self.empleados = empleados
        
        super().__init__(nombre, edad, anyosEmpresa, domicilo) # con super se reeimporta

    def MostrarDatos(self): #con el super tambien podemos completar funciones
        super().MostrarDatos()
        print()
        print (f"Adenás tienes {self.permisos} permisos y tienes a {self.empleados} trabajando para ti")
        print()


trabajador002 = TrabajadorAR("Manel", 23, 2, "Sagunto", "10|10", "10")  



