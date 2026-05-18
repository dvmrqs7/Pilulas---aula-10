from bonus import calcular_bonus

def test_cenario_bom():
    assert calcular_bonus(2000, "Bom") == 200.0

def test_cenario_excelente():
    assert calcular_bonus(2000, 'Excelente') == 400.0

def test_cenario_regular():
    assert calcular_bonus(2000, 'Regular') == 40.0

def test_cenario_ruim():
    assert calcular_bonus(2000, 'Ruim') == 0.0
    
def test_cenario_salario_negativo():
    for salario in [-2000,-10]:
        assert calcular_bonus(salario, 'Excelente') == 0.0

def test_cenario_invalido():
    assert calcular_bonus(2000, 'mais ou menos') == 0.0
    