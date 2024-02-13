import random
class CuentaBancaria:

    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self.saldo = saldo
        self.num_cuenta = f"ES {random.randint(1000000000,9999999999)}"
    
    def mostrar(self):
        return f"El saldo actual del numero de cuenta {self.num_cuenta}, perteneciente a {self.nombre} es: {self.saldo:.2f}€"
       
    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo = self.saldo + cantidad
            return self.saldo
    
    def retirar(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente")
        self.saldo = self.saldo - cantidad
        return self.saldo