#ex 1a

def calcular_tarifa(minutos):
    if not isinstance(minutos, int) or isinstance(minutos, bool):
        raise TypeError("O tempo deve ser um valor inteiro")
    
    if minutos < 0:
        raise ValueError("O tempo não pode ser negativo")
    
    if minutos <= 15:
        return 0.0
    elif minutos <= 180:
        return 12.0
    elif minutos <= 720:
        horas_adicionais = math.ceil((minutos - 180) / 60)
        return 12.0 + horas_adicionais * 3.0
    else:
        return 60.0