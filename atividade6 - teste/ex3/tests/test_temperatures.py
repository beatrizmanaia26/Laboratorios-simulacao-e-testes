import pytest

from temperatures import dia_do_maior, maior


def test_maior_lista_com_varios_valores():
    assert maior([21, 25, 19, 30, 22]) == 30


def test_maior_lista_com_um_valor():
    assert maior([18]) == 18


def test_maior_lista_com_dois_valores():
    assert maior([30, 21]) == 30


def test_maior_lista_vazia_lanca_erro():
    with pytest.raises(ValueError):
        maior([])


def test_dia_do_maior_lista_com_varios_valores():
    assert dia_do_maior([21, 25, 19, 30, 22]) == 3


def test_dia_do_maior_lista_com_um_valor():
    assert dia_do_maior([18]) == 0


def test_dia_do_maior_lista_com_dois_valores():
    assert dia_do_maior([30, 21]) == 0


def test_dia_do_maior_lista_vazia_lanca_erro():
    with pytest.raises(ValueError):
        dia_do_maior([])

'''

a)Implemente a suíte e rode o mutmut. Liste os vivos com o mutmut
show

python3 -m pytest -v

result:


tests/test_temperatures.py::test_maior_lista_com_varios_valores PASSED  [ 12%]
tests/test_temperatures.py::test_maior_lista_com_um_valor PASSED        [ 25%]
tests/test_temperatures.py::test_maior_lista_com_dois_valores PASSED    [ 37%]
tests/test_temperatures.py::test_maior_lista_vazia_lanca_erro PASSED    [ 50%]
tests/test_temperatures.py::test_dia_do_maior_lista_com_varios_valores PASSED [ 62%]
tests/test_temperatures.py::test_dia_do_maior_lista_com_um_valor PASSED [ 75%]
tests/test_temperatures.py::test_dia_do_maior_lista_com_dois_valores PASSED [ 87%]
tests/test_temperatures.py::test_dia_do_maior_lista_vazia_lanca_erro PASSED [100%]

============================== 8 passed in 0.02s =======================


rm -rf mutants
python3 -m mutmut run

RESULT:
⠼ Generating mutants
    done in 56ms (1 files mutated, 0 ignored, 0 unmodified)
⠴ Running stats     
    done
⠇ Running clean tests
    done
⠼ Running forced fail test
    done
Running mutation testing
⠧ 22/22  🎉 11 🫥 0  ⏰ 0  🤔 0  🙁 11  🔇 0  🧙 0
234.33 mutations/second



python3 -m mutmut results

RESULT:
  temperatures.x_maior__mutmut_2: survived
    temperatures.x_maior__mutmut_3: survived
    temperatures.x_maior__mutmut_4: survived
    temperatures.x_maior__mutmut_7: survived
    temperatures.x_maior__mutmut_8: survived
    temperatures.x_dia_do_maior__mutmut_2: survived
    temperatures.x_dia_do_maior__mutmut_3: survived
    temperatures.x_dia_do_maior__mutmut_4: survived
    temperatures.x_dia_do_maior__mutmut_9: survived
    temperatures.x_dia_do_maior__mutmut_11: survived
    temperatures.x_dia_do_maior__mutmut_12: survived


B)Classifique cada vivo como equivalente ou não, com justificativa

1-ler diff do 11 vivos



## temperatures.x_maior__mutmut_2
# temperatures.x_maior__mutmut_2: survived
--- src/temperatures.py
+++ src/temperatures.py
@@ -1,6 +1,6 @@
 def maior(temps):
     if not temps:
-        raise ValueError("lista vazia")
+        raise ValueError(None)
     m = temps[0]
     for t in temps[1:]:
         if t > m:
## temperatures.x_maior__mutmut_3
# temperatures.x_maior__mutmut_3: survived
--- src/temperatures.py
+++ src/temperatures.py
@@ -1,6 +1,6 @@
 def maior(temps):
     if not temps:
-        raise ValueError("lista vazia")
+        raise ValueError("XXlista vaziaXX")
     m = temps[0]
     for t in temps[1:]:
         if t > m:
## temperatures.x_maior__mutmut_4
# temperatures.x_maior__mutmut_4: survived
--- src/temperatures.py
+++ src/temperatures.py
@@ -1,6 +1,6 @@
 def maior(temps):
     if not temps:
-        raise ValueError("lista vazia")
+        raise ValueError("LISTA VAZIA")
     m = temps[0]
     for t in temps[1:]:
         if t > m:
## temperatures.x_maior__mutmut_7
# temperatures.x_maior__mutmut_7: survived
--- src/temperatures.py
+++ src/temperatures.py
@@ -2,7 +2,7 @@
     if not temps:
         raise ValueError("lista vazia")
     m = temps[0]
-    for t in temps[1:]:
+    for t in temps[2:]:
         if t > m:
             m = t
     return m
## temperatures.x_maior__mutmut_8
# temperatures.x_maior__mutmut_8: survived
--- src/temperatures.py
+++ src/temperatures.py
@@ -3,6 +3,6 @@
         raise ValueError("lista vazia")
     m = temps[0]
     for t in temps[1:]:
-        if t > m:
+        if t >= m:
             m = t
     return m
## temperatures.x_dia_do_maior__mutmut_2
# temperatures.x_dia_do_maior__mutmut_2: survived
--- src/temperatures.py
+++ src/temperatures.py
@@ -1,6 +1,6 @@
 def dia_do_maior(temps):
     if not temps:
-        raise ValueError("lista vazia")
+        raise ValueError(None)
     pos = 0
     for i in range(1, len(temps)):
         if temps[i] > temps[pos]:
## temperatures.x_dia_do_maior__mutmut_3
# temperatures.x_dia_do_maior__mutmut_3: survived
--- src/temperatures.py
+++ src/temperatures.py
@@ -1,6 +1,6 @@
 def dia_do_maior(temps):
     if not temps:
-        raise ValueError("lista vazia")
+        raise ValueError("XXlista vaziaXX")
     pos = 0
     for i in range(1, len(temps)):
         if temps[i] > temps[pos]:
## temperatures.x_dia_do_maior__mutmut_4
# temperatures.x_dia_do_maior__mutmut_4: survived
--- src/temperatures.py
+++ src/temperatures.py
@@ -1,6 +1,6 @@
 def dia_do_maior(temps):
     if not temps:
-        raise ValueError("lista vazia")
+        raise ValueError("LISTA VAZIA")
     pos = 0
     for i in range(1, len(temps)):
         if temps[i] > temps[pos]:
## temperatures.x_dia_do_maior__mutmut_9
# temperatures.x_dia_do_maior__mutmut_9: survived
--- src/temperatures.py
+++ src/temperatures.py
@@ -2,7 +2,7 @@
     if not temps:
         raise ValueError("lista vazia")
     pos = 0
-    for i in range(1, len(temps)):
+    for i in range(len(temps)):
         if temps[i] > temps[pos]:
             pos = i
     return pos
## temperatures.x_dia_do_maior__mutmut_11
# temperatures.x_dia_do_maior__mutmut_11: survived
--- src/temperatures.py
+++ src/temperatures.py
@@ -2,7 +2,7 @@
     if not temps:
         raise ValueError("lista vazia")
     pos = 0
-    for i in range(1, len(temps)):
+    for i in range(2, len(temps)):
         if temps[i] > temps[pos]:
             pos = i
     return pos
## temperatures.x_dia_do_maior__mutmut_12
# temperatures.x_dia_do_maior__mutmut_12: survived
--- src/temperatures.py
+++ src/temperatures.py
@@ -3,6 +3,6 @@
         raise ValueError("lista vazia")
     pos = 0
     for i in range(1, len(temps)):
-        if temps[i] > temps[pos]:
+        if temps[i] >= temps[pos]:
             pos = i
     return pos



Dos 11 vivos, 2 são equivalentes e 9 não são.

Equivalentes (2)

- maior, mutante 8:if t > m → if t >= m. Quando t == m, o if passa a atribuir m = t. Como t e m são iguais, a atribuição não muda o valor de m. O retorno é sempre o mesmo, então nenhuma entrada distingue os dois códigos. Equivalente.

- dia_do_maior, mutante 9: range(1, len(temps)) → range(len(temps))`. Na primeira iteração, `i = 0` e a condição é `temps[0] > temps[0]`, que é sempre falsa. pos continua 0, como no original, e o resto do laço é idêntico. Equivalente.

Não equivalentes (9)

Mensagem de erro (6): mutantes 2, 3 e 4 nas duas funções.

- ValueError(None), "XXlista vaziaXX" e "LISTA VAZIA"` trocam a mensagem.
- A mensagem é observável, então existe um teste que mata cada um: um pytest.raises(ValueError, match="^lista vazia$").
- Sobrevivem porque o enunciado pede `pytest.raises(ValueError)` sem conferir a mensagem.



c)Mate os não equivalentes e calcule o MS antes e depois


rode:
cd "/Users/beatrizmanaia/Desktop/FEI 8S/Laboratorios-simulacao-e-testes/atividade6 - teste/ex3"
python3 -m pytest -v
rm -rf mutants
python3 -m mutmut run
python3 -m mutmut export-cicd-stats
cat mutants/mutmut-cicd-stats.json
python3 -m mutmut results


MS antes (suíte com 8 testes):

- Mortos: 11
- Gerados: 22
- Vivos: 11
- MS = 11 / 22 = 50%

MS depois (suíte com 13 testes):

- Mortos: 20
- Gerados: 22
- Vivos: 2 (mutantes 8 de `maior` e 9 de `dia_do_maior`, os equivalentes)
- MS = 20 / 22 ≈ 91%

MS considerando só os não equivalentes:

- Antes: 11 / 20 = 55%
- Depois: 20 / 20 = 00%

'''


def test_maior_lista_vazia_mensagem_exata():
    with pytest.raises(ValueError, match="^lista vazia$"):
        maior([])


def test_dia_do_maior_lista_vazia_mensagem_exata():
    with pytest.raises(ValueError, match="^lista vazia$"):
        dia_do_maior([])


def test_maior_ignora_primeiro_elemento_na_posicao_1():
    assert maior([10, 50]) == 50


def test_dia_do_maior_compara_posicao_1():
    assert dia_do_maior([10, 50]) == 1


def test_dia_do_maior_empate_retorna_primeira_ocorrencia():
    assert dia_do_maior([30, 30]) == 0

''' 
d) Explique por que > virar >= é equivalente numa função e não na outra

maior (mutante 8): EQUIVALENTE (no sentido de ==)
Retorna o valor. Com t == m, m = t não muda o valor, então o retorno é igual.

dia_do_maior (mutante 12): NÃO EQUIVALENTE
Retorna a posição. Com empate, >= move pos para o índice mais recente.
[30, 30]: original retorna 0, mutante retorna 1.

Ressalva: em maior, 0.0 e -0.0 são iguais por ==, mas o mutante pode
devolver -0.0. Não testado.



'''