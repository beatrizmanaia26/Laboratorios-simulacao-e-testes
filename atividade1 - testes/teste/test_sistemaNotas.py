import pytest
import sys
sys.path.insert(0, '../funcional')

from sistemaNotas import validar_nota, calcular_media, obter_situacao


#exercício1
'''
Escreva pelo menos 5 testes seguindo as convenções do
pytest (test_*.py, def test_*()), cobrindo os limites
exatos (nota 0, nota 10) e casos fora do intervalo.'''

'''
def test_validar_nota_extremo_inferior():
    assert validar_nota(0) == True


def test_validar_nota_extremo_superior():
    assert validar_nota(10) == True


def test_validar_nota_fora_negativo():
    assert validar_nota(-1) == False


def test_validar_nota_fora_maior():
    assert validar_nota(11) == False


def test_validar_nota_string():
    assert validar_nota('a') == False
'''

@pytest.mark.parametrize("nota,esperado", [
    (0, True),      
    (10, True),    
    (-1, False),  
    (11, False),   
    ('a', False),   
])
def test_validar_nota_parametrizado(nota, esperado):
    assert validar_nota(nota) == esperado

#exercício2

'''
Implemente as funções:
validar_nota(nota): retorna True se a nota está
entre 0 e 10 (inclusive)
calcular_media(notas): retorna a média de uma
lista de notas
Escreva pelo menos 5 testes seguindo as convenções do
pytest (test_*.py, def test_*()), cobrindo os limites
exatos (nota 0, nota 10) e casos fora do intervalo.'''

def test_calcular_media():
    with pytest.raises(
        ValueError, match="lista de notas vazia"
    ):
        calcular_media([])  

#exercício3

'''
def test_media_turma_a():
    notas = [6,7,8]
    assert calcular_media(notas) == 7

def test_media_turma_b():
    notas = [6,7,8]
    assert obter_situacao(calcular_media(notas)) == "Aprovado"
'''

'''Os dois testes acima repetem a mesma lista de notas. Crie
uma fixture em conftest.py chamada notas_exemplo e
refatore os dois testes para usá-la.'''

def test_media_turma_a(notas_exemplo):
    assert calcular_media(notas_exemplo) == 7

def test_media_turma_b(notas_exemplo):
    assert obter_situacao(calcular_media(notas_exemplo)) == "Aprovado"

#exercício 4

'''
a) Escreva um teste parametrizado de obter_situacao
cobrindo pelo menos 5 médias diferentes, incluindo
exatamente 7 e exatamente 5.
b) Um dos casos vai falhar. Identifique por quê e corrija a
função (a especificação é média maior ou igual a 7 para
Aprovado, e maior ou igual a 5 para Recuperação).'''

@pytest.mark.parametrize("media,esperado", [
    (9, "Aprovado"),      
    (7, "Aprovado"),    
    (6, "Recuperacao"),   
    (5, "Recuperacao"),     
    (2, "Reprovado"),      
])
def test_validar_obter_situacao_parametrizado(media, esperado):
    assert obter_situacao(media) == esperado

#exercicio5
'''
turma = []
def test_matricula_aluno():
    turma.append("Ana")
    assert len(turma) == 1

def test_matricula_outro_aluno():
    turma.append("Bruno")
    assert len(turma) == 2
'''
'''
Qual boa prática da checklist esse par de testes viola?
Reescreva os dois testes para que cada um rode de forma
independente, em qualquer ordem.  '''

'''RESPOSTA: Esse par de tste viola a boa prática de Testes independentes: cada um roda sozinho, em
qualquer ordem, pois ao utilizar a variavel global nao da para ambos estarem certos ao mesmo tempo'''

# SOLUÇÃO: Reescrever com Fixture
@pytest.fixture
def turma():
    return []

def test_matricula_aluno(turma):
    turma.append("Ana")
    assert len(turma) == 1

def test_matricula_outro_aluno(turma):
    turma.append("Bruno")
    assert len(turma) == 1 