def inputEnteroPositivo(mensaje, valor_minimo=1):
    saldo = input(mensaje)
    while not saldo.isnumeric() or int(saldo) < valor_minimo:
        if not saldo.isnumeric():
            print("Introduce un valor numerico")
        else:
            print(f"Ingreso minimo es {valor_minimo}€.")

        saldo = input(mensaje)

    return int(saldo)