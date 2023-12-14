class Plan1:
    accesoContenidos =True
    accesoOnline = True

    def __init__(self,nombrePlan, accesoIlimitado,profesoresPresenciales, horasContenido, seguimineto):
        self.nombrePlan = nombrePlan
        self.accesoIlimitado = accesoIlimitado
        self.profesoresPresenciales = profesoresPresenciales
        self.horasContenido = horasContenido
        self.seguimineto = seguimineto
        

    def informacion(self):
        print(f"{self.nombrePlan}")
        print(f"Este plan contiene acceso Ilimitado = {self.accesoIlimitado} \nprofesores Presenciales = {self.profesoresPresenciales} \nhoras Contenido = {self.horasContenido} \nseguimineto = {self.seguimineto}")
        print()    


planBasic = Plan1("PLAN BÁSICO",True,False, 100, "Básico" ) 
  