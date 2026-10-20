import pytest
from estacinamento import calcular_tarifa


@pytest.mark.parametrize("minutos,valor_esperado,descricao", [
    # CE01: 0 ≤ minutos ≤ 15 (Grátis)
    (0, 0.0, "CE01_limite_inferior"),
    (7, 0.0, "CE01_representante"),
    (15, 0.0, "CE01_limite_superior"),
    
    # Fronteira: CE01 → CE02
    (16, 12.0, "Fronteira_CE01_CE02_inicio_CE02"),
    
    # CE02: 16 ≤ minutos ≤ 180 (R$ 12,00)
    (16, 12.0, "CE02_limite_inferior"),
    (90, 12.0, "CE02_representante"),
    (180, 12.0, "CE02_limite_superior"),
    
    # Fronteira: CE02 → CE03a
    (181, 15.0, "Fronteira_CE02_CE03a_inicio_CE03a"),
    
    # CE03a: 181 ≤ minutos ≤ 240 (1 hora adicional = R$ 15,00)
    (181, 15.0, "CE03a_limite_inferior"),
    (210, 15.0, "CE03a_representante"),
    (240, 15.0, "CE03a_limite_superior"),
    
    # Fronteira: CE03a → CE03b
    (241, 18.0, "Fronteira_CE03a_CE03b_inicio_CE03b"),
    
    # CE03b: 241 ≤ minutos ≤ 300 (2 horas adicionais = R$ 18,00)
    (241, 18.0, "CE03b_limite_inferior"),
    (270, 18.0, "CE03b_representante"),
    (300, 18.0, "CE03b_limite_superior"),
    
    # Fronteira: CE03b → CE03c
    (301, 21.0, "Fronteira_CE03b_CE03c_inicio_CE03c"),
    
    # CE03c: 301 ≤ minutos ≤ 360 (3 horas adicionais = R$ 21,00)
    (301, 21.0, "CE03c_limite_inferior"),
    (330, 21.0, "CE03c_representante"),
    (360, 21.0, "CE03c_limite_superior"),
    
    # Fronteira: CE03c → CE03d
    (361, 24.0, "Fronteira_CE03c_CE03d_inicio_CE03d"),
    
    # CE03d: 361 ≤ minutos ≤ 420 (4 horas adicionais = R$ 24,00)
    (361, 24.0, "CE03d_limite_inferior"),
    (390, 24.0, "CE03d_representante"),
    (420, 24.0, "CE03d_limite_superior"),
    
    # Fronteira: CE03d → CE03e
    (421, 27.0, "Fronteira_CE03d_CE03e_inicio_CE03e"),
    
    # CE03e: 421 ≤ minutos ≤ 480 (5 horas adicionais = R$ 27,00)
    (421, 27.0, "CE03e_limite_inferior"),
    (450, 27.0, "CE03e_representante"),
    (480, 27.0, "CE03e_limite_superior"),
    
    # Fronteira: CE03e → CE03f
    (481, 30.0, "Fronteira_CE03e_CE03f_inicio_CE03f"),
    
    # CE03f: 481 ≤ minutos ≤ 540 (6 horas adicionais = R$ 30,00)
    (481, 30.0, "CE03f_limite_inferior"),
    (510, 30.0, "CE03f_representante"),
    (540, 30.0, "CE03f_limite_superior"),
    
    # Fronteira: CE03f → CE03g
    (541, 33.0, "Fronteira_CE03f_CE03g_inicio_CE03g"),
    
    # CE03g: 541 ≤ minutos ≤ 600 (7 horas adicionais = R$ 33,00)
    (541, 33.0, "CE03g_limite_inferior"),
    (570, 33.0, "CE03g_representante"),
    (600, 33.0, "CE03g_limite_superior"),
    
    # Fronteira: CE03g → CE03h
    (601, 36.0, "Fronteira_CE03g_CE03h_inicio_CE03h"),
    
    # CE03h: 601 ≤ minutos ≤ 660 (8 horas adicionais = R$ 36,00)
    (601, 36.0, "CE03h_limite_inferior"),
    (630, 36.0, "CE03h_representante"),
    (660, 36.0, "CE03h_limite_superior"),
    
    # Fronteira: CE03h → CE03i
    (661, 39.0, "Fronteira_CE03h_CE03i_inicio_CE03i"),
    
    # CE03i: 661 ≤ minutos ≤ 720 (9 horas adicionais = R$ 39,00)
    (661, 39.0, "CE03i_limite_inferior"),
    (690, 39.0, "CE03i_representante"),
    (720, 39.0, "CE03i_limite_superior"),
    
    # Fronteira: CE03i → CE04
    (721, 60.0, "Fronteira_CE03i_CE04_inicio_CE04"),
    
    # CE04: minutos > 720 (Diária = R$ 60,00)
    (721, 60.0, "CE04_limite_inferior"),
    (1440, 60.0, "CE04_representante"),
    (10000, 60.0, "CE04_valor_muito_alto"),
], ids=lambda x: x[2])
def test_entradas_validas(minutos, valor_esperado, descricao):
    assert calcular_tarifa(minutos) == valor_esperado


def test_tempo_negativo_um():
    with pytest.raises(ValueError, match="O tempo não pode ser negativo"):
        calcular_tarifa(-1)


def test_tempo_negativo_grande():
    with pytest.raises(ValueError, match="O tempo não pode ser negativo"):
        calcular_tarifa(-1000)


def test_tempo_float():
    with pytest.raises(TypeError, match="O tempo deve ser um valor inteiro"):
        calcular_tarifa(10.5)


def test_tempo_float_zero():
    with pytest.raises(TypeError, match="O tempo deve ser um valor inteiro"):
        calcular_tarifa(0.1)


def test_tempo_string():
    with pytest.raises(TypeError, match="O tempo deve ser um valor inteiro"):
        calcular_tarifa("10")


def test_tempo_none():
    with pytest.raises(TypeError, match="O tempo deve ser um valor inteiro"):
        calcular_tarifa(None)


def test_tempo_booleano():
    with pytest.raises(TypeError, match="O tempo deve ser um valor inteiro"):
        calcular_tarifa(True)


def test_tempo_lista():
    with pytest.raises(TypeError, match="O tempo deve ser um valor inteiro"):
        calcular_tarifa([10])

