class CuentaBancaria:

    def __init__(self, nombre, saldo, num_cuenta):
        self.nombre = nombre
        self.saldo = saldo
        self.num_cuenta = num_cuenta
    
    def mostrar(self):
        return f"El saldo actual de la cuenta nº {self.num_cuenta}, perteneciente a {self.nombre} es de = {self.saldo} euros"
       
    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo = self.saldo + cantidad
            return self.saldo
    
    def retirar(self, cantidad):
        if self.saldo >= cantidad:
            self.saldo = self.saldo - cantidad
            return self.saldo
    