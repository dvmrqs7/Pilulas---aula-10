def calcular_bonus(salario_base: float, avaliacao:str) -> float:
    if salario_base < 0:
        return 0.0
    valores = {
                "Bom": 0.10,
                'Excelente': 0.20,
                'Regular': 0.02,
            }
    valores = valores.get(avaliacao,0.0)
    return salario_base * valores