from dia import Dia
def test_fecha_valida():
    
    d = Dia(2024, 2, 13)
    assert d.anyo == 2024
    assert d.mes == 2
    assert d.dia == 13

def test_fecha_invalida_dia():

    '''
    Comprobamos si el dia es invalido con ValueError, 
    si no es valido envia mensaje de error"
    '''

    try:
        d = Dia(2023, 2, 29)
        assert False, "Excepción ValueError"
    except ValueError as e:
        assert str(e) == "El mes 2 del año 2023 no tiene 29 días"

def test_fecha_invalida_mes():

    '''
    Comprobamos si el mes es invalido con ValueError, 
    si no es valido envia mensaje de error"
    '''

    try:
        d = Dia(2023, 13, 1)
        assert False, "Excepción ValueError"
    except ValueError as e:
        assert str(e) == "El mes debe estar entre 1 y 12"

def test_calculo_dia_semana():
    '''
    Calcular el dia de la semana
    0 = sábado, 1 = domingo, 2 = lunes, 3 = martes, 4 = miercoles, 5 = jueves, 6 = viernes
    '''
    d = Dia(2024, 2, 13)
    assert d.dia_semana == 4  

# Ejecutar pruebas
test_fecha_valida()
test_fecha_invalida_dia()
test_fecha_invalida_mes()
test_calculo_dia_semana()

print("Todas las pruebas pasaron exitosamente.")

