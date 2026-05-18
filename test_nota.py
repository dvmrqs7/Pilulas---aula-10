from nota import converter_nota_para_conceito

def test_conceito_a():
    for nota in [9.0, 10.0]:
        assert converter_nota_para_conceito(nota) == 'A'
def test_conceito_b():
    for nota in [7.0, 8.9]:
        assert converter_nota_para_conceito(nota) == 'B'
def test_conceito_c():
    for nota in [5.0, 6.9]:
        assert converter_nota_para_conceito(nota) == 'C'
def test_conceito_d():
    for nota in [3.0, 4.9]:
        assert converter_nota_para_conceito(nota) == 'D'
def test_conceito_f():
    for nota in [0, 2.9]:
        assert converter_nota_para_conceito(nota) == 'F'

def test_nota_negativa():
    for nota in [-10.0, -0.1]:
        assert converter_nota_para_conceito(nota) == 'Nota inválida'

def test_nota_acima():
    for nota in [10.1, 20.0]:
        assert converter_nota_para_conceito(nota) == 'Nota inválida'
