import plan2

class plan3(plan2.Plan2):
    
    def __init__(self, nombrePlan, accesoIlimitado, profesoresPresenciales, horasContenido, seguimineto,contactoProfes, tutor):
        self.contactoProfes = contactoProfes
        self.tutor = tutor
        
        super().__init__(nombrePlan, accesoIlimitado, profesoresPresenciales, horasContenido, seguimineto)

    def informacion(self):
        super().informacion()
        print()
        print(f"Además gracias al plan premium dispondras de: \nChat con profes = {self.contactoProfes} \nTutor personal = {self.tutor}")


planPremium = plan3("PLAN PREMIUM",True,True, 500, "Permanente", True, True)