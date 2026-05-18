def Semaforo(cor: str) -> str:
    if cor == "verde":
        return "Siga"
    elif cor == "amarelo":
        return "Atenção"
    elif cor == "vermelho":
        return "Pare"
    else:
        return "Cor inválida"