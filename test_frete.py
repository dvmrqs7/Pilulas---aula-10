from frete import calcular_frete

def test_calcular_frete_peso_ate_1kg():
    for peso in [0.1, 1]:
        assert calcular_frete(peso) == 5.00

def test_calcular_frete_peso_entre_1kg_e_5kg():
    for peso in [1.01, 5]:
        assert calcular_frete(peso) == 10.00

def test_calcular_frete_peso_acima_5kg():
    for peso in [5.01, 10]:
        assert calcular_frete(peso) == 18.00

def test_calcular_frete_peso_negativo():
    for peso in [-10.0, 0.0]:
        assert calcular_frete(peso) == 0.00
