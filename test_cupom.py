from cupom import aplicar_cupom

def test_aplicar_cupom10():
    assert aplicar_cupom('CUPOM10', 100.0) == 10.0

def test_aplicar_cupom25_valido():
    assert aplicar_cupom('CUPOM25', 100.0) == 25.0

def test_aplicar_cupom25_invalido():
    for valor in [1,99.99]:
        assert aplicar_cupom('CUPOM25', valor) == 0.0

def test_aplicar_cupom35_descontovip():
    assert aplicar_cupom('DESCONTOVIP', 500.0) == 175.0

def test_aplicar_cupom35_descontovip_invalido():
    for valor in [1, 499.99]:
        assert aplicar_cupom('DESCONTOVIP', valor) == 0.0

def test_letra_minuscula():
    assert aplicar_cupom('cupom10', 100.0) == 10.0

def test_letra_maiuscula():
    assert aplicar_cupom('CUPOM10', 100.0) == 10.0
        