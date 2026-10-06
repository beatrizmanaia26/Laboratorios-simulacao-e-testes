import pytest

def calcular_tarifa(minutos):
    if not isinstance(minutos, int):
        raise TypeError("minutos deve ser inteiro")
    if minutos <= 0:
        raise ValueError("minutos nao pode ser negativo")
    if minutos < 15:
        return 0.00
    if minutos <= 180:
        return 12.00
    if minutos < 720:
        return 12.00 + 3.00 * ((minutos - 180) // 60)
    return 60.00


@pytest.mark.parametrize("minutos,valor_esperado", [
    (0, 0.0), (7, 0.0), (15, 0.0),
    (16, 12.0),
    (16, 12.0), (90, 12.0), (180, 12.0),
    (181, 15.0),
    (181, 15.0), (210, 15.0), (240, 15.0),
    (241, 18.0),
    (241, 18.0), (270, 18.0), (300, 18.0),
    (301, 21.0),
    (301, 21.0), (330, 21.0), (360, 21.0),
    (361, 24.0),
    (361, 24.0), (390, 24.0), (420, 24.0),
    (421, 27.0),
    (421, 27.0), (450, 27.0), (480, 27.0),
    (481, 30.0),
    (481, 30.0), (510, 30.0), (540, 30.0),
    (541, 33.0),
    (541, 33.0), (570, 33.0), (600, 33.0),
    (601, 36.0),
    (601, 36.0), (630, 36.0), (660, 36.0),
    (661, 39.0),
    (661, 39.0), (690, 39.0), (720, 39.0),
    (721, 60.0),
    (721, 60.0), (1440, 60.0), (10000, 60.0),
])
def test_entradas_validas(minutos, valor_esperado):
    assert calcular_tarifa(minutos) == valor_esperado


def test_tempo_negativo():
    with pytest.raises(ValueError):
        calcular_tarifa(-1)




'''teste estagiario minimo'''
def calcular_tarifa(minutos):
    if not isinstance(minutos, int):
        raise TypeError("minutos deve ser inteiro")
    if minutos <= 0:
        raise ValueError("minutos nao pode ser negativo")
    if minutos < 15:
        return 0.00
    if minutos <= 180:
        return 12.00
    if minutos < 720:
        return 12.00 + 3.00 * ((minutos - 180) // 60)
    return 60.00


# SUÍTE COM APENAS 1 REPRESENTANTE POR CLASSE VÁLIDA
@pytest.mark.parametrize("minutos,valor_esperado", [
    (8, 0.0),       # CE01: 0 a 15 minutos
    (100, 12.0),    # CE02: 16 a 180 minutos
    (300, 18.0),    # CE03: 181 a 720 minutos (representante no meio)
    (1000, 60.0),   # CE04: acima de 720 minutos
])
def test_apenas_representantes(minutos, valor_esperado):
    assert calcular_tarifa(minutos) == valor_esperado
