'''
1.- Crear una cuenta. El programa pide Nombre e Ingreso inicial

2.- Presenta un mensaje que dice "Tipo de movimiento (I-Ingreso, R-Retirada *-Fin)

    - Si el tipo movimiento es I
        - Pedir cantidad
        - Validar que la cantidad sea un numero y positiva
        - Realizar el ingreso
        - Si la cantidad no es un numero o no es positiva, volver a pedirla

    - Si el tipo de movimiento es R
        - Pedir cantidad
        - Validar que la cantidad sea un numero y positiva
        - Si el numero es correcto, realizar la retirada
            - Si la retirada devuelve saldo insuficiente, avisar y volver al punto 2
            - Si la retirada va bien volver al punto 2
        - Si la cantidad no es un numero o no es positiva, volver a pedirla

    - Si el tipo es *
        - Imprimir el saldo de la cuenta
        - Fin del programa

    - Si el tipo no es ninguno de los anteriores volver a 2
'''

from entities import CuentaBancaria
from controls import inputEnteroPositivo

'''
Entrada nombre

'''

nombre = input("Nombre: ")
while len(nombre) < 3:
    print("El nombre debe tener al menos 3 caracteres.")
    nombre = input("Nombre: ")

'''
Entrada saldo inicial

'''

saldo = inputEnteroPositivo("Cantidad a ingresar:", 50)



la_cuenta = CuentaBancaria(nombre, saldo)

print(la_cuenta.mostrar())

accion = input("Tipo de movimiento (I->Ingreso, R->Retirada *->Fin)")

while accion != "*":
    

    if accion.upper() == "I":
        saldo = inputEnteroPositivo("Introduce cantidad a ingresar:")
        print(f"Nuevo saldo de la cuenta: {la_cuenta.depositar(saldo):.2f}€")
    elif accion.upper() == "R":
        try:
            saldo = inputEnteroPositivo("Introduce cantidad a retirar:")
            nuevo_saldo = la_cuenta.retirar(saldo)
            print(f"Nuevo saldo de la cuenta: {nuevo_saldo:.2f}€")
        except ValueError:
            print("Saldo insuficiente, vuelve a intentarlo")

    else:
        print("Opcion incorrecta")

    accion = input("Tipo de movimiento (I->Ingreso, R->Retirada *->Fin)")

print(f"El saldo final de la cuenta {la_cuenta.num_cuenta} es:  {la_cuenta.saldo}€")