"""
EXERCÍCIO 3B - TESTES PARA CLASSIFICAR_VENTO USANDO A FUNÇÃO GENÉRICA

Classes de Equivalência (4 classes):
 velocidade < 20      → "calmo"
 20 ≤ velocidade < 40 → "moderado"
 40 ≤ velocidade < 60 → "forte"
 velocidade ≥ 60      → "tempestade"

Valores-Limite (3 fronteiras):
  Fronteira 1: limite = 20 (transição "calmo" → "moderado")
  Fronteira 2: limite = 40 (transição "moderado" → "forte")
  Fronteira 3: limite = 60 (transição "forte" → "tempestade")

Para cada fronteira testamos: ANTES, EXATO e DEPOIS
  ANTES:  19.9, 39.9, 59.9 (último valor da classe anterior)
  EXATO:  20.0, 40.0, 60.0 (limite exato, primeiro valor da nova classe)
  DEPOIS: 20.1, 40.1, 60.1 (primeiro valor claramente na nova classe)
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'funcional'))
from IndiceMassaCorporal import classificar_por_feixas


# Definir as faixas de vento para usar na função genérica
faixas_vento = [
    (20, "calmo"),
    (40, "moderado"),
    (60, "forte"),
    (float('inf'), "tempestade")
]

def test_classe_1_calmo():
    resultado = classificar_por_feixas(10, faixas_vento)
    assert resultado == "calmo"


def test_classe_2_moderado():
    resultado = classificar_por_feixas(30, faixas_vento)
    assert resultado == "moderado"


def test_classe_3_forte():
    resultado = classificar_por_feixas(50, faixas_vento)
    assert resultado == "forte"


def test_classe_4_tempestade():
    resultado = classificar_por_feixas(80, faixas_vento)
    assert resultado == "tempestade"

@pytest.mark.parametrize("velocidade,categoria_esperada", [
    # Fronteira 1: limite = 20
    (19.9, "calmo"),
    (20.0, "moderado"),
    (20.1, "moderado"),
    
    # Fronteira 2: limite = 40
    (39.9, "moderado"),
    (40.0, "forte"),
    (40.1, "forte"),
    
    # Fronteira 3: limite = 60
    (59.9, "forte"),
    (60.0, "tempestade"),
    (60.1, "tempestade"),
], ids=[
    "fronteira_20_antes",
    "fronteira_20_exato",
    "fronteira_20_depois",
    "fronteira_40_antes",
    "fronteira_40_exato",
    "fronteira_40_depois",
    "fronteira_60_antes",
    "fronteira_60_exato",
    "fronteira_60_depois",
])
def test_valores_limite_vento(velocidade, categoria_esperada):
    resultado = classificar_por_feixas(velocidade, faixas_vento)
    assert resultado == categoria_esperada
