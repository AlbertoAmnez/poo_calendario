class RelojDigital:
    def __init__(self, horas=0, minutos=0, segundos=0):
        self.horas = horas
        self.minutos = minutos
        self.segundos= segundos

    def tranforma_horas(self):
        
        self.horas = self.horas % 24

    def tranforma_minutos(self):

    
    def tranforma_segundos(self):
            


    def info(self):
        
        return f"El reloj marca {self.horas:02d}:{self.minutos:02d}:{self.segundos:02d}"

    
consulta = RelojDigital(28)
print(consulta.info())
