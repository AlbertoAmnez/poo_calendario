class LibroException(Exception):
    pass

class Libro:
    def __init__(self, titulo, autor, paginas, prestado ):
        self.libro = titulo
        self.autor = autor
        self.num_pagina= paginas
        self.prestado = prestado

    def info(self):
        
        res = f"El libro {self.libro} de {self.autor} de {self.num_pagina} paginas "
        if self.prestado:
            return res + "está prestado"
        else:
            return res + "esta disponible"
        
        '''
        Otra opcion de hacerlo con un ternario:
        return f"El libro {self.libro} de {self.autor} de {self.num_pagina} paginas. Está {'prestado' if self.prestado else 'dispobible'}."
        '''

    def prestar(self):

        if self.prestado == True:
            raise LibroException("el libro ya está prestado")
        self.prestado = True
        
    def devolver(self):

        if self.prestado == False:
            return "No se puede devolver, está disponible"
        self.prestado = False
pedido = Libro ("La sombra del Viento", "Ruiz Zafon",  450, True)
print(pedido.info())

class Habitacion:
    def __init__(self, tipo, numero, ocupada):
        self.tipo = tipo
        self.numero = numero
        self.ocupada = ocupada

    def info(self):
        res = f"La habitacion {self.tipo}, numero {self.numero} "
        if self.ocupada == True:
            return res + "está ocupada"
        else:
            return res + "esta disponible"
        

    def reservar(self):
        if self.ocupada == False:
            self.ocupada = True
        else:
            return "la habtacion ya está ocupada"

    def cancelar_reserva(self):
        if self.ocupada == True:
            self.ocupada = False
        else:
            return 'cancelar reserva'
        
    
reserva = Habitacion ("con piscina", 150, False)
print(reserva.info())

reserva.reservar()
print(reserva.info())

reserva.cancelar_reserva()
print(reserva.info())
