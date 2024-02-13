class Dia:
    def __init__(self, anyo=1970, mes=1, dia=1):
        self.anyo = anyo
        self.mes = mes
        self.dia = dia
        self.dia_semana = self.calcular_dia_semana()

        
        self.validar_fecha()

    def validar_fecha(self):
        if self.mes < 1 or self.mes > 12:
            raise ValueError("El mes tiene que estar entre 1 y 12")
        
        if self.dia < 1 or self.dia > 31:
            raise ValueError("El día tiene estar entre 1 y 31")
        '''
        Inicializamos la lista dias_por_mes con '0' para que coincidan los indices de la lista con los numeros de mes, ya que el indice empieza en 0 pero el mes empieza en 1.
        Asi, lo hago mas intuitivo haciendo coincidir el indice con el numero del mes.
        '''
        dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.anyo % 4 == 0 and (self.anyo % 100 != 0 or self.anyo % 400 == 0):
            dias_por_mes[2] = 29  
        
        if self.dia < 1 or self.dia > dias_por_mes[self.mes]:
            raise ValueError(f"El mes {self.mes} del año {self.anyo} no tiene {self.dia} dias")