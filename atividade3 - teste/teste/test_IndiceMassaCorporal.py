import pytest
import sys
import os

# Adiciona o diretório funcional ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'funcional'))

from IndiceMassaCorporal import calcular_imc, categorizar_imc, classificar_pessoa, tem_frete_gratis, classificar_vento

# EX1: Escreva ao menos 4 testes, um representante de cada classe válida (Implemente calcular_imc(peso, altura), categorizar_imc(imc) eclassificar_pessoa(peso, altura).)

def test_calcular_imc():
    peso = 50.0      
    altura =  1.70
    resultado = calcular_imc(peso,altura)
    assert round(resultado, 2) == 17.30  

def test_categorizar_imc():
    imc = 26
    resultado = categorizar_imc(imc)
    assert resultado == "sobrepeso"


'''OPCAO 1: sem parametrize'''

def test_classificar_pessoa_abaixo_do_peso():
   # (IMC < 18.5)
    resultado = classificar_pessoa(50, 1.70)
    assert resultado['categoria'] == "abaixo do peso"
    assert resultado['imc'] > 0


def test_classificar_pessoa_peso_normal():
    # (18.5 ≤ IMC < 25)
    resultado = classificar_pessoa(70, 1.70)
    assert resultado['categoria'] == "peso normal"
    assert resultado['imc'] > 0


def test_classificar_pessoa_sobrepeso():
    #(25 ≤ IMC < 30)
    resultado = classificar_pessoa(85, 1.80)
    assert resultado['categoria'] == "sobrepeso"
    assert resultado['imc'] > 0


def test_classificar_pessoa_obesidade():
    # (IMC ≥ 30)
    resultado = classificar_pessoa(120, 1.70)
    assert resultado['categoria'] == "obesidade"
    assert resultado['imc'] > 0


'''OPÇÃO 2: usando @pytest.mark.parametrize'''

@pytest.mark.parametrize("peso,altura,categoria_esperada", [
    (50, 1.70, "abaixo do peso"),    # IMC < 18.5
    (70, 1.70, "peso normal"),       # 18.5 ≤ IMC < 25
    (85, 1.80, "sobrepeso"),         # 25 ≤ IMC < 30
    (120, 1.70, "obesidade"),        # IMC ≥ 30
])
def test_classificar_pessoa_parametrizado(peso, altura, categoria_esperada):

    resultado = classificar_pessoa(peso, altura)
    assert resultado['categoria'] == categoria_esperada
    assert resultado['imc'] > 0
    assert isinstance(resultado, dict)
    assert 'imc' in resultado
    assert 'categoria' in resultado

# EX2: Escreva um teste parametrizado de categorizar_imc cobrindo os valores-limite das três fronteiras, com ids descritivos (fronteiras adjacentes podem compartilhar pontos de teste, então menos de 9 casos distintos já cobrem as seis posições limite)


@pytest.mark.parametrize("imc,categoria_esperada", [
    # Fronteira 1: 18.5
    (18.49, "abaixo do peso"),      
    (18.5, "peso normal"),     
    (18.51, "peso normal"),       
    
    # Fronteira 2: 25
    (24.99, "peso normal"),        
    (25.0, "sobrepeso"),     
    (25.1, "sobrepeso"),     
    
    # Fronteira 3: 30
    (29.99, "sobrepeso"),           
    (30.0, "obesidade"),   
    (30.1, "obesidade"),   
         
], ids=[
    "fronteira_18_5_antes",
    "fronteira_18_5_exato",
    "fronteira_18_5_depois",
    "fronteira_25_antes",
    "fronteira_25_exato",
    "fronteira_25_depois",
    "fronteira_30_antes",
    "fronteira_30_exato",
    "fronteira_30_depois",
])
def test_categorizar_imc_valores_limite(imc, categoria_esperada):
    resultado = categorizar_imc(imc)
    assert resultado == categoria_esperada


# EX2: O calcular_imc do Exercício 1 ainda aceita peso ou altura não positivos sem reclamar: adicione a validação (levantar ValueError nesse caso) e escreva dois testes que confirmem o novo comportamento

def test_calcular_imc_peso_invalido_zero():
    with pytest.raises(ValueError, match="Peso e altura devem ser maiores que zero"):
        calcular_imc(0, 1.70)


def test_calcular_imc_altura_invalida_zero():
    with pytest.raises(ValueError, match="Peso e altura devem ser maiores que zero"):
        calcular_imc(70, 0)


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

def test_classe_1_calmo():
    assert classificar_vento(10) == "calmo"


def test_classe_2_moderado():
    assert classificar_vento(30)  == "moderado"


def test_classe_3_forte():
    assert classificar_vento(50)  == "forte"


def test_classe_4_tempestade():
    assert classificar_vento(80)  == "tempestade"

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
    assert classificar_vento(velocidade) == categoria_esperada


# EX4a: Teste parametrizado para cobertura completa da tabela de decisão (8 regras)
'''
TABELA DE DECISÃO - FRETE GRÁTIS

CONDIÇÃO               |R1 R2 R3 R4 R5 R6 R7 R8
COMPRA >=200           |S  S. S. S. N. N. N. N  
ASSINATURA PREMIUM     |S  S. N. N. S. S. N. N
PESO PEDIDO <=30KG     |S. N. S. N. S. N  S  N
LIBERA FRETE (True)    |X              
NAO LIBERA FRETE (False)|.  X. X. X  X. X. X. X

Interpretação:
- R1: Compra >= 200 AND Premium AND Peso <= 30 → LIBERA (True)
- R2: Compra >= 200 AND Premium AND Peso > 30 → NÃO LIBERA (False)
- R3: Compra >= 200 AND NÃO Premium AND Peso <= 30 → NÃO LIBERA (False)
- R4: Compra >= 200 AND NÃO Premium AND Peso > 30 → NÃO LIBERA (False)
- R5: Compra < 200 AND Premium AND Peso <= 30 → NÃO LIBERA (False)
- R6: Compra < 200 AND Premium AND Peso > 30 → NÃO LIBERA (False)
- R7: Compra < 200 AND NÃO Premium AND Peso <= 30 → NÃO LIBERA (False)
- R8: Compra < 200 AND NÃO Premium AND Peso > 30 → NÃO LIBERA (False)
'''

@pytest.mark.parametrize("valor_compra,cliente_premium,peso,esperado", [
    (200, True, 30, True),
    (210, True, 31, False),
    (200, False, 30, False),
    (210, False, 31, False),
    (199, True, 29, False),
    (199, True, 31, False),
    (199, False, 29, False),
    (199, False, 31, False),
    
], ids=[
    "R1-CompraOK_PremiumSim_PesoOK",
    "R2-CompraOK_PremiumSim_PesoAlto",
    "R3-CompraOK_PremiumNao_PesoOK",
    "R4-CompraOK_PremiumNao_PesoAlto",
    "R5-CompraBaixa_PremiumSim_PesoOK",
    "R6-CompraBaixa_PremiumSim_PesoAlto",
    "R7-CompraBaixa_PremiumNao_PesoOK",
    "R8-CompraBaixa_PremiumNao_PesoAlto",
])
def test_frete_gratis_tabela_decisao(valor_compra, cliente_premium, peso, esperado):
    resultado = tem_frete_gratis(valor_compra, cliente_premium, peso)
    assert resultado == esperado

#ex4 considerando tabela reduzida
@pytest.mark.parametrize("valor_compra,cliente_premium,peso,esperado", [
    (200, True, 30, True),
    (210, True, 31, False),
    (200, False, 30, False),
    (210, False, 31, False),
    
], ids=[
    "R1-CompraOK_PremiumSim_PesoOK",
    "R2-CompraOK_PremiumSim_PesoAlto",
    "R3.1-CompraOK_PremiumNao_PesoOK",
    "R4.1-CompraOK_PremiumNao_PesoAlto",
])
def test_frete_gratis_tabela_decisao_reduzida(valor_compra, cliente_premium, peso, esperado):
    resultado = tem_frete_gratis(valor_compra, cliente_premium, peso)
    assert resultado == esperado

