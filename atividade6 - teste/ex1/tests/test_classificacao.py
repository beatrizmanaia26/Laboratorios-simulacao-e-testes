from classificacao import classificar_aluno


def test_aluno_aprovado():
    assert classificar_aluno(8.0, 80) == "Aprovado"


def test_aluno_reprovado():
    assert classificar_aluno(3.0, 90) == "Reprovado"

'''a) Meça a cobertura de ramos e rode o mutmut.
 Quantos mutantes foram gerados, mortos e vivos?

1-cd "/Users/beatrizmanaia/Desktop/FEI 8S/Laboratorios-simulacao-e-testes/atividade6 - teste/ex1"

2-python3 -m pytest -v --cov=src --cov-branch --cov-report=term-missing

resp:

tests/test_classificacao.py::test_aluno_aprovado PASSED [ 50%]
tests/test_classificacao.py::test_aluno_reprovado PASSED [100%]

=============== tests coverage ================
_ coverage: platform darwin, python 3.14.6-final-0 _

Name                   Stmts   Miss Branch BrPart  Cover   Missing
------------------------------------------------------------------
src/classificacao.py      12      4     10      4    64%   3, 5, 7, 11
------------------------------------------------------------------
TOTAL                     12      4     10      4    64%
============== 2 passed in 0.03s ==============

3-
   rm -rf mutants
   python3 -m mutmut run


resp:============= test session starts =============
platform darwin -- Python 3.14.6, pytest-9.1.1, pluggy-1.6.0 -- /Library/Frameworks/Python.framework/Versions/3.14/bin/python3
cachedir: .pytest_cache
rootdir: /Users/beatrizmanaia/Desktop/FEI 8S/Laboratorios-simulacao-e-testes/atividade6 - teste/ex1
configfile: pyproject.toml
testpaths: tests
plugins: cov-7.1.0, platformdirs-4.13.5
collected 2 items                             

tests/test_classificacao.py::test_aluno_aprovado PASSED [ 50%]
tests/test_classificacao.py::test_aluno_reprovado PASSED [100%]

=============== tests coverage ================
_ coverage: platform darwin, python 3.14.6-final-0 _

Name                   Stmts   Miss Branch BrPart  Cover   Missing
------------------------------------------------------------------
src/classificacao.py      12      4     10      4    64%   3, 5, 7, 11
------------------------------------------------------------------
TOTAL                     12      4     10      4    64%
============== 2 passed in 0.03s ==============
beatrizmanaia@MacBook-Pro-de-Beatriz ex1 %  rm -rf mutants
beatrizmanaia@MacBook-Pro-de-Beatriz ex1 %  python3 -m mutmut run
⠼ Generating mutants
    done in 62ms (1 files mutated, 0 ignored, 0 unmodified)
⠏ Running stats     
    done
⠦ Running clean tests
    done
⠹ Running forced fail test
    done
Running mutation testing
⠏ 36/36  🎉 6 🫥 0  ⏰ 0  🤔 0  🙁 30  🔇 0  🧙 0
275.09 mutations/second


4-python3 -m mutmut results

resp:
beatrizmanaia@MacBook-Pro-de-Beatriz ex1 % python3 -m mutmut results
    classificacao.x_classificar_aluno__mutmut_1: survived
    classificacao.x_classificar_aluno__mutmut_2: survived
    classificacao.x_classificar_aluno__mutmut_3: survived
    classificacao.x_classificar_aluno__mutmut_4: survived
    classificacao.x_classificar_aluno__mutmut_5: survived
    classificacao.x_classificar_aluno__mutmut_6: survived
    classificacao.x_classificar_aluno__mutmut_7: survived
    classificacao.x_classificar_aluno__mutmut_8: survived
    classificacao.x_classificar_aluno__mutmut_9: survived
    classificacao.x_classificar_aluno__mutmut_10: survived
    classificacao.x_classificar_aluno__mutmut_11: survived
    classificacao.x_classificar_aluno__mutmut_12: survived
    classificacao.x_classificar_aluno__mutmut_13: survived
    classificacao.x_classificar_aluno__mutmut_14: survived
    classificacao.x_classificar_aluno__mutmut_15: survived
    classificacao.x_classificar_aluno__mutmut_16: survived
    classificacao.x_classificar_aluno__mutmut_17: survived
    classificacao.x_classificar_aluno__mutmut_18: survived
    classificacao.x_classificar_aluno__mutmut_19: survived
    classificacao.x_classificar_aluno__mutmut_20: survived
    classificacao.x_classificar_aluno__mutmut_21: survived
    classificacao.x_classificar_aluno__mutmut_22: survived
    classificacao.x_classificar_aluno__mutmut_23: survived
    classificacao.x_classificar_aluno__mutmut_24: survived
    classificacao.x_classificar_aluno__mutmut_25: survived
    classificacao.x_classificar_aluno__mutmut_29: survived
    classificacao.x_classificar_aluno__mutmut_30: survived
    classificacao.x_classificar_aluno__mutmut_31: survived
    classificacao.x_classificar_aluno__mutmut_32: survived
    classificacao.x_classificar_aluno__mutmut_33: survived


A) resposta: 
foram gerados: 36 
foram mortos: 6
ficaram vivos: 30


b) Agrupe os vivos pela causa e diga quais estão em linhas que a suíte nem executa
Como classifiquei: para cada um dos 30 mutantes vivos, perguntei:

A linha aparece em Missing? (3, 5, 7, 11) Se sim, a causa é linha não executada.
Se não, o que mudou? Se foi um número ou uma comparação, a causa é valor de fronteira não testado.
Resultado

Causa	Linhas	Mutantes	Quantidade
1. Linha não executada	3, 5, 7, 11	6–9, 15–18, 21–23, 31–33	14
2. Valor de fronteira não testado	2, 4, 6, 8, 10	1–5, 10–14, 19–20, 24–25, 29–30	16
Causa 1: linhas que a suíte não executa (14 vivos)

Linha 3, raise ValueError("Media invalida"): mutantes 6–9
Linha 5, raise ValueError("Presenca invalida"): mutantes 15–18
Linha 7, return "Reprovado por falta": mutantes 21–23
Linha 11, return "Recuperacao": mutantes 31–33
Essas linhas nunca são executadas pelos testes, então trocar a mensagem ou o texto não muda o resultado da suíte.

Causa 2: linhas executadas, mas sem o valor de fronteira (16 vivos)

Linha 2, média inválida (mutantes 1–5): faltam médias 0, 0.5, 10, 10.5 e 11.
Linha 4, presença inválida (mutantes 10–14): faltam presenças -1, 0, 0.5, 100 e 101.
Linha 6, presença 75 (mutantes 19–20): falta classificar_aluno(8.0, 75).
Linha 8, média 7.0 (mutantes 24–25): falta classificar_aluno(7.0, 80).
Linha 10, média 5.0 (mutantes 29–30): falta classificar_aluno(5.0, 80).
Conferência: 14 + 16 = 30 vivos, igual ao total do mutmut



c)Acrescente testes até matar todos os vivos. Algum é equivalente? Qual
o MS final?

testes a matar todos os 30 mutantes vivos.

Os testes cobrem as linhas 3, 5, 7 e 11 (que a suite nao executava) e as
fronteiras de media (0, 0.5, 5.0, 7.0, 10 e 11) e de presenta (-1, 0, 75, 100 e 101).
 Mutantes gerados: 36 | mortos: 36 | vivos: 0
 Equivalente: nenhum. Cada mutante vivo muda o resultado para alguma entrada,
 por isso todos puderam ser mortos.
 MS final = 36 / 36 = 100%

 '''
 
import pytest


def test_aluno_reprovado_por_falta():
    assert classificar_aluno(9.0, 70) == "Reprovado por falta"


def test_aluno_em_recuperacao():
    assert classificar_aluno(6.0, 80) == "Recuperacao"


def test_fronteira_media_7_aprovado():
    assert classificar_aluno(7.0, 80) == "Aprovado"


def test_fronteira_media_5_recuperacao():
    assert classificar_aluno(5.0, 80) == "Recuperacao"


def test_fronteira_presenca_75_nao_reprova_por_falta():
    assert classificar_aluno(8.0, 75) == "Aprovado"


@pytest.mark.parametrize("media, esperado", [
    (0.0, "Reprovado"),
    (0.5, "Reprovado"),
    (10.0, "Aprovado"),
])
def test_medias_nos_limites_validos(media, esperado):
    assert classificar_aluno(media, 80) == esperado


@pytest.mark.parametrize("media", [11.0, -1.0])
def test_media_invalida_lanca_erro(media):
    with pytest.raises(ValueError, match="^Media invalida$"):
        classificar_aluno(media, 80)


@pytest.mark.parametrize("presenca, esperado", [
    (0, "Reprovado por falta"),
    (100, "Aprovado"),
])
def test_presencas_nos_limites_validos(presenca, esperado):
    assert classificar_aluno(8.0, presenca) == esperado


@pytest.mark.parametrize("presenca", [-1, 101])
def test_presenca_invalida_lanca_erro(presenca):
    with pytest.raises(ValueError, match="^Presenca invalida$"):
        classificar_aluno(8.0, presenca)


'''
d)Troque a conferência da mensagem por
pytest.raises(ValueError, match=msg). O que muda?

RESPOSTA d)
Com pytest.raises(ValueError, match=msg), o teste passa a conferir a mensagem
da exceção, e não só o tipo. O match é uma expressão regular usada com
re.search, ou seja, a mensagem só precisa CONTER o padrão em algum ponto.

O que muda nos mutantes:
 Sem match (só ValueError): mutantes 6-9 e 15-18 não morrem, porque a exceção
   continua sendo ValueError, mesmo com outra mensagem.
 Com match="Media invalida" (sem âncora): o mutante 6 morre (mensagem None),
   mas o mutante 7 ("XXMedia invalidaXX") sobrevive, porque contém o trecho.
Com match="^Media invalida$" (âncora): o mutante 7 morre, porque a mensagem
   inteira precisa ser igual. É por isso que o arquivo usa âncoras.

 Verificação: re.search("Media invalida", "XXMedia invalidaXX") -> True (passa,
 mutante sobrevive); re.search("^Media invalida$", "XXMedia invalidaXX") -> None
 (falha, mutante morre). Também é sensível a maiúsculas: "media invalida"
 (mutante 8) não casa com "Media invalida".


'''