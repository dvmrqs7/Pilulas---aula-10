def aplicar_cupom(codigo_cupom: str, valor_compra: float) -> float:
    cupons_validos = {
        'CUPOM10': 0.10,
        'CUPOM25': 0.25,
        'DESCONTOVIP': 0.35
    }
    codigo_cupom = codigo_cupom.upper()
    if codigo_cupom in cupons_validos:
        if codigo_cupom == 'CUPOM25' and valor_compra >= 100.0:
            return valor_compra * cupons_validos[codigo_cupom]
        elif codigo_cupom == 'DESCONTOVIP' and valor_compra >= 500.0:
            return valor_compra * cupons_validos[codigo_cupom]
        elif codigo_cupom == 'CUPOM10':
            return valor_compra * cupons_validos[codigo_cupom]
    return 0.0       