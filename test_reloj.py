from reloj import RelojDigital

def test_crear_reloj_digital():

    # Preparo el test con condiciones iniciales
    reloj = RelojDigital()

    # Comprueblo el resultado esperado
    assert reloj.horas == 0
    assert reloj.minutos == 0
    assert reloj.segundos == 0
    assert reloj.info == "00:00:00"

def test_crea_reloj_con_hora_buena():

     # Preparo el test con condiciones iniciales
    reloj = RelojDigital(22,45,3)

    # Comprueblo el resultado esperado
    assert reloj.horas == 22
    assert reloj.minutos == 45
    assert reloj.segundos == 3
    assert reloj.info == "22:45:03"

def test_crea_reloj_con_horas_de_mas():

     # Preparo el test con condiciones iniciales
    reloj = RelojDigital(25,5,3)

    # Comprueblo el resultado esperado
    assert reloj.horas == 1
    assert reloj.minutos == 45
    assert reloj.segundos == 3
    assert reloj.info == "01:45:03"