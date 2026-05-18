def calcular_frete(peso: float) -> float:
    if peso == 0.0:
        return 0.0
    elif peso <= 1.0:
        return 5.0
    elif peso <= 5.0:
        return 10.0
    else:
        return 18.0
