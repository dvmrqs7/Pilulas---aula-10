from semaforo import Semaforo

def test_verde():
    assert Semaforo("verde") == "Siga"

def test_amarelo():
    assert Semaforo("amarelo") == "Atenção"

def test_vermelho():
    assert Semaforo("vermelho") == "Pare"

def test_cor_invalida():
    assert Semaforo("azul") == "Cor inválida"